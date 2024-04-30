from chi2 import chi2

n = 10

S2 = 6.2

σ2 = 5

a = 0.05

H1 = "<"

chi2_seen = (n - 1) * S2 / σ2

print("chi2 наблюдаемое:", chi2_seen)

if H1 == ">":
    Chi2 = chi2(a, n - 1)
    print("Критическая точка:", Chi2)

    if chi2_seen < Chi2:
        print("Нулевая гипотеза принимается")
    else:
        print("Нулевая гипотеза отвергается")
elif H1 == "!=":
    Chi2_l = chi2(1 - a / 2, n - 1)
    Chi2_r = chi2(a / 2, n - 1)
    print("Критические точки:", Chi2_l, Chi2_r)

    if Chi2_l < chi2_seen < Chi2_r:
        print("Нулевая гипотеза принимается")
    else:
        print("Нулевая гипотеза отвергается")
elif H1 == "<":
    Chi2 = chi2(1 - a, n - 1)
    print("Критическая точка:", Chi2)

    if chi2_seen > Chi2:
        print("Нулевая гипотеза принимается")
    else:
        print("Нулевая гипотеза отвергается")
