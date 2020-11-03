# Author: Kylie Chambers
# Date: 1/29/2020
# Description: A box class that accepts parameters for length, width and height of the box,
# and a method to return the volume of the box. Plus a function that uses insertion sort to
# sort a list of boxes from greatest volume to least.

class Box:
    """
    A box class that accepts parameters for length, width and height of the box,
    and a method to return the volume of the box.
    """
    def __init__(self, length, width, height):
        """
        creates a new box, accepting its length, width and height as parameters
        """
        self.length = length
        self.width = width
        self.height = height
    def volume(self):
        """
        Finds the volume of the box and returns it
        """
        return self.length * self.width * self.height

def box_sort(box_list):
    """
    Sorts a list of boxes by volume from greatest to least.
    """
    for index in range(1, len(box_list)):
        current_element = box_list[index]
        pos = index
        while current_element.volume() > box_list[pos-1].volume() and pos > 0:
            box_list[pos] = box_list[pos - 1]
            pos = pos - 1
        box_list[pos] = current_element
