# From the MIT course number 6.0001, Introduction to Computer Science and
# Programming in Python, Fall 2016.

# Time is not a good evaluator of program efficiency, as it varies as a result of
# too many things (algorithms, implementations, computers, small or large inputs)

import time

def c_to_f(c):
    return c*9/5 + 32

t0 = time.clock()
c_to_f(100000)
t1 = time.clock() - t0
print("t =", t0, ":", t1, "s")  # There was an apparent mistake here, "t=", t, but t wasn't defined

# Counting operations is a little better for evaluating program efficiencyself.
# Here, we have 3x + 2 operations (3x + 1 + another 1 from the return statement):
def mysum(x):
    total = 0
    for i in range(x+1):
        total += 1
    return total

print(mysum(10))

# Unfortunately, it's still affected by the implementation. If we change the for
# loop to a while loop, we have an extra operation, because I both have to set
# the value of i and test the value of i, as well as doing all the operations
# that come afterwards. So, I'd get 4x + 1:
def my_sum(x):
    i = 0
    while i < x + 1:
        i += 1
    return i

print(my_sum(10))

# Different inputs change how the program runs. This is a function that searches
# for an element in a list:
def search_for_elmt(l, e):
	for i in l:
		if i == e:
			return True
	return False

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(search_for_elmt(l, 10))

# We can start talking about orders of growth. Here's a function that computes
# factorial:
def fact_iter(n):
    '''assumes n an int >= 0'''
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer
print(fact_iter(8))

# Linear search on an unsorted list:
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found

print(linear_search(l, 5))      # I always test the code by calling the function inside print()


# Linear search on a sorted list. It only needs to search until it reaches
# a number greater than e. Since it's sorted, it's clear e isn't in the list.
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

l2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']    # Tried it on a list of strings too
print(search(l2, 'z'))

# Add characters of a string, assumed to be composed of decimal digits:
def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val

print(addDigits('1234567'))

# Quadratic complexity. Function to determine if one list is a subset of the
# second, i.e. every element in first appears in second (assume no duplicates):
def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True

print(isSubset([4, 5, 6], [1, 2, 3, 4, 5, 6, 7]))

#Quadratic complexity. Find intersection of two lists, return a list with each
# element appearing only once:
def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):   # I think if e not in res is clearer than if not(e in res)
            res.append(e)
    return res

print(intersect([1, 1, 2, 3, 6, 8], [1, 2, 3, 4, 5, 6, 7, 3]))

# Don't use this function, it's just an example of a function that computes
# n squared very inefficiently:
def g(n):
    '''assumes n >= 0'''
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x

print(g(3))

# Bisection search implementation 1:
def bisect_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) // 2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)

print(bisect_search1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))

# Bisection search implementation 2, more efficient than the previous one:
def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False    # nothing left to search
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)

print(bisect_search2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14))

# Another example of logarithmic complexity:
def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i//10
    return result

print(intToStr(55))

# Exponential complexity. A function that generates all the subsets of a set:
def genSubsets(L):
    if len(L) == 0:
        return [[]]     # list of empty list
    smaller = genSubsets(L[:-1])   # all subsets without the last element
    extra = L[-1:]      # create a list of just the last element
    new = []
    for small in smaller:
        new.append(small+extra) # for all smaller solutions, add one with last element
    return smaller+new      # combine those with last element and those without

print(genSubsets([1, 2, 3, 4]))

# Complexity of iterative Fibonacci. Best case: O(1), worst case: O(1) + O(n) + O(1) = O(n).
def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n-1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
        return fib_ii

print(fib_iter(8))

# Complexity of recursive Fibonacci. Worst case: O(2^n).
def fib_recur(n):
    '''assumes n an int >= 0'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

print(fib_recur(8))
