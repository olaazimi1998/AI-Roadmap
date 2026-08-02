# dictionary comprehension:
# dictionary = {key: value for item in iterable}

numbers = {x: x**2
            for x in range(4,10)}
print(numbers)

numbers = {x: x**2 for x in range(4,10) if x % 2 == 0}
print(numbers)

numbers = {x: x **3 for x in range(2,8)}
print(numbers)

numbers = {x: x ** 2 for x in range(3, 6)}
print(numbers)

names = {"ali", "ahmed", "abdullah", "mansor"}
students = {n: len(n) for n in names}
print(students)

# map each student to their index
students = {n: i for i, n in enumerate(names)}
print(students)

students = {i for i, n in enumerate(names)}
print(students)
numbers = [2, 3, 4, 4, 5, 5, 7, 8, 9]
numbers = {x for x in numbers}
print(numbers)


names = ["ali", "ahmed", "sara"]
results = {name: name.upper() for name in names}
print(results)


evens = [3, 4, 6, 8, 10]
numbers = {x * 2 for x in evens if x % 2 == 0}
print(numbers)

lables = [
    "cat",
    "dog",
    "rabbit", 
    "hen"
]

classes = {lable for lable in lables}
print(classes)





classes = {i: lable for i, lable in enumerate(lables, start=1)}
print(classes)

classes = {i: lable for i, lable in enumerate(lables, start=7)}
print(classes)

classes = {lable: i for i, lable in enumerate(lables, start=1)}
print(classes)

students = {
    "ali": 20, 
    "sara": 22, 
    "ahmed": 30, 
    "abdullah": 40
}

new_set = {name: score +10 for name, score in students.items()}
print(new_set)


new_set = {name: score >= 30 for name, score in students.items()}
print(new_set)

new_setter = {name: score for name, score in students.items() if score >= 30 } 
print(new_setter)


predictions = [
    "cat",
    "dog",
    "rabbit",
    "cat",
    "dog",
    "rabbit",

]
new_predictions ={item: predictions.count(item) for item in predictions}
print(new_predictions)

squares = {x**2 for x in range(10)}
print(squares)