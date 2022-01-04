'''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

# implementation
def max_sub_array_of_size_k(k, arr):
    # instantiate the max sum (result), current window sum, and start index
    max_sum, window_sum = 0, 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end] # add the next element with idx at window
        # slide the window if we've exceeded the window size limit
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start] # subtract the element going out
            window_start += 1 # slide the window ahead
    return max_sum

def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))) # 9
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))) # 7

main()

'''
Time Complexity 
The time complexity of the above algorithm will be O(N).

Space Complexity 
The algorithm runs in constant space O(1).
'''