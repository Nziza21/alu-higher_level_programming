#!/usr/bin/python3
"""Solve the N Queens problem using backtracking."""
import sys


def is_safe(board, row, col, n):
    """Check if a queen can be placed at board[row][col]."""
    for i, j in board:
        if j == col or abs(row - i) == abs(col - j):
            return False
    return True


def solve_nqueens(n, row=0, board=[]):
    """Recursively place queens on the board."""
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            solve_nqueens(n, row + 1, board + [[row, col]])


def main():
    """Main function to handle arguments and call solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
