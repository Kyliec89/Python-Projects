# Author: Kylie Chambers
# Date: 2/10/2020
# Description: A recursive function that accepts a string and checks if
# it is a palindrome and returns True is so or False otherwise.

def is_palindrome(word):
    if len(word) < 1:
        return True
    else:
        if word[0].lower == word[-1].lower:
            return is_palindrome(word[1:-1])
        else:
            return False