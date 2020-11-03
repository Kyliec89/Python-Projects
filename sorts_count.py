# Author: Kylie Chambers
# Date: 1/29/2020
# Description: A bubble sort and an insertion sort that count the number of
# exchanges and comparisons made while sorting a list and returns them as a
# tuple.

def bubble_count(my_list):
    """
    a bubble sort function that counts the number of comparisons and exchanges
    made while sorting a list and returns them as a tuple.
    """
    comparisons = 0
    exchanges = 0

    for items in range(len(my_list)):
        for index in range(len(my_list) - 1 - items):

            comparisons = comparisons + 1

            if my_list[index] > my_list[index + 1]:
                temp = my_list[index]
                my_list[index] = my_list[index + 1]
                my_list[index + 1] = temp

                exchanges = exchanges + 1

    return comparisons, exchanges

def insertion_count(my_list):
    """
    a insertion sort function that counts the number of comparisons and exchanges
    made while sorting a list and returns them as a tuple.
    """
    comparisons = 0
    exchanges = 0

    for index in range(1, len(my_list)):
        current_element = my_list[index]
        pos = index - 1
        while pos >= 0:
            comparisons = comparisons + 1
            if my_list[pos] > current_element:
                exchanges = exchanges + 1
                my_list[pos + 1] = my_list[pos]
                pos = pos - 1
            else:
                break

        my_list[pos +1] = current_element

    return comparisons, exchanges