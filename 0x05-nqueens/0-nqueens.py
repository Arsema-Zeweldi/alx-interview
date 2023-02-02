#!/usr/bin/python3
"""The N queens puzzle"""
import sys


def print_board(board, N):
    """Print the board"""
    b = []

    for i in range(N):
        for j in range(N):
            if j == board[i]:
                b.append([i, j])
    print(b)


def isSafe(board, i, j, r):
    """Checks is the queens are in a non-attacking position"""
    return board[i] in (j, j - i + r, i - r + j)


def solveNQueens(board, row, N):
    """Solves the N Queens puzzle"""
    if row == N:
        print_board(board, N)

    else:
        for j in range(N):
            allowed = True
            for i in range(row):
                if isSafe(board, i, j, row):
                    allowed = False
            if allowed:
                board[row] = j
                solveNQueens(board, row + 1, N)


def chessBoard(size):
    return [0 * size for i in range(size)]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    N = sys.argv[1]
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    else:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

    board = chessBoard(int(N))
    row = 0
    solveNQueens(board, row, int(N))
