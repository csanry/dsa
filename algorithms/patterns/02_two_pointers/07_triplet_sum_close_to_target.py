"""
Problem Statement
Given an array of unsorted numbers and a target number,
find a triplet in the array whose sum is as close to the target number possible.
Return the sum of the triplet.
If more than one such triplet exists, return the sum of the triplet with the smallest sum.

Example 1:
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Example 2:
Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Example 3:
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
"""

import math


def triplet_sum_close_to_target(arr, target_sum):

    # keep track of the smallest difference
    arr.sort()
    smallest_difference = math.inf

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            target_diff = target_sum - (arr[i] + arr[left] + arr[right])

            if target_diff == 0:  # we found an exact match
                return target_sum

            # handle multiple solutions where the difference from target is the same
            # return the smallest sum
            if abs(target_diff) < abs(smallest_difference) or (
                abs(target_diff) == abs(smallest_difference)
                # eg. difference of 1 vs -1: we should take the positive number
                and target_diff > smallest_difference
            ):
                smallest_difference = target_diff

            # shift pointers
            if target_diff > 0:
                left += 1  # we need a triplet with a larger sum
            else:
                right -= 1  # we need a triplet with a smaller sum

    return target_sum - smallest_difference


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))  # 1
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))  # 0
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))  # 3


if __name__ == "__main__":
    main()


"""
Time complexity
Sorting the array will take O(N * logN).
The section to search for a triplet will take O(N^2).
Overall the function will take O(N * logN + N^2),
which is asymptotically equivalent to O(N^2).

Space complexity
The space complexity of the above algorithm will be O(N) which is required for sorting.
"""
