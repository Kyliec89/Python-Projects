# Author: Kylie Chambers
# Date: 2/26/2020
# Description: A sort_timer decorator function that compares the
# run time of a bubble sort vs an insertion sort function.

import time
import random
import matplotlib.pyplot as plt

def sort_timer(func):
    def timer(*args, **kwargs):

        time_prior = time.perf_counter()
        func(*args)

        time_after = time.perf_counter()
        return time_after - time_prior

    return timer

def compare_sorts(func1, func2):

    bubble_func = []
    insertion_func =[]

    for items in range(1,11):
        list_1 = [random.randint(1,10000) for x in range(1000*items)]
        list_2 = list(list_1)
        bubble_func.append(func1,(list_1))
        insertion_func.append(func2,(list_2))

    plot_graph(bubble_func)
    plot_graph(insertion_func)

def plot_graph(y):
    x = list(range(1000,11000,1000))
    plt.plot(x,y)
    plt.xlabel("Size")
    plt.ylabel("Time")
    plt.show()

def bubble_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for pass_num in range(len(a_list) - 1):
    for index in range(len(a_list) - 1 - pass_num):
      if a_list[index] > a_list[index + 1]:
        temp = a_list[index]
        a_list[index] = a_list[index + 1]
        a_list[index + 1] = temp

def insertion_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    while pos >= 0 and a_list[pos] > value:
      a_list[pos + 1] = a_list[pos]
      pos -= 1
    a_list[pos + 1] = value
