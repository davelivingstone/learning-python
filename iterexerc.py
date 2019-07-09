# Let's create a class and a generator you can interate through.
# It prints the words in a sentence separately. 
# This is my attempt. First, let's try the class:

class Sentence:

	def __init__(self, s):
		self.s = s.split()
		self.start = -1
		self.end = len(self.s)-1

	def __iter__(self):
		return self

	def __next__(self):
		if self.start >= self.end:
			raise StopIteration
		self.start += 1
		return self.s[self.start]


test = Sentence('This is a test')

for i in test:
	print(i)

# print(next(test))
# print(next(test))

# This is my generator function:

def sentence(s):
	start = 0
	end = len(s.split())
	while start < end:
		yield s.split()[start]
		start += 1


my_sentence = sentence('This is a test')

for i in my_sentence:
	print(i)


# This is Corey Schafer's solution, better than mine, 
# of course, although it looks like I was really close:

class Sentence:

	def __init__(self, sentence):
		self.sentence = sentence
		self.index = 0
		self.words = self.sentence.split()

	def __iter__(self):
		return self

	def __next__(self):
		if self.index >= len(self.words):
			raise StopIteration
		index = self.index
		self.index += 1
		return self.words[index]


my_sentence = Sentence('This is a test')

for word in my_sentence:
	print(word)

# You can use the next method if you want one item at a time:
# print(next(test))
# print(next(test))


# This is Corey's generator function, more practical and simple:

def sentence(sentence):
	for word in sentence.split():
		yield word

my_sentence = sentence('This is a test')

for word in my_sentence:
	print(word)

# And you can do this until you get the StopIteration exception:
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
