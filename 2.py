import math
from laplace import laplace_arg

m = 369
n = 899

p0 = 0.5

a = 0.05

H1 = "!="

w = m / n

Z = (w - p0) / math.sqrt((p0 * (1 - p0)) / n)

print("Z =", Z)

if H1 == ">":
    laplace_value = (1 - 2 * a) / 2

    z_kr = laplace_arg(laplace_value)

    if Z < z_kr:
        print("Нулевая гипотеза отвергается")
    else:
        print("Нулевая гипотеза принимается")
elif H1 == "!=":
    laplace_value = (1 - a) / 2

    z_kr = laplace_arg(laplace_value)

    print("z_kr =", z_kr)

    if abs(Z) < z_kr:
        print("Нулевая гипотеза принимается")
    else:
        print("Нулевая гипотеза отвергается")
elif H1 == "<":
    laplace_value = (1 - 2 * a) / 2

    z_kr = laplace_arg(laplace_value)

    if Z > -z_kr:
        print("Нулевая гипотеза принимается")
    else:
        print("Нулевая гипотеза отвергается")
