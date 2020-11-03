# Author: Kylie Chambers
# Date: 1/29/2020
# Description: An insertion sort function that lists of sorts strings in
# alphabetical order, ignoring case.

def string_sort(string_list):
    """
    An insertion sort function that sorts strings and
    ignores case.
    """
    for index in range(1, len(string_list)):
        current_element = string_list[index]
        pos = index - 1
        while pos >= 0 and string_list[pos].lower() > current_element.lower():
            string_list[pos + 1] = string_list[pos]
            pos = pos - 1
        string_list[pos +1] = current_element
        