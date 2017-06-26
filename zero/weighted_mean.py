"""
	Day 0/9
	HackerRanks's 10 Days of Stats 

	Given an array, X, of N integers and an array, W, representing the respective weights of X's elements, 
	calculate and print the weighted mean of 's elements. 
	Your answer should be rounded to a scale of  decimal place (i.e.,  format).

	Gabby Ortman 
	26 June 2017
"""

def calculate_weighted_mean(arr, weight_arr, num_elements): 
	numerator = 0 
	denominator = sum(weight_arr)
	for i in range(num_elements): 
		numerator += arr[i] * weight_arr[i]

	return numerator / denominator
		
if __name__ == '__main__':
	num_elements = int(input().strip())
	arr = [int(x) for x in input().split()]
	weight_arr = [int(x) for x in input().split()]
	wmean = calculate_weighted_mean(arr, weight_arr, num_elements)
	print("{0:.1f}".format(wmean))