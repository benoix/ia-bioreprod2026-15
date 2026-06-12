from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def to_zscore(matrix: np.ndarray) -> np.ndarray:
    """Convert each row of ``matrix`` (one gene) to a z-score profile."""
    mean = matrix.mean(axis=1, keepdims=True)
    std = matrix.std(axis=1, ddof=0, keepdims=True)

    safe_std = np.where(std == 0, 1.0, std)
    zscores = (matrix - mean) / safe_std
    zscores[std.squeeze() == 0] = 0.0
    return zscores


def plot_heatmap(zscores: np.ndarray, time_points: np.ndarray, output_path: Path) -> None:
    """Plot the periodic gene expression heatmap (Figure 2A style)."""
    fig, ax = plt.subplots(figsize=(6, 8))

    extent = (time_points[0], time_points[-1], zscores.shape[0], 0)
    im = ax.imshow(
        zscores,
        aspect="auto",
        cmap="cividis",
        vmin=-1.5,
        vmax=1.5,
        extent=extent,
        interpolation="nearest",
    )

    ax.set_xlabel("time (minutes)")
    ax.set_ylabel(f"Top Periodic Genes ({zscores.shape[0]})")
    ax.set_title("Saccharomyces cerevisiae")

    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("z-score")

    fig.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)
