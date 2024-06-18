"""
Problem Statement
We are given an unsorted array containing 'n' numbers taken from the range 1 to 'n'.
The array has some duplicates, find all the duplicate numbers without using any extra space.

Example 1:
Input: [3, 4, 4, 5, 5]
Output: [4, 5]

Example 2:
Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
"""


def find_all_duplicates(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    # iterate through the array and find all numbers not equal to their index + 1
    duplicate_numbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicate_numbers.append(nums[i])

    return duplicate_numbers


def main():
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


if __name__ == "__main__":
    main()

"""
Time complexity
The time complexity of the above algorithm is O(n).

Space complexity
Ignoring the space required for storing the duplicates, the algorithm runs in constant space O(1).
"""