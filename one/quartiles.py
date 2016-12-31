"""
	Day 1/9
	HackerRanks's 10 Days of Stats 

	Given an array, X, of n integers, calculate the respective first quartile (Q1), 
	second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.

	Gabby Ortman 
	30 December 2016
"""
def median(arr, num_elements, midpoint): 
	"""
		The median is defined as the midpoint in a set of ordered elements. 
		If the number of elements, k, is odd, then it is the middle element. 
		If the number of elements, k, is even, then it is the average of the middle two elements. 
	"""
	if num_elements % 2 == 0: 
		return (arr[midpoint] + arr[midpoint - 1]) // 2
	else: 
		return arr[midpoint]

if __name__ == '__main__':
	num_elements = int(input().strip())
	arr = [int(x) for x in input().split()]
	arr.sort()
	midpoint = num_elements // 2 

	if num_elements % 2 == 0: 
		lower = arr[0 : midpoint]
		upper = arr[midpoint : num_elements]
	else: 
		lower = arr[0 : midpoint]
		upper = arr[midpoint + 1 : num_elements]

	print(median(lower, len(lower), len(lower) // 2))
	print(median(arr, num_elements, midpoint))
	print(median(upper, len(upper), len(upper) // 2))
		
