import math

from laplace import laplace_arg

n = 10
m = 10

x_mean = 14.3
y_mean = 12.2

D_X = 22
D_Y = 18

a = 0.05

H1 = "<"

Z = (x_mean - y_mean) / math.sqrt((D_X / n + D_Y / m))
print("Z наблюдаемое:", Z)

if H1 == ">":
    laplace_value = (1 - 2 * a) / 2
    z = laplace_arg(laplace_value)
    print("Критическая точка:", z)

    if Z < z:
        print("Нулевая гипотеза принимается")
    else:
        print("Нулевая гипотеза отвергается")
elif H1 == "!=":
    laplace_value = (1 - a) / 2
    z = laplace_arg(laplace_value)
    print("Критическая точка:", z)

    if abs(Z) < z:
        print("Нулевая гипотеза принимается")
    else:
        print("Нулевая гипотеза отвергается")
elif H1 == "<":
    laplace_value = (1 - 2 * a) / 2
    z = laplace_arg(laplace_value)
    print("Критическая точка:", z)

    if Z > -z:
        print("Нулевая гипотеза принимается")
    else:
        print("Нулевая гипотеза отвергается")

