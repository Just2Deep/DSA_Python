"""
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the 0 element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].
"""

nums = [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]
print(nums)
# 0 solving in linear search way


def count_rotations(nums):
    pos = 0

    while pos < len(nums):
        if nums[pos] < nums[pos-1]:
            return pos

        pos += 1
    return 0


print(count_rotations(nums))


# now let's reduce the complexity since the list is sorted by using binary search.

def binary_count_rotations(nums):

    def condition(mid):
        if nums[mid] < nums[mid-1]:
            return 'found'
        elif nums[mid] < nums[-1]:
            return 'left'
        else:
            return 'right'

    count = binary_search(0, len(nums)-1, condition)

    return 0 if count == -1 else count


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


print(binary_count_rotations(nums))


"""
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. You are also given a target number. Write a function to find the position of the target number within the rotated list. You can assume that all the numbers in the list are unique.

Example: In the rotated sorted list [5, 6, 9, 0, 2, 3, 4], the target number 2 occurs at position 5.
"""

# modify our binary_count_rotations to solve this issue or we can split the list into 2 sorted subarrays and apply binary search for it.


def binary_count_rotations_prob(nums, target):

    def condition(mid):
        if nums[mid] == target and nums[mid - 1] < nums[mid]:
            return 'found'

        # When mid is smaller than 0
        if nums[mid] < nums[0]:         # [5, 6, 9, 0, 2, 3, 4], [5,6,0,1,2,3,4]
            if nums[mid] < nums[mid-1]:     # middle is the smallest [5, 6, 9, 0, 2, 3, 4]
                if target >= nums[0]:   # target 5,6,9
                    return 'left'
                else:                       # target 2,3,4
                    return 'right'
            else:                           # [5,6,0,1,2,3,4]
                if target >= nums[0] or target < nums[mid]:   # target 5,6,0
                    return 'left'
                elif target > nums[mid] and target < nums[0]:  # target 2,3,4
                    return 'right'

            # When mid is greater than 0
        # [4,5,6,7,0,1,2], [4,5,6,7,8,9,0,1,2]
        else:
            if target < nums[mid] and target >= nums[0]:  # target 4,5,6 and 4,5,6,7
                return 'left'
            elif target > nums[mid] or target < nums[0]:  # target 9 and 0,1,2
                return 'right'

    count = binary_search(0, len(nums)-1, condition)

    return 0 if count == -1 else count


print(binary_count_rotations_prob(nums, 3))
