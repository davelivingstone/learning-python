'''This is a Fibonacci sequence generator I wrote, after looking at
a series of algorithms. It seems to be pretty fast,although still O(n).
The one on Python.org is based on a while loop and it hinges on a < n,
but I wanted something that would calculate the nth Fibonacci number.
I decided to start it at 1 instead of 0, but that's just my preference;
alternatively, we can just set a = 0 and then use range(n+1).'''

def myfib(n):
	a, b = 1, 1
	for i in range(n):
		print(a)
		a, b = b, a+b
	return a


myfib(10)
myfib(20)
