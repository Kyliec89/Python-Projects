# Author: Kylie Chambers
# Date: 2/10/2020
# Description: A recursive function that accepts a list of numbers as a parameter
# and returns the largest number.

def array_max(numbers):
    max = numbers[0]
    return find_max(numbers, max)

def find_max(numbers, max):
    if(len(numbers)==1):
        return max
    else:
        if numbers[0] > max:
            max = numbers[0]
        numbers.remove(numbers[0])
        return find_max(numbers, max)
