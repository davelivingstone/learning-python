# I wrote this binary search function based on a Khan Academy
# JS/pseudocode exercise that I solved. It assumes that the list
# it receives as its first argument is already sorted.

def binary_search(l, val):
	minimum = 0
	maximum = len(l)-1
	num = 0
	while minimum <= maximum:
		guess = int((minimum+maximum)/2)
		num += 1
		if val == l[guess] or minimum == maximum:
			print(f'Guess: {guess}, value: {l[guess]})')
			print(f'Number of guesses: {num}')
			return guess;
		elif val < l[guess]:
			minimum = guess + 1
		else:
			maximum = guess - 1
		print(f'Guess: {guess}, value: {l[guess]})')
	print(f'Number of guesses: {num}')
	return -1

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

binary_search(primes, 73)
binary_search(primes, 41)
binary_search(primes, 42)

