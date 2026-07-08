# Snippet 1
result = "Cannot divide by zero"
x = 10 # the error going to be division error
y = 0
if y != 0:
    print(x / y)
else:
    print("Result:", result) # when y is 0 u can not divide it

# Snippet 2
numbers = [1, 2, 3, 4, 5] # the error going to be Indexerror
for i in range(len(numbers)):
    print(numbers[i])

# Snippet 3
def calculate_area(radius): # missing : so error going to be syntaxerror
    area = 3.14 * radius ** 2
    return area
radius = 5
print(calculate_area(radius))

# Snippet 4
def is_even(number): #missing mark so the error going to be Syntaxerror
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))

# Snippet 5 
for i in range(5): # missing mark so syntaxerror
    print(i)

# Snippet 6
def greet(name): # syntax error
    return "Hello,  " + name
print(greet("Alice"))

#snippet 7
numbers = [1, 2, 3, 4, 5] #indentationerror
total = 0
for number in numbers:
    total += number
print("Sum of numbers:", total)

#snippet 8
def factorial(n): # recursion error
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# Snippet 9
name = input("Enter your name: ")
if name == "Alice" or "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")
if name in ("Alice", "Bob"):
    print("Hello, friend!")
else:
    print("Hello, stranger!")

# Snippet 10
def divide_numbers(x, y): #zerodivisonerror"
    if y == 0:
        return "Cannot divide by zero"

    result = x / y
    return result

num1 = 10
num2 = 0
print(divide_numbers(num1, num2))