import csv


def laplace_arg(laplace):
    filename = 'laplace/laplace_values.csv'

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        data = list(reader)

    res = min(data, key=lambda x: abs(float(x[1]) - laplace))
    return float(res[0])
