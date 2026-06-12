from pathlib import Path

import numpy as np

from figure2arepro.io import load_periodic_gene_matrix


def test_load_periodic_gene_matrix(tmp_path: Path) -> None:
    source = Path("data/pgen.1006453.s002.xlsx")
    matrix, gene_ids, time_points = load_periodic_gene_matrix(source)

    assert matrix.shape == (1246, 50)
    assert len(gene_ids) == 1246
    assert np.allclose(time_points, np.arange(0, 250, 5))
    assert all(isinstance(gene_id, str) for gene_id in gene_ids)
