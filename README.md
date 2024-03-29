[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7013396.svg)](https://doi.org/10.5281/zenodo.7013396)

# Monte Carlo Integration

Theory and implementation of Monte Carlo integration in Python.

## Theory

See [docs/monte_carlo_integration.pdf](docs/monte_carlo_integration.pdf) for a write-up of my research notes.

## Example

Here is an example using indicator functions.

```python
import numpy as np

import mcintegration as mci

# Indicator function for being inside a unit sphere in R^N
i = lambda x: np.sum(x**2, -1) <= 1.0

# Area of unit circle in R^2
A_circle, err_one_sigma = mci.mcintegrate(
    i,
    lower=[-1.0] * 2,
    upper=[1.0] * 2,
    n=int(1e5),
)
print(A_circle, err_one_sigma)
# 3.1438 0.00129

# Volume of unit sphere in R^3
V_sphere, err_one_sigma = mci.mcintegrate(
    i,
    lower=[-1.0] * 3,
    upper=[1.0] * 3,
    n=int(1e5),
)
print(V_sphere, err_one_sigma)
# 4.1735 0.00157
```
