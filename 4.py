import math

from student import student

n = 5
m = 6

x_mean = 3.3
y_mean = 2.48

S2_x = 0.25
S2_y = 0.108

a = 0.05

H1 = "<"

T = (x_mean - y_mean) / math.sqrt((n - 1) * S2_x + (m - 1) * S2_y) * math.sqrt(n * m * (n + m - 2) / (n + m))
print("T наблюдаемое:", T)

if H1 == ">":
    t = student(a, n + m - 2)
    print("Критическая точка:", t)

    if T < t:
        print("Нулевая гипотеза принимается")
    else:
        print("Нулевая гипотеза отвергается")
elif H1 == "!=":
    t = student(a, n + m - 2)
    print("Критическая точка:", t)

    if abs(T) < t:
        print("Нулевая гипотеза принимается")
    else:
        print("Нулевая гипотеза отвергается")
elif H1 == "<":
    t = student(a, n + m - 2)
    print("Критическая точка:", t)

    if T > -t:
        print("Нулевая гипотеза принимается")
    else:
        print("Нулевая гипотеза отвергается")