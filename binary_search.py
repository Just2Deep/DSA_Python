# binary search

query_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
number = 3


def binary_search(query, number):
    low, high = 0, len(query) - 1

    while low <= high:
        mid = (low + high) // 2

        print(f'low: {low}, high: {high}, mid: {mid}')

        if query[mid] < number:
            high = mid - 1
        elif query[mid] > number:
            low = mid + 1
        else:
            return mid

    return -1


print(binary_search(query_list, number))
