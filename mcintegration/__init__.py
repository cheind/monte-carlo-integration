from typing import Protocol

import numpy as np


class Integrand(Protocol):
    """Signature for the function to be integrated.

    The integrand is any function,

        f: R^D -> R.

    Its assumed that the integrand supports vectorization,

        f: R^(NxD) -> R^N.
    """

    def __call__(self, x: np.ndarray) -> np.ndarray:
        """Evaluates the function at x.

        Params:
            x: (NxD) array

        Returns:
            y: N array
        """


def mcintegrate(
    f: Integrand,
    lower: np.ndarray,
    upper: np.ndarray,
    n: int = int(1e5),
    gen: np.random.Generator = None,
) -> tuple[float, float]:
    """Numerically integrate a function using Monte Carlo approach.

    Params:
        f: the integrand that maps f: R^(NxD) -> R^N for N samples.
        lower: (D,) array. Inclusive lower bounds of integration
        upper: (D,) array. Inclusive upper bounds of integration
        n: Number of samples
        gen: random number generator to be used to draw samples. If None,
            default is used.

    Returns:
        F: estimate of the integral
        err: estimate of the 1-sigma approximation error

    Example:
        Integral of cosine
        >>> F, err = mcintegrate(np.cos, 0.0, np.pi/2)
        >>> f'{F:.2f}'
        '1.00'

        Volume of unit sphere
        >>> i = lambda x: np.sum(x**2, -1) <= 1.0
        >>> F, err = mcintegrate(i, [-1.0] * 3, [1.0] * 3, n=int(1e6))
        >>> abs(F-(4/3*np.pi)) < 1e-2
        True

    See:
        Taboga, Marco (2021). "The Monte Carlo method",
        Lectures on probability theory and mathematical statistics.
        https://www.statlect.com/asymptotic-theory/Monte-Carlo-method.
    """

    if gen is None:
        gen = np.random.default_rng()

    lower = np.asfarray(np.atleast_1d(lower))
    upper = np.asfarray(np.atleast_1d(upper))

    d = upper - lower
    eps = np.finfo(upper.dtype).eps

    s = gen.uniform(lower, upper + eps, size=(n, lower.shape[0]))
    y = f(s)

    mci = np.prod(d) / n * y.sum()
    mce = np.sqrt(1 / n * np.var(y))

    return mci, mce
