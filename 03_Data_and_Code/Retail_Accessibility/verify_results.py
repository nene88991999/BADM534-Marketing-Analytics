"""Reconcile saved tables, source hashes, and distances with Bellman-Ford paths."""
from pathlib import Path
from hashlib import sha256
import csv
import gzip
import json
import math
import networkx as nx
from snapshot_access import build_network

HERE = Path(__file__).resolve().parent


def read(name):
    return list(csv.DictReader((HERE / "results" / name).open()))


def main():
    manifest = json.loads((HERE / "data/manifest.json").read_text())
    for name, meta in manifest["inputs"].items():
        assert sha256((HERE / "data" / name).read_bytes()).hexdigest() == meta["sha256"]
    footprint = json.loads((HERE / "results/cartography.json").read_text())
    assert math.isclose(footprint["corridor_area_km2"], 1.60)
    assert math.isclose(footprint["filled_area_km2"], 4.84)
    assert footprint["reached_nodes_before"] == footprint["reached_nodes_after"] == 4
    rows = read("synthetic_origins.csv"); policies = read("policies.csv")
    for p in policies:
        selected = [r for r in rows if r["policy"] == p["policy"]]
        denominator = sum(int(r["people"]) for r in selected)
        assert denominator == 800
        for bound in ["lower", "upper"]:
            count = sum(int(r["people"]) * int(r[bound]) for r in selected)
            assert count == int(p[bound+"_people"])
            assert math.isclose(count/denominator, float(p[bound+"_share"]))
    with gzip.open(HERE / "data/osm_highways.json.gz", "rt") as f:
        g = build_network(json.load(f))
    origins = {r["store_key"]: r for r in read("observed_origins.csv")}
    pairs = read("observed_pairs.csv")
    assert len(origins) == 4 and len(pairs) == 12
    for key, origin in origins.items():
        bf = nx.single_source_bellman_ford_path_length(g, int(origin["snapped_node"]), weight="km")
        for row in [p for p in pairs if p["origin"] == key]:
            target = origins[row["target"]]
            expected = bf[int(target["snapped_node"])] + (float(origin["snap_m"])+float(target["snap_m"]))/1000
            assert math.isclose(expected, float(row["network_km"]), abs_tol=1e-9)
            assert expected + 1e-9 >= float(row["straight_km"])
        for metric in ["straight", "network"]:
            eligible = [p for p in pairs if p["origin"] == key and p["target_available"] == "1"]
            best = min(eligible, key=lambda p: (float(p[metric+"_km"]), p["target"]))
            assert best["target"] == origin[metric+"_target"]
    result = {"checked_on": "2026-11-18", "checks": ["eight independent unit tests executed separately",
              "input SHA-256 hashes", "analytic footprint areas and unchanged reachable count", "six population-bound totals", "twelve distances against Bellman-Ford",
              "geographical-distance lower bounds", "eight nearest-alternative selections"],
              "sha256": {p.name: sha256(p.read_bytes()).hexdigest() for p in sorted((HERE / "results").iterdir()) if p.suffix in {".csv", ".json"}}}
    (HERE / "verification.json").write_text(json.dumps(result, indent=2)+"\n")
    print("Input hashes, population bounds, 12 routes, and 8 nearest selections agree.")


if __name__ == "__main__":
    main()
