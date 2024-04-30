import math

from student import student

n = 8

r = -0.72

a = 0.05

H1 = "!="

T = r * math.sqrt(n - 2) / math.sqrt(1 - r ** 2)
print("T наблюдаемое:", T)

if H1 == "!=":
    t = student(a, n - 2)
    print("Критическая точка:", t)

    if abs(T) < t:
        print("Нулевая гипотеза принимается")
    else:
        print("Нулевая гипотеза отвергается")
