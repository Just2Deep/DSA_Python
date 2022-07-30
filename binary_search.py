# binary search

query_list = [9, 8, 6, 6, 6, 6, 6, 6, 5, 5, 4, 3, 2, 1]
number = 5


def test_location(query, number, mid):

    if query[mid] == number:
        if mid - 1 >= 0 and query[mid-1] == number:
            return 'left'
        else:
            return 'found'
    elif query[mid] > number:
        return 'right'
    elif query[mid] < number:
        return 'left'


def binary_search(query, number):
    low, high = 0, len(query) - 1

    while low <= high:
        mid = (low + high) // 2

        print(f'low: {low}, high: {high}')

        result = test_location(query, number, mid)

        if result == 'left':
            high = mid - 1
        elif result == 'right':
            low = mid + 1
        elif result == 'found':
            return mid

    return -1


print(binary_search(query_list, number))
