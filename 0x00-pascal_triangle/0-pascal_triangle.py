#!/usr/bin/python3
"""
pascal's triangle - interview prep
"""


def pascal_triangle(n):
    """
    implementation of pascal's famous triangle
    """
    triangle = [[1]]
    if n > 0:
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)
        return triangle
    return []
