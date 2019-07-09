# -*- coding: utf-8 -*-
# Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

l = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        l.append(str(i))
print ', '.join(l)


# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.

def fact(x):
    if x == 0:
        return 1
    return (x * fact(x - 1))

x = int(raw_input("Enter a number. "))
print fact(x)


# With a given integral number n, write a program to generate a dictionary
# that contains (i, i*i) such that is an integral number between 1 and n
# (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program: 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n = int(raw_input("Enter a number: "))
d = dict()
for i in range(1, n+1):
    d[i] = i * i
print d


# Write a program which accepts a sequence of comma-separated numbers from
# console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

values = raw_input("Enter a series of numbers: ")
l = values.split(",")
t = tuple(l)
print l
print t

# Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java. Output : java

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))


# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)
# The longer and less practical version that I came up with:
print("The examination will start from : " + str(exam_st_date[0]) + " / " + str(exam_st_date[1]) + " / " + str(exam_st_date[2]))
# The better, more concise version that they provided as a solution:
print( "The examination will start from : %i / %i / %i"%exam_st_date)


#  Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5 
# Expected Result : 615

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

# FizzBuzz exercise:
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz") # I'd write it print(num, "Fizzbuzz")
    elif num % 3 == 0:
        print("Fizz") # Or print(num, "Fizz")
    elif num % 5 == 0:
        print("Buzz") # Or print(num, "Buzz")
    else:
        print(num)
# And one that counts the occurrences of FizzBuzz:

counter = 0
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        counter += 1
    elif number % 3 == 0:
        print("Buzz")
    elif number % 5 == 0:
        print("Fizz")
    else:
        print(number)

print("Total FizzBuzz occurences: {}".format(counter))﻿
 
# Example of the zip() function:

lis1 = ['a', 'b', 'c']
lis2 = [1, 2, 3, 4, 5]

test2 = list(zip(lis1, lis2))

zipped_list = test2[:]

zipped_list_2 = list(test2)

print(test2)
print(zipped_list)
print(zipped_list_2)

# Getting the middle index character in a string:

def get_middle_character(odd_string):
    variable = len(odd_string)/2
    middle_character = odd_string[variable +1]
    return middle_character 
print(get_middle_character("Hakuna matata"))

# Similarly, splitting a string into a first half and a second half:

s = 'Hakuna matata'
middle_index = len(s)/2
first_half, middle, second_half = s[:middle_index], s[middle_index], s[middle_index+1:]
print(first_half, middle, second_half)


from statistics import median
print(median([3, 2, 4, 7, 1, 5, 6]))

from numpy import median
print(median([3, 2, 4, 7, 1, 5, 6]))

def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result
print(factorial(4))

'''Suppose you are given a string and you want to count how many times each letter appears.
There are several ways you could do it:
1. You could create 26 variables, one for each letter of the alphabet. Then you could tra-
verse the string and, for each character, increment the corresponding counter, proba-
bly using a chained conditional.
2. You could create a list with 26 elements. Then you could convert each character to
a number (using the built-in function ord ), use the number as an index into the list,
and increment the appropriate counter.
3. You could create a dictionary with characters as keys and counters as the correspond-
ing values. The first time you see a character, you would add an item to the dictionary.
After that you would increment the value of an existing item.

Each of these options performs the same computation, but each of them implements that
computation in a different way.
An implementation is a way of performing a computation; some implementations are
better than others. For example, an advantage of the dictionary implementation is that we
don’t have to know ahead of time which letters appear in the string and we only have to
make room for the letters that do appear.
Here is what the code might look like:'''

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] +=1
    return d
print(histogram('hullabaloo'))

'''Dictionaries have a method called get that takes a key and a default value. If the key
appears in the dictionary, get returns the corresponding value; otherwise it returns the
default value. As an exercise, use get to write histogram more concisely. You should be able to eliminate
the if statement'''

def histo(s):
	d = {}
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d
print(histo('barracks'))

