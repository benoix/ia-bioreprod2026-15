from pathlib import Path

import numpy as np

from figure2arepro.plot import to_zscore


def test_to_zscore() -> None:
    matrix = np.array([[1.0, 2.0, 3.0], [4.0, 4.0, 4.0]])
    zscores = to_zscore(matrix)

    assert zscores.shape == matrix.shape
    assert np.allclose(zscores[0], [-1.22474487, 0.0, 1.22474487], rtol=1e-6)
    assert np.allclose(zscores[1], [0.0, 0.0, 0.0])
