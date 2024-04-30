from scipy import stats


def student(a, n):
    return stats.t.ppf(1 - a / 2, df=n)
