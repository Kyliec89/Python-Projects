# Author: Kylie Chambers
# Date: 2/26/2020
# Description: generator function named count_seq that doesn't take
# any parameters and generates a sequence that starts like this:
# 2, 12, 1112, 3112, 132112, 1113122112, 311311222112, 13211321322112, ...

def count_seq():
    number = '2'

    while True:
        yield int(number)
        next_number =''

        while len(number) > 0:
            first = number[0]
            count = 0
            while len(number) > 0 and number[0] == first:
                count = count + 1
                number = number[1:]
            next_number = next_number + '{}{}'.format(count, first)
        number = next_number
