# HackerRank: Two Strings (Solution)
# https://www.hackerrank.com/challenges/two-strings/problem
#
# Given two strings, determine if they share a common substring. A substring may be as small as one character.
# For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.


def twoStrings(s1, s2):
	x = set(s1)
	y = set(s2)
	if len(x.intersection(y)) >= 1:
		print('YES')
	else:
		print('NO')