#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
	"""pascal_triangle"""
	listOfLists = []
	if (n == 0):
		return listOfLists
	for i in range(n):
		listOfLists.append([])
		listOfLists[i].append(1)
		if (i > 0):
			for j in range(1, i):
				listOfLists[i].append(listOfLists[i - 1][j - 1]
					+ listOfLists[i - 1][j])
			listOfLists[i].append(1)
	return listOfLists
