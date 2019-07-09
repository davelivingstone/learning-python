'''(Sum the digits in an integer) Write a program that reads
 an integer between 0 and 1000 and adds all the digits in the integer. 
 For example, if an integer is 932 , the sum of all its digits is 14 . 
 (Hint: Use the % operator to extract digits, and use the //
operator to remove the extracted digit. For instance, 932 % 10 = 2 and 932 //
10 = 93 .)'''

# a = 932
# # b = (a // 10) // 10
# # print(b)
# # c = (a // 10) % 10
# # print(c)
# # d = (a % 100) % 10
# # print(d)
# # e = b + c + d
# # print(e)

# b = ((a // 10) // 10) + ((a // 10) % 10) + ((a % 100) % 10)
# print(b)

# # In order to find out how many digits an integer has, use this:
# print(len(str(abs(a))))

# user_input = int(input("Enter a number between 0 and 1000\n"))	
# if len(str(abs(user_input))) == 4:
# 	print((((user_input // 10) // 10) // 10) + ((user_input // 10) % 10) + ((user_input % 100) % 10))
# if len(str(abs(user_input))) == 3:
# 	print(((user_input // 10) // 10) + ((user_input // 10) % 10) + ((user_input % 100) % 10))
# elif len(str(abs(user_input))) == 2:
# 	print((user_input % 10) + (user_input // 10))
# elif len(str(abs(user_input))) == 1:
# 	print(user_input)

# from urllib2 import urlopen
# site = urlopen('http://placekitten.com/250/350')
# data = site.read()
# kitten_file = open('kitteh.jpg', 'w') # 'wb' for Windows systems, else it corrupts the file
# kitten_file.write(data)
# kitten_file.close()

# I had to do some debugging to solve this one, partly 
# because the Codecademy instructions were incomplete.

def cube(number):
    return number**3

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
print(by_three(9))

# Define a function called count that has two arguments called sequence and item.
# Return the number of times the item occurs in the list.

def count(sequence, item):
	sum = 0
	for i in sequence:
		if i == item:
			sum = sum + 1
	return str(sum)

print(count([1, 'Joe', 'Joe', 1, 1, 1, 2, 6], 7))


'''Define a function called purify that takes in a list of numbers, 
removes all odd numbers in the list, and returns the result. 
For example, purify([1,2,3]) should return [2].
Do not directly modify the list you are given as input; 
instead, return a new list with only the even numbers.'''

def purify(lst):
  lst2 = []
  for i in lst:
    if i % 2 == 0:
      lst2.append(i)
  return lst2
print(purify([1, 2, 3, 4, 5, 6]))


'''Define a function called product that takes a list of integers 
as input and returns the product of all of the elements in the list. 
For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).
You can use a loop to go through the elements of the list.
It'll probably be useful to use the *= operator.
Be careful not to start your total at 0, as this would make the overall 
result of the multiplication equal to 0! (Anything multiplied by zero equals zero.)'''

def product(lst):
  total = 1
  for i in lst:
    total *= i
  return total

print(product([1, 3, 7]))


'''Write a function remove_duplicates that takes in a list and 
removes elements of the list that are the same.
For example: remove_duplicates([1, 1, 2, 2]) should return [1, 2].
Don't remove every occurrence, since you need to keep a single 
occurrence of a number.
The order in which you present your output does not matter. 
So returning [1, 2, 3] is the same as returning [3, 1, 2].
Do not modify the list you take as input! Instead, return a new list.
The easiest way to approach this problem is to create a new list in 
your function, loop through your input list, and add items from your 
input list to your new list if the current item is not already contained 
in your new list. Using the a not in b syntax might help you here.
Also, note that destructively modifying a list while you are looping 
through it is bad practice and will likely lead to bugs somewhere down the line! 
That's why we always make a fresh copy to work on.'''

def remove_duplicates(lst):
  lst2 = []
  for i in lst:
    if i not in lst2:
      lst2.append(i)
  return lst2

print(remove_duplicates([1, 1, 1, 2, 2, 3, 4, 5, 5]))


