# Q.01-01
print("Q.01-01")
print("The sum of 1 to 5 is:", 1+2+3+4+5)
print()


# Q.02-01
print("Q.02-01")
N = 1
S = 0

while N < 100:
    S += N
    N += 2

print("Sum of odd numbers between 1 and 100:", S)
print()

# Q.02-02
print("Q.02-02")
n = int(input("Enter an integer: "))

if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")
print()

# Q.03-01
print("Q.03-01")
print('*' * 5)
print('# ' * 5)
print()

# Q.04-01
print("Q.04-01")
name = "Piyush Sarkar"
address = "Kasna, Greater Noida"

print("Name:", name)
print("Address:", address)
print()


# Q.05-01
print("Q.05-01")
x = 1
y = 0

print(x and y)
print(x or y)
print(not x)
print(not y)
print()


# Q.06-01
print("Q.06-01")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    print("Ascending order:", a, b)
else:
    print("Ascending order:", b, a)
print()


# Q.07-01
print("Q.07-01")
num = int(input("Enter 0 or 1: "))

if num == 0:
    print("You entered 0")
elif num == 1:
    print("You entered 1")
else:
    print("Invalid input")
print()

# Q.08-01
print("Q.08-01")

for num in range(2, 13):
    for i in range(2, num):
        if num % i == 0:
            print(num, "is Composite")
            break
    else:
        print(num, "is Prime")
print()

# Q.09-01
print("Q.09-01")

for num in range(100, 1000):
    a = num // 100
    b = (num // 10) % 10
    c = num % 10
    
    if num == a**3 + b**3 + c**3:
        print(num)
print()

# Q.10-01
print("Q.10-01")

l1 = ['A', 'B']
l2 = ['1', '2']

for i in l1:
    for j in l2:
        print(i + j)
print()

# Q.11-01
print("Q.11-01")

person = {'Name': 'James', 'Age': 25}
person['Father'] = 'John Doe'

print(person)
print()



# Q.12-01
print("Q.12-01")

lst = [4, 1, 7, 3]

for i in range(len(lst)):
    if lst[i] > lst[-1]:
        lst[i], lst[-1] = lst[-1], lst[i]

print(lst)
print()


#  Q.13-01
print("Q.13-01")

a = [[1, 2], [3, 4], [5, 6]]
new_list = []

for row in a:
    for item in row:
        new_list.append(item)

print(new_list)
print()



# Q.14-01
print("Q.14-01")

maria = {'korean': 85, 'english': 90, 'math': 92, 'science': 90}
average = sum(maria.values()) / len(maria)

print("Average:", average)
print()



# Q.15-01
print("Q.15-01")

import copy

school = {
    'class1': {'student1': 'A'},
    'class2': {'student2': 'B'}
}

school2 = copy.deepcopy(school)

print("school is school2:", school is school2)
print()

# Q.16-01
print("Q.16-01")

scores = (
    ('Hyun', 88, 95, 90),
    ('Min', 85, 90, 92),
    ('Jin', 78, 85, 88),
    ('Lee', 90, 92, 94)
)

names, eng, math, sci = zip(*scores)

average_math = sum(math) / len(math)

print("Average Math Score:", average_math)
print()