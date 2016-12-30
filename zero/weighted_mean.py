"""
	Day 0/9
	HackerRanks's 10 Days of Stats 

	Given an array, X, of N integers and an array, W, representing the respective weights of X's elements, 
	calculate and print the weighted mean of 's elements. 
	Your answer should be rounded to a scale of  decimal place (i.e.,  format).

	Gabby Ortman 
	30 December 2016
"""

class WeightedMean(object):
	"""
		Class representing the Weighted Mean 
	"""
	def __init__(self, arr, num_elements, weight_arr):
		self.arr = arr 
		self.num_elements = num_elements
		self.weight_arr = weight_arr 
		self.weighted_mean = None

	def calculate_weighted_mean(self): 
		numerator = 0 
		denominator = sum(self.weight_arr)
		for i in range(self.num_elements): 
			numerator += self.arr[i] * self.weight_arr[i]

		self.weighted_mean = numerator / denominator

	def get_wmean(self): 
		return self.weighted_mean
		
if __name__ == '__main__':
	num_elements = int(input().strip())
	arr = [int(x) for x in input().split()]
	weight_arr = [int(x) for x in input().split()]
	GabbysAmazingStatsMachine = WeightedMean(arr, num_elements, weight_arr)
	GabbysAmazingStatsMachine.calculate_weighted_mean()
	wmean = GabbysAmazingStatsMachine.get_wmean() 
	print("{0:.1f}".format(wmean))