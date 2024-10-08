"""
Problem Statement
We are given an unsorted array containing numbers taken from the range 1 to 'n'.
The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Example 1:
Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

Example 2:
Input: [2, 4, 1, 2]
Output: 3

Example 3:
Input: [2, 3, 2, 1]
Output: 4
"""


def find_missing_numbers(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing_numbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing_numbers.append(i + 1)

    return missing_numbers


def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))


if __name__ == "__main__":
    main()

"""
Time complexity
The time complexity of the above algorithm is O(n).

Space complexity
Ignoring the space required for the output array, the algorithm runs in constant space O(1).
"""
