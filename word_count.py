# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# ===================================================

import re
from hash_map import HashMap

"""
This is the regular expression used to capture words. It could probably be endlessly
tweaked to catch more words, but this provides a standard we can test against, so don't
modify it for your assignment submission.
"""
rgx = re.compile("(\w[\w']*\w|\w)")

def hash_function_2(key):
    """
    This is a hash function that can be used for the hashmap.
    """

    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash

def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """

    keys = set()

    ht = HashMap(2500,hash_function_2)

    # This block of code will read a file one word as a time and
    # put the word in `w`. It should be left as starter code.
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:
                w = w.lower()
                if ht.contains_key(w):
                    ht.put(w, ht.get(w)+1)
                else:
                    ht.put(w,1)

        counter = ht.hash_list()
        for i in range(0, len(counter) -1):
            for j in range(0, len(counter)- i - 1):
                if counter[j][1] < counter[j + 1][1]:
                    counter[j], counter[j+1] = counter[j+1], counter[j]

        top =[]
        for i in range(0, number):
            top.append(counter[i])
        return top


#print(top_words("/Users/CashBox/PycharmProjects/261-Portfolio/alice.txt",10))  # COMMENT THIS OUT WHEN SUBMITTING TO GRADESCOPE