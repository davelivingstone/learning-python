# 1. Function for the Fibonacci sequence with a generator
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b
	
# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break

# 2. Another nice little variation, with the number of iterations:
def fib(num):
    a, b = 0, 1
    for i in range(0, num):
        yield "{}: {}".format(i+1, a)
        a, b = b, a + b

for item in fib(10):
    print(item)

# 3. The simplest form I found:

a, b = 0, 1
for i in range(10):
	print(a)
	a, b = b, a + b
	
# while loop version of the previous solution:

a, b = 0, 1
while a < 10:
	print(a)
	a, b = b, a+b

# DON'T use this version I found on brilliant.com, because it's 
# prohibitively expensive, especially for numbers from the 35th Fibonacci 
# number upwards. It's just an example of using a bad algorithm to solve this problem:
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# Also from brilliant.com, this is a function using a different algorithm, 
# and is much faster, it only needs 999 additions to calculate the number
# (one addition per iteration of the loop):
def smart_fibonacci(n):
	a, b = 0, 1
	for i in range(1, n):
		a, b = b, a+b
	return b

print(smart_fibonacci(1000))

# This variation that also counts how many additions we need to compute
# that particular number:
def smart_fibonacci(n):
    a, b = 0, 1
    if n == 0:
        return a, 0
    additions = 0
    for i in range(1,n):
        a, b = b, a+b
        additions += 1
    return b, additions

print(smart_fibonacci(1000))

# A function that computes Fibonacci numbers up to a certain number, I
# found it on Python.org:
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(1000)

