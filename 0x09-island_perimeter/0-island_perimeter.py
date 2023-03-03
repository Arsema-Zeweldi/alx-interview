#!/usr/bin/python3
"""Returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """island perimeter"""
    seen = set()

    def ip(i, j):
        """i and j are ints"""
        if i >= len(grid) or j >= len(grid[0]) or \
            i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in seen:
            return 0

        seen.add((i, j))
        perimeter = ip(i, j + 1)
        perimeter += ip(i + 1, j)
        perimeter += ip(i, j - 1)
        perimeter += ip(i - 1, j)
        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return ip(i, j)
