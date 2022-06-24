from functools import partial
from typing import Callable

import mcintegration as mci
import numpy as np


def repeated_integration(m: int, f: Callable):
    Fs, errs = zip(*[f() for _ in range(m)])
    return np.mean(Fs), np.mean(errs)


def test_mcintegrate_cos():
    f = np.cos
    F, err = repeated_integration(
        100, partial(mci.mcintegrate, f=f, lower=0.0, upper=np.pi / 2)
    )
    assert err < 1e-3
    assert np.allclose(F, 1.0, atol=err * 3)


def test_mcintegrate_nd():
    f = lambda x: np.cos(x[:, 0]) * np.sin(x[:, 1])
    F, err = repeated_integration(
        100, partial(mci.mcintegrate, f=f, lower=[0.0, 0.0], upper=[1.0, 1.0])
    )
    assert err < 1e-3
    assert np.allclose(F, 0.386, atol=err * 3)


def test_mcintegrate_area_circle():
    f = lambda r: 2 * np.pi * r
    F, err = repeated_integration(
        100, partial(mci.mcintegrate, f=f, lower=0.0, upper=1.0)
    )
    assert err < 1e-2
    assert np.allclose(F, np.pi, atol=err * 3)


def test_volume_sphere():
    i = lambda x: np.sum(x**2, -1) <= 1.0
    F, err = repeated_integration(
        100, partial(mci.mcintegrate, f=i, lower=[-1.0] * 3, upper=[1.0] * 3)
    )
    assert err < 1e-2
    assert np.allclose(F, np.pi * 4 / 3, atol=err * 3)
