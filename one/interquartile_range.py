"""
	Day 1/9
	HackerRanks's 10 Days of Stats 

	The interquartile range of an array is the difference between its first and third quartiles.

	Given an array, X, of n integers and an array, F, representing the respective frequencies 
	of 's elements, construct a data set, S, where each xi occurs at frequency f. 
	Then calculate and print 's interquartile range, rounded to a scale of  decimal place (i.e., 12.3 format).

	Gabby Ortman 
	31 December 2016
"""
def median(arr, num_elements, midpoint): 
	"""
		The median is defined as the midpoint in a set of ordered elements. 
		If the number of elements, k, is odd, then it is the middle element. 
		If the number of elements, k, is even, then it is the average of the middle two elements. 
	"""
	if num_elements % 2 == 0: 
		return (arr[midpoint] + arr[midpoint - 1]) / 2
	else: 
		return arr[midpoint]


def create_data_set(num_elements, val_arr, freq_arr): 
	ret_arr = []
	for i in range(num_elements): 
		for j in range(freq_arr[i]): 
			ret_arr.append(int(val_arr[i])) 
	ret_arr.sort() 
	return ret_arr

if __name__ == '__main__':
	num_elements = int(input().strip())
	val_arr = input().split() 
	freq_arr = [int(x) for x in input().split()]
	
	val_arr = create_data_set(num_elements, val_arr, freq_arr)
	num_elements = sum(freq_arr)


	midpoint = num_elements // 2 

	if num_elements % 2 == 0: 
		lower = val_arr[0 : midpoint]
		upper = val_arr[midpoint : num_elements]
	else: 
		lower = val_arr[0 : midpoint]
		upper = val_arr[midpoint + 1 : num_elements]

	q1 = median(lower, len(lower), len(lower) // 2)
	q3 = median(upper, len(upper), len(upper) // 2)

	iqr = q3 - q1 
	print("{0:.1f}".format(iqr))