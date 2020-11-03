# Author: Kylie Chambers
# Date: 1/12/2020
# Description: A program containing the Person class, which creates objects containing a persons name and age,
# and a function for finding the mean, median, and mode of those ages, using the statistics library and returning
# it as a tuple.

import statistics

class Person:
    """a class that takes a persons name and age and initializes the data members"""
    def __init__(self, name, age):
        """a function that initializes the data members"""
        self.name = name
        self.age = age


def basic_stats(personlist):
    """a function that takes person objects and finds the mean, median, and mode of the ages and
    returns them as a tuple"""
    #a list to store the ages
    age = []

    #a loop that adds the age of each person to the age list
    for number in personlist:
        age.append(number.age)

    #finds the mean of the ages
    mean_ages = statistics.mean(age)

    #finds the median of the ages
    median_ages = statistics.median(age)

    #finds the mode of the ages
    mode_ages = statistics.mode(age)

    #returns the mean, median, and mode as a tuple
    return mean_ages, median_ages, mode_ages
