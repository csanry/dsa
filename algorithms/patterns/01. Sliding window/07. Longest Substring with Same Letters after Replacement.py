"""
Problem Statement
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1: Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Example 2:
Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Example 3:
Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""


# implementation
def length_of_longest_substring(st, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    # try to extend the range [window_start, window_end]
    for window_end in range(len(st)):
        right_char = st[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        max_repeat_letter_count = max(
            max_repeat_letter_count, frequency_map[right_char]
        )

        # current window is from window_start to window_end, overall we have a letter which is
        # repeating max_repeat_letter_count times, this means we should replace the remaining letters
        # in the window. If the remaining letters are more than k, we need to shrink the window as
        # we are not allowed to replace more than k times
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = st[window_start]
            frequency_map[left_char] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(length_of_longest_substring("aabccbb", 2))  # 5
    print(length_of_longest_substring("abbcb", 1))  # 4
    print(length_of_longest_substring("abccde", 1))  # 3


main()

"""
Time Complexity
The time complexity of the above algorithm will be O(N) where ‘N’ is the number of letters in the input string.

Space Complexity
As we are expecting only the lower case letters in the input string, we can conclude that the space complexity will be O(26), to store each letter’s frequency in the HashMap, which is asymptotically equal to O(1).
"""
