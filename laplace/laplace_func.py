import numpy as np
import scipy


def laplace(x):
    return round(scipy.stats.norm.cdf(x) - 0.5, 8)


def laplace_by_hand(x):
    x = x / 1.414213562
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    p = 0.3275911
    s = np.sign(x)
    t = 1 / (1 + s * p * x)
    b = np.exp(-x * x)
    y = (s * s + s) / 2 - \
        s * (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * b / 2
    return y
