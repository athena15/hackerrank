# HackerRank "Write a function" Leap Year challenge
# https://www.hackerrank.com/challenges/write-a-function/problem


def is_leap(year):
	leap = False
	if year % 4 == 0:
		if year % 400 == 0:
			return True
		elif year % 100 == 0:
			return False
		else:
			return True
	else:
		return False


is_leap(1990)
