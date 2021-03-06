"""
	Day 1/9
	HackerRanks's 10 Days of Stats 
	


	Gabby Ortman 
	31 December 2016
"""
import math 

def calculate_mean(arr, num_elements):
	"""
		The mean is defined as the sum of elements x1 - xk divided by the number of elements k. 
		μ = (Σ xi) / k  
	"""
	element_sum = 0
	for x in arr: 
		element_sum += x 

	return element_sum / num_elements

def variance(arr, num_elements, mean): 
	ret_sum = 0
	for i in range(num_elements): 
		difference = arr[i] - mean 
		ret_sum += (difference ** 2)
	return ret_sum

def standard_deviation(variance, num_elements): 
	return math.sqrt(variance, / num_elements)

if __name__ == '__main__':
	num_elements = int(input().strip())
	arr = [int(x) for x in input().split()]
	mean = calculate_mean(arr, num_elements)
	variance = variance(arr, num_elements, mean)
	st_dev = standard_deviation(variance / num_elements)
	print("{0:.1f}".format(st_dev))