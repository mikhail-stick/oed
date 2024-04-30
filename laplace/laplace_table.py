import csv
from laplace_func import laplace


def main():
    start = 0
    end = 5
    step = 0.01

    x_values = []
    laplace_values = []
    x = start
    while x <= end:
        x_values.append(round(x, 2))
        laplace_values.append(laplace(x))
        x += step

    filename = 'laplace/laplace_values.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'laplace'])
        for i in range(len(x_values)):
            writer.writerow([x_values[i], laplace_values[i]])


if __name__ == "__main__":
    main()