'''Write a function called median that takes a list as an input and 
returns the median value of the list. For example: median([1, 1, 2]) should return 1.
The list can be of any size and the numbers are not guaranteed to be 
in any particular order. 
Make sure to sort it! If the list contains an even number of elements, 
your function should return the average of the middle two.
In order to find the median of a list with an even number of elements, 
you're going to need to find the indices of the middle two elements.
You can find the middle two elements by halving the length of the array 
to find the index of the first element, and subtracting one from the first 
index to find the second index.
For example, with an array of length 6 like [0, 1, 2, 3, 4, 5], the two 
middle elements that need to be averaged in order find the median would be 2 and 3. 
You get 3 by cutting the length of the array in half and 2 by subtracting 1 
from the previous index: 3. You can use a similar pattern to find the middle element 
of an odd-length list.
Last but not least, note that (2 + 3) / 2 is not the same as (2 + 3) / 2.0! 
The former is integer division, meaning Python will try to give you an integer back. 
You'll want a float, so something like (2 + 3) / 2.0 is the way to go.'''

def median(lst):
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0
print(median([2, 1, 3, 4, 5, 7]))

# I found the above solution on stackoverflow, since mine was getting too verbose.
# I was close but, as they say, no cigar. The next one is Codecademy's solution:

def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
   
print(median([2, 4, 5, 9]))

# There's also the median function in statistics and also in numpy, 
# but they wanted us to do it the long way around.

from numpy import median
print(median([5, 2, 3, 8, 9, -2]))

from statistics import median
print(median([3, 2, 4, 7, 1, 5, 6]))

'''Define a function on line 3 called print_grades with one argument, 
a list called grades_input. Inside the function, iterate through 
grades_input and print each item on its own line. After your function, 
call print_grades with the grades list as the parameter.'''

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

print print_grades(grades)

'''Define a function, grades_sum, that does the following:
- Takes in a list of scores, scores.
- Computes the sum of the scores.
- Returns the computed sum.
Call the newly created grades_sum function with the list of 
grades and print the result.'''

def grades_sum(scores):
  total = 0
  for grade in scores:
    total = total + grade	# I was scratching my head for a while, asking myself why it wasn't just giving me the sum
  return total   			# Well, I had indented it too much here and I was getting the entire addition sequence
print grades_sum(grades)	# I just had to indent return total flush with the for loop. Moral of the story: watch HOW MUCH you INDENT

'''Define a function, grades_average, below the grades_sum function 
that does the following:
- Has one argument, grades_input, a list
- Calls grades_sum with grades_input
- Computes the average of the grades by dividing that sum 
by float(len(grades_input)).
- Returns the average.
Call the newly created grades_average function with the list of 
grades and print the result.
Your grades_average function should use the built-in Python 
len function and your grades_sum function to compute the average.
Remember that integer division in Python will always result in an integer. 
We convert len(grades_input) is a float so that the average is a float.'''

def grades_average(grades_input):
  average = grades_sum(grades_input) / float(len(grades_input))
  return average
print grades_average(grades)

'''Define a new function called grades_variance that accepts one argument, 
scores, a list.
- First, create a variable average and store the result of calling 
grades_average(scores).
- Next, create another variable variance and set it to zero. We will use 
this as a rolling sum.
- for each score in scores: Compute its squared difference: 
(average - score) ** 2 and add that to variance.
- Divide the total variance by the number of scores.
- Then, return that result.
- Finally, after your function code, print grades_variance(grades).'''

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score) ** 2
  result = variance / len(scores)
  return result
print grades_variance(grades)

'''The standard deviation is the square root of the variance. 
You can calculate the square root by raising the number to the one-half power.
- Define a function, grades_std_deviation, that takes one argument 
called variance.
- return the result of variance ** 0.5
- After the function, create a new variable called variance and store 
the result of calling grades_variance(grades).
Finally print the result of calling grades_std_deviation(variance).'''

def grades_std_deviation(variance):
  return variance**0.5
  
variance = grades_variance(grades)
print grades_std_deviation(variance)

