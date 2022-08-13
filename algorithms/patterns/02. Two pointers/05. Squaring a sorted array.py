"""
Problem Statement 
Given a sorted array, return an array of the squares of each number, sorted in non-decreasing order.

Example 1:
Input: [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
Explanation: After squaring, the array becomes [16, 1, 0, 9, 100].
After sorting, the array becomes [0, 1, 9, 16, 100].

Example 2:
Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]
Explanation: After squaring, the array becomes [9, 1, 0, 1, 4].
After sorting, the array becomes [0, 1, 1, 4, 9].
"""


def square_sorted_array(arr):

    l, r = 0, len(arr) - 1
    res = [0] * len(arr)

    current_idx = len(arr) - 1
    while l <= r:
        if arr[l] ** 2 > arr[r] ** 2:
            res[current_idx] = arr[l] ** 2
            l += 1
        else:
            res[current_idx] = arr[r] ** 2
            r -= 1
        current_idx -= 1
    return res


def main():
    print(square_sorted_array([-4, -1, 0, 3, 10]))
    print(square_sorted_array([-3, -1, 0, 1, 2]))


main()

"""
Time complexity 
The time complexity of the above algorithm will be O(n) as we are iterating through the input array only once.

Space complexity 
The space complexity of the above algorithm will also be O(n); this space will be used for the output array.
"""
