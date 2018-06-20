'''Taken from HackerRank problem found here:
https://www.hackerrank.com/challenges/2d-array/problem'''

# Complete the hourglassSum function below.
def hourglassSum(arr):
	sums = []

	for j in range(0, 4):
		for i in range(0, 4):
			count += sum(arr[j][i:i + 3])
			count += arr[j + 1][i + 1]
			count += sum(arr[j + 2][i:i + 3])
			sums.append(count)
	return max(sums)


array_x = \
	[[1, 1, 1, 0, 0, 0],
	 [0, 1, 0, 0, 0, 0],
	 [1, 1, 1, 0, 0, 0, ],
	 [0, 0, 2, 4, 4, 0],
	 [0, 0, 0, 2, 0, 0],
	 [0, 0, 1, 2, 4, 0]]

assert hourglassSum(array_x) == 19
