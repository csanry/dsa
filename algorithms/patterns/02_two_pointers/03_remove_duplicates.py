"""
Problem Statement
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space
After removing the duplicates in-place, return the new length of the array.

Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
"""


# implementation
def remove_duplicates(arr):
    # index to track the next non-duplicate element
    left = 1

    # index to traverse the array
    right = 1

    while right < len(arr):
        if arr[left - 1] != arr[right]:
            arr[left] = arr[right]
            left += 1
        right += 1

    return left


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


if __name__ == "__main__":
    main()


"""
Time Complexity
The time complexity of the above algorithm will be O(N), where 'N' is the total number of elements in the given array.
We have to traverse the entire array to check for duplicates.

Space Complexity
The algorithm runs in constant space O(1).
"""
