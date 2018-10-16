import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="filepath", required=True)
args = parser.parse_args()
data = args.filepath

with open(data) as reader:
    next(reader)
    N = M = L = 0
    riders = []
    for line in reader:
        line = line.strip().split()
        if len(line) == 2:
            riders.append(list(map(lambda x: int(x), line)))
        elif len(line) == 3:
            N, M, L = list(map(lambda x: int(x), line))
        else:  # assumes no empty lines
            i = 0
            while sum([x[0] for x in riders if x[0] >= L]) < M:
                riders = [[x[0] + x[1], x[1]] for x in riders]
                i += 1
            print(i)
            riders = []
            continue
    i = 0
    while sum([x[0] for x in riders if x[0] >= L]) < M:
        riders = [[x[0] + x[1], x[1]] for x in riders]
        i += 1
    print(i)
