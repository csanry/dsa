"""
Problem Statement
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Example 2:
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""


# implementation
def pair_with_target_sum(arr, target_sum):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]

        if target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum
    return [-1, -1]


def main():
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum([2, 5, 9, 11], 11))


main()

"""
Time Complexity
The time complexity of the above algorithm will be O(N), where 'N' is the total number of elements in the given array.

Space Complexity
The algorithm runs in constant space O(1).

An alternate approach
Instead of using a two-pointer or a binary search approach, we can utilize a Hashtable to search for the required pair.
We can iterate through the array one number at a time.

For our number X, we need to find Y such that X + Y == Target:
1. Search for Y (which is equivalent to Target - X") in the HashTable.
2. If Y is present in the Hashtable: pair found
3. If Y is not present, insert X into the Hashtable, we can search it for the later numbers.
"""


def pair_with_target_sum_hash(arr, target_sum):
    nums = {}  # hashtable to store numbers and their indices
    for i, x in enumerate(arr):
        if target_sum - x in nums:
            return [nums[target_sum - x], i]
        else:
            nums[arr[i]] = i
    return [-1, -1]


def main():
    print(pair_with_target_sum_hash([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum_hash([2, 5, 9, 11], 11))


main()

"""
Time Complexity
The time complexity of the above algorithm will be O(N), where 'N' is the total number of elements in the given array.

Space Complexity
The space complexity will also be O(N), as, in the worst case, we will be pushing 'N' numbers into the Hashtable.
"""
