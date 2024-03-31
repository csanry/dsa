"""
Problem Challenge 1

Permutation in a String (hard)
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba

If a string has ‘n’ distinct characters it will have n! permutations.

Example 1:
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Example 4:
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""


# implementation
def find_permutation(st, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # our goal is to match all the characters from the char_frequency to the
    # current window - try to extend the range [window_start, window_end]
    for window_end in range(len(st)):
        right_char = st[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

        # if window gets longer than pattern, shrink the window
        if window_end >= len(pattern) - 1:
            left_char = st[window_start]
            window_start += 1
            # increase back the characters to match
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    return False


def main():
    print("Permutation exist: " + str(find_permutation("oidbcaf", "abc")))  # True
    print("Permutation exist: " + str(find_permutation("odicf", "dc")))  # False
    print(
        "Permutation exist: " + str(find_permutation("bcdxabcdy", "bcdyabcdx"))
    )  # True
    print("Permutation exist: " + str(find_permutation("aaacb", "abc")))  # True


main()

"""
Time Complexity
The time complexity of the above algorithm will be O(N + M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

Space Complexity
The space complexity of the algorithm is O(M) since in the worst case,
the whole pattern can have distinct characters which will go into the HashMap.
"""
