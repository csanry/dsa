"""
Problem Statement
Given an array of characters where each character represents a fruit tree:
Your goal is to put the maximum number of fruits into two baskets.
The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you can't skip a tree.
You will pick one fruit from each tree until you cannot (stop when you have to pick a third fruit type).
Write a function to return the maximum number of fruits in both the baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""

# implementation with defaultdict to eliminate checking for 0s
from collections import defaultdict


def fruits_into_baskets(fruits):
    window_start, max_fruits = 0, 0
    fruit_dict = defaultdict(int)

    # using enumeration to count the index of each fruit tree
    # try to extend the range of [window_start, window_end]
    for window_end, fruit in enumerate(fruits):
        fruit_dict[fruit] += 1

        # if the number of fruits exceeds 2, shrink the window until the max distinct fruits == 2
        while len(fruit_dict) > 2:
            fruit_dict[fruits[window_start]] -= 1
            if fruit_dict[fruits[window_start]] == 0:
                del fruit_dict[fruits[window_start]]
            window_start += 1

        # record current max total
        max_fruits = max(max_fruits, window_end - window_start + 1)
    return max_fruits


def main():
    print(
        "Maximum number of fruits: "
        + str(fruits_into_baskets(["A", "B", "C", "A", "C"]))
    )  # 3
    print(
        "Maximum number of fruits: "
        + str(fruits_into_baskets(["A", "B", "C", "B", "B", "C"]))
    )  # 5


if __name__ == "__main__":
    main()


"""
Time Complexity
The time complexity of the above algorithm will be O(N) where 'N' is the number of characters in the input array.
The outer for loop runs for all characters and the inner while loop processes each character only once,
therefore the time complexity of the algorithm will be O(N+N), which is asymptotically equivalent to O(N).

Space Complexity
O(1) as there can be a maximum of three types of fruits stored in the frequency map.

Similar Problems
Problem 1: Longest Substring with at most 2 distinct characters
Given a string, find the length of the longest substring in it with at most two distinct characters.
Solution: This problem is exactly similar to our parent problem.
"""
