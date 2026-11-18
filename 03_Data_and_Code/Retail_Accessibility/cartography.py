"""Exact synthetic square footprints; cartographic area and network access."""
from pathlib import Path
import json
import networkx as nx


def calculate():
    # A 2 km square road circuit; two minutes per edge, origin at one corner.
    g = nx.cycle_graph(4)
    nx.set_edge_attributes(g, 2, "minutes")
    reached = nx.single_source_dijkstra_path_length(g, 0, cutoff=5, weight="minutes")
    # Explicit square-corner footprint, 0.1 km to each side of the road loop.
    outer_area = 2.2 ** 2
    hole_area = 1.8 ** 2
    return {"synthetic": True, "threshold_minutes": 5,
            "corridor_area_km2": outer_area - hole_area,
            "filled_area_km2": outer_area, "added_area_km2": hole_area,
            "reached_nodes_before": len(reached), "reached_nodes_after": len(reached),
            "interpretation": "Filling the display polygon adds no graph nodes, links, or verified reachable locations."}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "results")
    output = parser.parse_args().output; output.mkdir(parents=True, exist_ok=True)
    result = calculate()
    (output / "cartography.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
