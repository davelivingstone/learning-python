# I added the step parameter to the MyRange class from Corey Schafer's tutorial:

class MyRange:

	def __init__(self, start, end, step=1):
		self.start = start
		self.end = end
		self.step = step

	def __iter__(self):
		return self

	def __next__(self):
		if self.start >= self.end:
			raise StopIteration
		current = self.start
		self.start += self.step
		return current

nums = MyRange(1, 10, 2)

print(dir(nums))

for num in nums:
	print(num)

