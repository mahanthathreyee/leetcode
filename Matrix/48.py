'''
Problem: Rotate Image
Link: https://leetcode.com/problems/rotate-image/
Tags: Matrix, Array
'''


class Solution:
    def rotate(self, M: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(M)
        for i in range(n):
            for j in range(i + 1, n):
                M[i][j], M[j][i] = M[j][i], M[i][j]
            M[i].reverse()
