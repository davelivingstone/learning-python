# Let's check if y is the square root of x:

def sq_root(x, y):
    result1 = x - y
    result2 = y * y
    result3 = x + y
    print(list(((result1, result2, result3))))
    while x > 0 and y > 0:
        if x - y <= y * y <= x + y:
            return True
        else:
            return False
    return False
print(sq_root(4, 2))

# I figured out another way, which is clearer:

def extr_sqrt(x, y):
    squared = y * y
    square_root = x / y
    print(tuple((squared, square_root)))		# If it's true, than this should display the same thing
    if (y * y == x) and (x / y == y):			# as the arguments passed in the function call, just with the decimal value for the second item
        return True
    else:
        return False
print(extr_sqrt(4, 2))

# Here's the version with user input:

for_x = int(input("Enter a number 'x' that we'll use to extract the square root:\n"))
for_y = int(input("Enter a number 'y' and we'll check if it's the square root of 'x':\n"))
def extr_sqrt(x, y):
    squared = y * y
    division_check = x / y
    square_root = x ** 0.5
    print(f"The square root of {x} is {square_root}")
    print(f"{y} times {y} is {squared}, {x} divided by {y} is {division_check}")
    if (y * y == x) and (x / y == y):
        return "That's correct."		# I  wrote f"{x} is a perfect square", but that wasn't the function(sic!) of the function
    else:
        return "It's incorrect."
print(extr_sqrt(for_x, for_y))
