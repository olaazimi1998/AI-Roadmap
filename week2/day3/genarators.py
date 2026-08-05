
from collections.abc import Iterator


def list_numbers():
    return [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 9, 10]

print(list_numbers())


def test():
    return 10
    return 20

print(test())


def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7

gen = numbers()
print(next(gen))
print(next(gen))


def count():
    for i in range(1, 11):
        yield i
for number in count():
    print(number)


print("Generator expression")


def squares(n: int) -> Iterator[int]:
    for i in range(n):
        yield i ** 1
        yield i ** 3
for item in squares(6):
    print(item)


def even_numbers(limit: int) -> Iterator[int]:
    for i in range(limit):
        if i % 2 == 0:
            yield i

for number in even_numbers(20):
    print(number)

def read_file(filename: str) -> Iterator[str]:
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

for line in read_file("week2/day3/number.txt"):
    print(line)


def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()
for line in read_file("week2/day3/number.txt"):
    print(line)

def csv_reader(file_name):
    with open(file_name) as file:
        for row in file:
            yield row.strip().split(",")

for row in csv_reader("week2/day3/dataset.csv"):
    print(row)



def read_file(file_name):
    with open(file_name, "r") as file:
        for line in file:
            number = int(line.strip())
            if number > 50:
                yield number

for line in read_file("week2/day3/number.txt"):
    print(line)




def csv_reader(file_name):
    with open(file_name) as file:
        for row in file:
            yield row.strip().split(",")


for row in csv_reader("week2/day3/dataset.csv"):
    print(row)




def csv_reader(file_name):
    with open(file_name) as file:
        

            first_line = next(file)
            yield first_line.strip().split(",")


for row in csv_reader("week2/day3/dataset.csv"):
    print(row)

    



















































