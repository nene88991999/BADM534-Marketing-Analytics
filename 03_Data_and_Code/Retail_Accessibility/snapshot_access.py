"""Frozen restaurant statuses and a later illustrative OSM network; distances in km."""
from pathlib import Path
import csv
import gzip
import json
import math
import networkx as nx
from accessibility import write_csv

HERE = Path(__file__).resolve().parent
ALLOWED = {"residential", "living_street", "pedestrian", "footway", "path", "steps",
           "service", "unclassified", "tertiary", "tertiary_link", "secondary",
           "secondary_link", "primary", "primary_link"}


def haversine(a, b):
    lat1, lon1, lat2, lon2 = map(math.radians, (*a, *b))
    h = math.sin((lat2-lat1)/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin((lon2-lon1)/2)**2
    return 6371.0088 * 2 * math.asin(math.sqrt(min(1, h)))


def build_network(data):
    elements = data["elements"]
    coordinates = {e["id"]: (e["lat"], e["lon"]) for e in elements if e["type"] == "node"}
    g = nx.Graph()
    for way in (e for e in elements if e["type"] == "way"):
        tags = way.get("tags", {})
        if tags.get("highway") not in ALLOWED or tags.get("area") == "yes":
            continue
        if tags.get("foot") in {"no", "private"}:
            continue
        if tags.get("access") in {"no", "private"} and tags.get("foot") not in {"yes", "designated", "permissive"}:
            continue
        # Undirected connectivity is an imposed convention, not verified pedestrian routing.
        for a, b in zip(way["nodes"], way["nodes"][1:]):
            if a not in coordinates or b not in coordinates or a == b:
                continue
            pa, pb = coordinates[a], coordinates[b]
            if not all(40.08 <= p[0] <= 40.155 and -88.30 <= p[1] <= -88.185 for p in [pa, pb]):
                continue
            km = haversine(pa, pb)
            if km > 0 and (not g.has_edge(a, b) or km < g[a][b]["km"]):
                g.add_edge(a, b, km=km, osm_way=way["id"])
    nx.set_node_attributes(g, {n: coordinates[n] for n in g}, "latlon")
    return g


def main(output=HERE / "results"):
    output = Path(output); output.mkdir(parents=True, exist_ok=True)
    with gzip.open(HERE / "data/osm_highways.json.gz", "rt") as f:
        osm = json.load(f)
    g = build_network(osm)
    stores = list(csv.DictReader((HERE / "data/restaurants.csv").open()))
    assert len({s["store_key"] for s in stores}) == len(stores)
    snaps = {}
    for s in stores:
        p = (float(s["lat"]), float(s["lon"]))
        node = min(g, key=lambda n: (haversine(p, g.nodes[n]["latlon"]), n))
        km = haversine(p, g.nodes[node]["latlon"])
        if km > 0.2:
            raise ValueError("Origin farther than 200 m from selected graph")
        snaps[s["store_key"]] = (node, km, p)
    pairs = []
    for a in stores:
        node, connector, p = snaps[a["store_key"]]
        lengths = nx.single_source_dijkstra_path_length(g, node, weight="km")
        for b in stores:
            if a["store_key"] == b["store_key"]:
                continue  # Alternatives always exclude the origin restaurant.
            dest, end_connector, q = snaps[b["store_key"]]
            route = lengths.get(dest, math.inf) + connector + end_connector
            pairs.append(dict(origin=a["store_key"], target=b["store_key"],
                              target_available=int(b["available"]), straight_km=haversine(p, q),
                              network_km=route if math.isfinite(route) else None))
    rows = []
    for s in stores:
        eligible = [p for p in pairs if p["origin"] == s["store_key"] and p["target_available"] == 1]
        row = dict(store_key=s["store_key"], street=s["street"], available=int(s["available"]),
                   snapped_node=snaps[s["store_key"]][0],
                   snap_m=1000*snaps[s["store_key"]][1],
                   candidate_alternatives=len(eligible))
        for metric in ["straight", "network"]:
            valid = [p for p in eligible if p[metric+"_km"] is not None]
            best = min(valid, key=lambda p: (p[metric+"_km"], p["target"]), default=None)
            row[metric+"_target"] = best["target"] if best else None
            row[metric+"_km"] = best[metric+"_km"] if best else None
        rows.append(row)
    summary = {"synthetic": False, "observed_status_date": "2026-10-24",
               "network_osm_base": osm["osm3s"]["timestamp_osm_base"],
               "origin_denominator": len(stores), "unavailable": sum(1-int(s["available"]) for s in stores),
               "network_nodes": g.number_of_nodes(), "network_edges": g.number_of_edges(),
               "components": nx.number_connected_components(g),
               "snapped_components": [len(nx.node_connected_component(g, snaps[s["store_key"]][0])) for s in stores],
               "within_4km": {m: sum(r[m+"_km"] is not None and r[m+"_km"] <= 4 for r in rows) for m in ["straight", "network"]},
               "scope": "Four observed restaurant origins; same-chain alternatives in fixed box; later undirected network and straight snapping connectors are imposed."}
    write_csv(output / "observed_pairs.csv", pairs)
    write_csv(output / "observed_origins.csv", rows)
    (output / "observed_summary.json").write_text(json.dumps(summary, indent=2)+"\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "results")
    main(parser.parse_args().output)
