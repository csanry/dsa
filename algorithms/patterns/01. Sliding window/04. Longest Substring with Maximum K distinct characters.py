"""
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""


# implementation
def longest_substring_with_k_distinct(st, k):
    window_start, max_length = 0, 0
    char_frequency = {}

    # in the following loop we'll try to extend the range of [window_start, window_end]
    for window_end in range(len(st)):
        right_char = st[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # shrink the sliding window, until we have 'k' distinct characters in the char_frequency map
        while len(char_frequency) > k:
            left_char = st[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1  # shrink the start window

        # record the current max length
        max_length = max(max_length, window_end - window_start + 1)
    # finish loop for each letter to get final result
    return max_length


def main():
    print(
        "Length of the longest substring: "
        + str(longest_substring_with_k_distinct("araaci", 2))
    )  # 4
    print(
        "Length of the longest substring: "
        + str(longest_substring_with_k_distinct("araaci", 1))
    )  # 2
    print(
        "Length of the longest substring: "
        + str(longest_substring_with_k_distinct("cbbebi", 3))
    )  # 5


main()

"""
Time Complexity
The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input string.
The outer for loop runs for all characters and the inner while loop ultimately processes each character only once, therefore the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N).

Space Complexity
The space complexity of the algorithm is O(K), as we will be storing a maximum of ‘K+1’ characters in the HashMap.
"""
