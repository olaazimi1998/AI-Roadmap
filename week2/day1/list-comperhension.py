# previosly


numbers = []
for i in range(10):
    numbers.append(i) # type: ignore

print(numbers) # type: ignore

print("\n")
#now
numbers = [i for i in range(10)]

numbers = []
for i in range(1, 20):
    numbers.append(i ** 2) # type: ignore

print(numbers) # type: ignore

print("\n")

numbers = [i ** 3 for i in range(1, 20)]
print(numbers)


numbers = [i + 4 for i in range(6, 9)]
print(numbers)


#even
evens = [i for i in range(20) if i % 2 == 0]
print(evens)

#odd
odds = [i for i in range(20) if i % 3 == 0]
print(odds)

#change words to uppercase
names = ["ali", "sara", "amir"]

upper_names = [name.upper() for name in names]

print(upper_names)


#change word to lowercase
names = ["ALI", "SARA", "AHMED"]
lower_names = [name.lower() for name in names]
print(lower_names)


#len of world
words = ["python", "machine", "learning", "ai"]
lengths = [len(word) for word in words]
print(lengths)

numbers = [i ** 2 for i in range(20) if i % 2 == 0]
print(numbers)


numbers = [i ** 4 if i % 2 == 0 else -i for i in range(10)]
print(numbers)

print("\n")
matrix = [[i * j for j in range(6)] for i in range(7)]
print(matrix)


ages = [15, 21, 30, 40, 50, 18]
adults = [age for age in ages if age >= 18]
print(adults)


Predictions = [0.1, 0.3, 0.8, 0.7, 0,5] # type: ignore
classes = [1 if p > 0.5 else 0 for p in Predictions] # type: ignore
print(classes)


#creat
numbers = [1, 2, 3, 4, 5, 6]
result = [x < 2 for x in numbers]
print(result)

evens = [ x for x in range(20) if x % 2 == 0]
print(evens)


odds = [x for x in range(20) if x % 2 != 0 ]
print(odds)

scores = [20, 50, 69, 90, 79, 78]
results = [len(scores) for score in scores ]
print(results)

# use if else in list comperhencive
numbers = [x if x % 2 == 0 else -x for x in range(8)]
print(numbers)

numbers =[6, 8, 9, 7]
print([x **2 for x in numbers])



# work with strings
names = ["sara", "marwa", "mahdia", "kiara"]
 # type: ignore
new_list = [name.upper() for name in names]
print(new_list)


name = ["ALI", "AHMED", "ABDULLAH", "MANSOR"]
new_list = [name.lower() for name in names]
print(new_list)

#work with dictionaries
students ={
    "ali": 20,
    "sara": 40,
    "andrew": 80, 
    "ahmed": 50,
    "marawa": 20
}

keys = [key for key in students.keys()]
print(keys)
upper_keys = [key.upper() for key in keys]
print(upper_keys)

values = [value for value in students.values()]
print(values)

# work with sets
numbers ={4, 5, 5, 5,6, 7, 8, 0, 9}
print(numbers)

lst = [ x for x in numbers]
print(lst)


matrix =[[i * j for j in range(6)] for i in range(7)]
print(matrix)


matrix = [[3,4], 
          [4,5], [67,89], [5,7]]
flat = [num for row in matrix for num in row]
print(flat)


flat = [num for row in matrix for num in row if num % 2 == 0]
print(flat)

#nested list comprehension
pairs = [(x, y) for x in range(3) for y in range(1)]
print(pairs)

math = [(x,y) for x in range(4) for y in range(2)]
print(math)

#zipping two lists
names = ['sara', 'ali', 'ahmed']
ages = [20, 40, 50]
result = [(name, age) for name, age in zip(names, ages)]
print(result)

# enmurate()
names = ["sara", "ali", "ahmed"]
result = [f"{i}: {name}" for i, name in enumerate(names)]
print(result)

names = ["sara", "ali", "ahmed"]
results = [f"{i}: {name}" for i, name in enumerate(names)]
print(results)


 # raed files
names = [" hoda", "  mana", "  labobo"]
lines = [name.strip() for name in names]
print(lines)

lists = [name.strip() for name in names]
print(lists)

#cleaning data
data = [None, 10, -8, 8, None]
clean = [x for x in data if x is not None and x >= 0]
print(clean)


#prepare for machine learning
predictions = [0.3, 0.5, 0.6, 0.1]
classes = [1 if p >= 0.4 else 0 for p in predictions ]
print(classes)







