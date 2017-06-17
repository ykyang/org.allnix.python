import io


def print_all(f: io.TextIOBase):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(lineCount, f):
    print(lineCount, f.readline()[:-1])  # strip off the trailing \n


ins = open('ex15_example.txt')
# print(type(ins) is io.TextIOWrapper)

print_all(ins)

rewind(ins)

print()

lineIndex = 1
print_a_line(lineIndex, ins)

lineIndex += 1
print_a_line(lineIndex, ins)

lineIndex += 1
print_a_line(lineIndex, ins)
