"""
Problem Statement
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
Explanation: There are four unique triplets whose sum is equal to zero.

Example 2:
Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: After squaring, the array becomes [9, 1, 0, 1, 4].
After sorting, the array becomes [0, 1, 1, 4, 9].
"""


def search_triplets(arr):
    arr.sort()
    triplets = []

    for i in range(len(arr)):
        # skip same elements to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        # helper function to search for pair Y + Z == -X
        search_pair(arr, -arr[i], i + 1, triplets)

    return triplets


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1

    # search for candidate pairs
    while left < right:
        current_sum = arr[left] + arr[right]

        # pair found
        if current_sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            # continue to search for other candidates that meet target_sum
            left += 1
            right -= 1

            # skip the same elements to avoid duplicates
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif current_sum < target_sum:  # we need a larger sum
            left += 1
        else:  # we need a pair with a smaller sum
            right -= 1


def main():
    print(
        search_triplets([-3, 0, 1, 2, -1, 1, -2])
    )  # [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
    print(search_triplets([-5, 2, -1, -2, 3]))  # [[-5, 2, 3], [-2, -1, 3]]


if __name__ == "__main__":
    main()


"""
Time complexity
Sorting the array will take O(N * logN).
The search_pair() function will take O(N).
As we are calling search_pair() for every number in the input array,
this means that overall search_triplets() will take O(N * logN + N^2),
which is asymptotically equivalent to O(N^2).

Space complexity
Ignoring the space required for the output array,
the space complexity of the above algorithm will be O(N) which is required for sorting.
"""
