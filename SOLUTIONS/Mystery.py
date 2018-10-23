from functools import reduce
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="filepath", required=True)


def factors(n):
    return len(set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

with open(parser.parse_args().filepath) as reader:
    next(reader)
    for line in reader:
        print(factors(int(line.strip())))
