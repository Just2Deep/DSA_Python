# This is a code for linear search algorithm.

number_list = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8]
number = 9


def linear_search(number_list, number):

    position = 0

    while position < len(number_list):
        if number_list[position] == number:
            return position
        position += 1

    return -1


print(linear_search(number_list, number))
