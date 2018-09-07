# HackerRank 'Merge the Tools' Solution - Python (Medium Difficulty)
# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
	for i in range(0, len(string), k):
		output = ''
		unique_letters = set()
		for letter in string[i:i + k]:
			if letter not in unique_letters:
				output += letter
				unique_letters.add(letter)
			else:
				pass
		print(output)


merge_the_tools('AABCAAADA', 1)
