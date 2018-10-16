def read_file(filename):
    line = ""
    with open(filename, mode="r") as f:
        line += f.readline()
    return line


print(read_file("sample.txt"))