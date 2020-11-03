# Author: Kylie Chambers
# Date: 1/29/2020
# Description: A binary search function that raises a TargetNotFound exception
# when the target is not  found.

from math import floor

class TargetNotFound(Exception):
    pass

def bin_except(a_list, target):
    """
    Searches a list for the target and returns the index of the position if found, 
    and raises TargetNotFound exception if not found.
    """
    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = floor((first + last) / 2)
        if a_list[middle] == target:
            return middle
        if a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    else:
        raise TargetNotFound
