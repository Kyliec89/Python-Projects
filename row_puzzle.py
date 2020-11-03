# Author: Kylie Chambers
# Date: 2/10/2020
# Description: A recursive function that accepts a list of integers
# and returns True if the puzzle is solvable for that row, or False
# otherwise.

def puzzle_helper(numbers, x):
    y = numbers[x]
    if y == -1:
        return False
    if y == 0:
        return True
    numbers[x] = -1
    left = right = False
    if(x+y < len(numbers)):
        left = puzzle_helper(numbers, x+y)
    if(0 <= x-y):
        right = puzzle_helper(numbers, x-y)
    if left == True or right == True:
        return True
    return False

def row_puzzle(numbers):
    return puzzle_helper(numbers, 0)
