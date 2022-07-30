# given an array which is sorted in increasing order. find the first and last index of a given element.

query_list = [1, 2, 3, 4, 5, 5, 6, 6, 6, 6, 6, 6, 8, 9]
number = 6


def first_position(query_list, number):

    def condition(mid):
        if query_list[mid] == number:
            if mid - 1 >= 0 and query_list[mid-1] == number:
                return 'left'
            return 'found'
        elif query_list[mid] > number:
            return 'left'
        else:
            return 'right'
    return binary_search(0, len(query_list)-1, condition)


def last_position(query_list, number):

    def condition(mid):

        if query_list[mid] == number:
            if mid < len(query_list) - 1 and query_list[mid+1] == number:
                return 'right'
            return 'found'
        elif query_list[mid] > number:
            return 'left'
        else:
            return 'right'
    return binary_search(0, len(query_list)-1, condition)


def binary_search(low, high, condition):

    while low <= high:

        mid = (low+high)//2
        result = condition(mid)

        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        else:
            low = mid + 1

    return -1


def first_and_last_position(query_list, number):
    return first_position(query_list, number), last_position(query_list, number)


print(first_and_last_position(query_list, number))
