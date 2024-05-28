"""
Problem Statement
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages,
have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result.

It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. Solution must be O(1) space complexity.

Example 1:
Input: nums = [3, 2, 3, 6, 3, 10, 9, 3], val = 3
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 6, 10, 9].

Example 2:
Input: [2, 11, 2, 2, 1]
Output: 2
Explanation: The first two elements after removing the duplicates will be [11, 1].
"""


# implementation
def remove_element(nums, val):
    # index to track the next position to swap the value that is not key in
    left = 0

    # traverse the array, if the array is the key value, skip the replacement step,
    # else replace the val of the element at the left pointer
    for right in range(len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1

    return left


def main():
    print(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3))  # 4
    print(remove_element([2, 11, 2, 2, 1], 2))  # 2


if __name__ == "__main__":
    main()


"""
Time Complexity
The time complexity of the above algorithm will be O(N), where 'N' is the total number of elements in the given array.
We have to traverse the entire array to check the values.

Space Complexity
The algorithm runs in constant space O(1). The replacement is done in-place.
"""
