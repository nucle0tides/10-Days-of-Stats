"""
	Day 0/9
	HackerRanks's 10 Days of Stats 

	Given an array of  integers, calculate and print the the respective mean, median, and mode on separate lines. 
	If your array contains more than one modal value, choose the numerically smallest one.
	
	Note: Other than the modal value (which will always be an integer), 
	your answers should be in decimal form, rounded to a scale of 1 decimal place.


	Gabby Ortman 
	29 December 2016
"""
class MeanMedianMode(object):
	"""
		hear me out, classes
	"""
	def __init__(self, arr, num_elements):
		self.arr = arr
		self.num_elements = num_elements
		self.mean = None
		self.median = None 
		self.mode = None 

	def calculate_mean(self):
		"""
			The mean is defined as the sum of elements x1 - xk divided by the number of elements k. 
			μ = (Σ xi) / k  
		"""
		element_sum = 0
		for x in self.arr: 
			element_sum += x 
		self.mean = element_sum / self.num_elements

	def get_mean(self): 
		return self.mean
		
	def find_median(self): 
		"""
			The median is defined as the midpoint in a set of ordered elements. 
			If the number of elements, k, is odd, then it is the middle element. 
			If the number of elements, k, is even, then it is the average of the middle two elements. 
		"""
		self.arr.sort()
		midpoint = self.num_elements // 2
		if self.num_elements % 2 == 0: 
			self.median = (self.arr[midpoint] + self.arr[midpoint - 1]) / 2
		else: 
			self.median = self.arr[midpoint]

	def get_median(self): 
		return self.median 

	def find_mode(self):
		"""
			The mode is defined as the element that occurs most frequently in a data set. 
		"""

		#calculate the number of occurances 
		element_occurances = {}
		for element in self.arr:
			if element not in element_occurances.keys(): 
				element_occurances[element] = 1 
			else: 
				element_occurances[element] += 1  

		#find the max occurances
		max_occurances = 0
		for x in element_occurances: 
			if element_occurances[x] > max_occurances: 
				max_occurances = element_occurances[x]

		#remove anything < max occurances
		max_occurances_hash = {}
		for x in element_occurances: 
			if element_occurances[x] == max_occurances: 
				max_occurances_hash[x] = max_occurances

		#get the minimum element with the max number of ocurrances 
		min_element = list(max_occurances_hash.keys())[0] 
		for x in max_occurances_hash: 
			if x < min_element: 
				min_element = x 

		self.mode = min_element

	def get_mode(self): 
		return self.mode 

if __name__ == '__main__':
	num_elements = int(input().strip())
	arr_string = input().strip() 
	arr = [int(x) for x in arr_string.split()]
	GabbysAmazingStatsMachine = MeanMedianMode(arr, num_elements)
	GabbysAmazingStatsMachine.calculate_mean()
	mean = GabbysAmazingStatsMachine.get_mean() 
	GabbysAmazingStatsMachine.find_median() 
	median = GabbysAmazingStatsMachine.get_median()
	GabbysAmazingStatsMachine.find_mode() 
	mode = GabbysAmazingStatsMachine.get_mode()
	print("{0:.1f}".format(mean))
	print("{0:.1f}".format(median))
	print(mode)
	
