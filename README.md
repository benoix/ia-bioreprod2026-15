# Figure 2A Reproduction

`figure2a-reproduction` is a lightweight Python package that loads periodic gene expression data from the Kelliher et al. (2016) supplementary table and generates the Figure 2A-style heatmap used in the publication.

## Features

- Load normalized periodic gene datasets from the provided Excel file
- Filter and order genes using the published periodicity criteria
- Convert gene expression profiles to z-scores
- Render a publication-ready heatmap
- CLI and Python API support

## Installation

```bash
python -m pip install --upgrade pip
python -m pip install .
```

For development:

```bash
python -m pip install -e .[dev]
```

## Usage

### Command line

```bash
python -m figure2arepro data/pgen.1006453.s002.xlsx -o figure2A_reproduction.png
```

Or after installation:

```bash
figure2a-reproduction data/pgen.1006453.s002.xlsx -o figure2A_reproduction.png
```

### Python API

```python
from pathlib import Path
from figure2arepro.io import load_periodic_gene_matrix
from figure2arepro.plot import to_zscore, plot_heatmap

matrix, gene_ids, time_points = load_periodic_gene_matrix(Path("data/pgen.1006453.s002.xlsx"))
zscores = to_zscore(matrix)
plot_heatmap(zscores, time_points, Path("figure2A_reproduction.png"))
```

## Repository structure

- `src/figure2arepro/` - package source code
- `data/` - raw dataset used for regression testing and figure reproduction
- `tests/` - unit tests
- `.github/workflows/ci.yml` - continuous integration pipeline

## Testing

Run unit tests with:

```bash
python -m pytest
```

## Quality checks and CI

This repository includes a GitHub Actions workflow to:

- run `ruff` linting
- execute unit tests with `pytest`
- build the package with `python -m build`
- generate API documentation using `pdoc`

## License

MIT License
