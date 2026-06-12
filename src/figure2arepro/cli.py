from __future__ import annotations

import argparse
from pathlib import Path

from .io import load_periodic_gene_matrix
from .plot import plot_heatmap, to_zscore


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a Figure 2A-style heatmap from Kelliher et al. 2016 periodic gene data."
    )
    parser.add_argument("xlsx_path", type=Path, help="Path to S1 Table (.xlsx) input file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("figure2A_reproduction.png"),
        help="Output image path (default: figure2A_reproduction.png)",
    )
    args = parser.parse_args()

    matrix, gene_ids, time_points = load_periodic_gene_matrix(args.xlsx_path)
    zscores = to_zscore(matrix)
    plot_heatmap(zscores, time_points, args.output)

    print(f"Loaded {len(gene_ids)} periodic genes x {len(time_points)} time points.")
    print(f"Figure saved to: {args.output}")
