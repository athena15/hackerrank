# HackerRank: Compare the Triplets (Solution)
# https://www.hackerrank.com/challenges/compare-the-triplets/problem


def compareTriplets(a, b):
	a_points = 0
	b_points = 0

	for i in range(3):
		if a[i] > b[i]:
			a_points += 1
		elif a[i] < b[i]:
			b_points += 1
	return a_points, b_points
