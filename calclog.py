# This is a simple algorithm I came up with to calculate log.
# This is the Python 3.x version:

def calc_log(n):
	'''Computes log to base 2'''
	counter = 0
	while n > 1:
		n //= 2
		#print(n)
		counter += 1
	return counter

user_input = int(input("Enter a number so we can calculate log:\n"))

print(calc_log(user_input))

# For Python 2.x:
#print("Python 2.x version:")
#
#def calc_log(n):
#	'''Computes log to base 2'''
#	counter = 0
#	while n > 0:
#		n /= 2
#		counter += 1
#	return counter
#
#user_input = int(raw_input("Enter a number so we can calculate log:\n"))
#
#print calc_log(user_input)
