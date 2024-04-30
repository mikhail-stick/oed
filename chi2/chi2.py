from scipy import stats


def chi2(a, n):
    return stats.chi2.ppf(1 - a, df=n)
