"""
Problem Statement
We are given an array containing 'n' distinct numbers taken from the range 0 to 'n'.
Since the array has only 'n' numbers out of the total 'n+1' numbers, find the missing number.

Example 1:
Input: [4, 0, 3, 1]
Output: 2

Example 2:
Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
"""


def find_missing_number(nums):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i]

        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    # the array is sorted, find the first number missing from its index
    for i in range(n):
        if nums[i] != i:
            return i

    return n


def main():
    print(find_missing_number([4, 0, 3, 1]))  # 2
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))  # 7


if __name__ == "__main__":
    main()

"""
Time complexity
The time complexity of the above algorithm is O(n).
In the while loop, although we are not incrementing the index i when swapping the numbers,
this will result in more than 'n' iterations of the loop,
but in the worst-case scenario, the while loop will swap a total of 'n-1' numbers,

Once a number is at its correct index, we will move on to the next number by incrementing i.
In the end, we iterate the input array again to find the first number missing from its index,
so overall, our algorithm will take O(n) + O(n-1) + O(n)  which is asymptotically equivalent to O(n).

Space complexity
The algorithm runs in constant space O(1).
"""
