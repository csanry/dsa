# Sliding Window

- The Sliding Window pattern is used to perform a required operation on a specific window size of a linear data structure

- One common problem would be to find the longest subarray containing all 1s

- Sliding windows start from the 1st element and keep shifting right by one element, adjusting the length of the window according to the problem

- In some cases, the window size remains constant, and in other cases, the window size grows or shrinks

## Ways to identify

1. Problem input is a linear data structure.
   - Linked list, array or string.

2. Asked to find the longest / shortest substring, subarray, or desired value.

## Problems

### [Maximum Sum Subarray of Size K](./02.%20Maximum%20Sum%20Subarray%20of%20Size%20K.py)

> Given an array of positive numbers and a positive number `k`, find the maximum sum of any contiguous subarray of size `k`

#### Brute force

- A basic brute force solution would be to calculate the sum of all `k` sized subarrays of the given array to find the subarray with the highest sum

- We can start from every index of the given array and add the next `k` elements to find the subarray's sum

```python
def max_sub_array_of_size_k(arr, k):
    max_sum = 0
    size = len(arr) - k + 1

    for i in range(size):
        window_sum = 0

        for v in range(i, i + k):
            window_sum += arr[v]

        max_sum = max(window_sum, max_sum)

    return max_sum
```

- Time complexity of the solution above is $O(n*k)$, where `n` is the total number of elements in the array and `k` is the size of the subarray

#### Sliding window

- We can utilize the sum of the previous subarray to calculate the next subarray

- To do so, consider each subarray as a sliding window of size `k`

- To calculate the sum of the next subarray, we need to slide the window ahead by one element

- So to slide the window forward and calculate the sum of the new position of the sliding window, we need to do two things:

    1. Subtract the element going out of the sliding window (the first element)

    2. Add the new element coming in

This approach saves us from recalculating the overlapping part of the sliding
window

```python
def max_subarray_of_size_k(k, arr):
    max_sum, window_sum = 0, 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum
```

- Time complexity of the above algorithm will be $O(n)$

- Space complexity of the above algorithm will be $O(1)$

### [Smallest Subarray with a given sum](./03.%20Smallest%20Subarray%20with%20a%20given%20sum.py)

> Given an array of positive numbers and a positive number 'S', find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'.
> Return 0 if no such subarray exists.

- We can use a similar strategy used in **Maximum Sum Subarray of Size K**

- The main difference is that the sliding window size is not fixed in this problem

- Here is one approach for this problem

    1. Add up elements from the beginning of the array until their sum becomes greater than or equal to `S`

    2. These elements will constitute our sliding window. Remember the current length of our window as the smallest window so far

    3. After this, keep adding one element in the sliding window in a stepwise fashion

    4. In each step, we will also try to shrink the window from the beginning. To find the smallest window, we will shrink the window until the window's sum is smaller than `S` again

    5. This shrinking will also happen in multiple steps; in each step, we will do two things:

        - Check if the current window length is the smallest so far, and if so, remember its length

        - Subtract the first element of the window from the running sum to shrink the sliding window

```python
def smallest_subarray_with_given_sum(s, arr):
    window_sum, window_start = 0, 0
    min_length = math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    return min_length if min_length != math.inf else 0
```

- The time complexity of the above algorithm is $O(n)$

- The outer for loop runs for all elements, and the inner while loop processes each element only once

- Therefore the algorithm requires 2n operations

- The algorithm runs in constant space $O(1)$

### [Longest Substring with Maximum K distinct characters](./04.%20Longest%20Substring%20with%20Maximum%20K%20distinct%20characters.py)

> Given a string, find the length of the **longest substring** in it with no
> more than K distinct characters.
>
> You can assume that K is less than or equal to the length of the given string.

- We can use a similar dynamic sliding window strategy as **Smallest Subarray with a given sum**

- We will use a hashmap to remember the frequency of each processed character

1. Insert characters into the hashmap from the beginning of the string until we have `K` distinct characters

2. These characters form our sliding window - remember the current length as the longest window so far

3. Next, try to grow the window by adding one character in the sliding window in a stepwise fashion

4. At each step, we will try to shrink the window from the beginning if the count of distinct characters in the hashmap is larger than `K`. We will shrink the window until we have $\le$ `K` distinct characters

5. The shrink step involves:

    - Recording the current window length if it is the longest so far

    - Removing the character frequency from the hashmap

### [Fruits into baskets](./05.%20Fruits%20into%20baskets.py)

> Given an array of characters where each characters represents a fruit tree, you are given **two baskets**, and your goal is to put the **maxiumum number of fruits in each basket**. The only restriction is that each basket can have only one type of fruit.
>
> You can start with any tree, but you can't skip a tree once you have started. You will pick one fruit from each tree until you cannot (ie. stop when you have to pick from a third fruit type).
>
> Write a function to return the maximum number of fruits in both baskets.

- This problem is similar to **Longest Substring with K Distinct Characters**

- In this problem, we need to find the length of the longest subarray with no more
than two distinct characters (fruit types)

- This can be conceptualized as a **Longest Substring with K Distinct Characters**
where `k=2`

```python
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
```

- The above algorithm's time complexity will be $O(n)$, where $n$ is the number of characters in the input array

    - The outer `for loop` runs for all characters, and the inner `while loop` processes each character only once

    - Therefore the algorithm performs `2n` operations each pass, which is asymptotically equivalent to $O(n)$

- The algorithm runs in constant space $O(1)$ as there can be a maximum of three types of fruits stored in the frequency map.

### [No Repeat Substring](./06.%20No%20Repeat%20Substring.py)

> Given an array of positive numbers and a positive number `k`, find the maximum sum of any contiguous subarray of size `k`.

- We can use a similar dynamic window strategy as **Longest Substring with Maximum K distinct characters**

- A hashmap is used to remember the last index of each character processed

- When we get a repeating character, shrink the sliding window to ensure that we will always have distinct characters in the sliding window

- We do this by shifting the start of the window to index of the last occurrence of the repeat character, **if** this index is greater than `window_start`

- Otherwise maintain `window_start` and compute the maximum length

```python
def non_repeat_substring(st):
    max_length, window_start = 0, 0
    char_index_map = {}

    for window_end in range(len(st)):
        right_char = st[window_end]
        if right_char in char_index_map:
            window_start = max(window_start, char_index_map[right_char] + 1)
        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)

    return max_length
```

- The time complexity of the above algorithm will be $O(n)$ as we have to process each character in the string once

- The algorithm requires $O(k)$ space, where `k` is the number of distinct characters in the input string

    - However, since we expect `k` to be a fixed set of characters (26 in English), we can say that the algorithm runs in fixed space $O(1)$

### [Longest Substring with Same Letters after Replacement](./07.%20Longest%20Substring%20with%20Same%20Letters%20after%20Replacement.py)

> Given a string with lowercase letters only, if you are allowed to replace no more than `k` letters with any letter, find the length of the longest substring having the same letters after replacement.

- We can use a similar dynamic sliding window strategy as **No Repeat Substring**

- For performance, a hashmap can be used to store the frequency of each letter

1. Iterate through the string, adding one letter at a time to the window

2. Keep track of the count of the maximum repeating letter in any window

3. At any point in time, we will need to try and replace the remaining letters

    - If the remaining letters are $\le$ `k`, we can replace them all

    - If we have more than `k` remaining letters, we need to shrink the window

4. While shrinking the window, it is not necessary to update the maximum repeating letter, as this will be checked in the next iteration

```python
def length_of_longest_substring(st, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    for window_end in range(len(st)):
        right_char = st[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        max_repeat_letter_count = max(
            max_repeat_letter_count, frequency_map[right_char]
        )

        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = st[window_start]
            frequency_map[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length
```

- This algorithm runs in $O(n)$ time, since we iterate through every character of the string once

- This algorithm requires $O(26)$ space to store each of the 26 letters of the English language, which is asymptotically equal to $O(1)$

### [Longest Subarray with Ones after Replacement](./08.%20Longest%20Subarray%20with%20Ones%20after%20Replacement.py)

> Given an array containing 0s and 1s, if you are allowed to replace no more than `k` 0s with 1s, find the length of the longest contiguous subarray having all 1s.

- This problem is quite similar to the **Longest Substring with same Letters after Replacement** with two characters (0s and 1s) in the input arrays

- We can approach this problem similarly by adding one number at a time in the window and maintaining a record of the maximum number of repeating 1s

- When we have more than `k` remaining 0s, we should shrink the window

```python
def length_of_longest_substring(arr, k):
    window_start, max_length, max_ones_count = 0, 0, 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1

        if (window_end - window_start + 1 - max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length
```

- The time complexity of the above algorithm will be $O(n)$ where `n` is the length of the input array

- The algorithm runs in $O(1)$ time

### [Permutation in a String](./09.%20Permutation%20in%20a%20String.py)

> Given a string and a pattern, find out if the string contains any permutation of the pattern.

- If a string has `n` distinct characters, it will have `n!` permutations

- The goal of this problem is to find a subarray which contains all of the character frequencies of the pattern

- A hashmap can be used to store the character frequencies

1. Create a hashmap with the character frequencies of the pattern

2. Iterate through the string, adding characters to the sliding window

3. If the character being added matches a character in the pattern, decrement its frequency; when the character frequency reaches 0, we have a match

4. We get our permutation if the number of characters matched is equal to the number of distinct characters in the pattern

5. If the window size is greater than the length of the pattern, shrink the window to make it equal to the pattern's size

6. When shrinking the window, if the character going out was part of the pattern, put it back in the frequency hashmap

```python
def find_permutation(st, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    for window_end in range(len(st)):
        right_char = st[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

        if window_end >= len(pattern) - 1:
            left_char = st[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False
```

- The time complexity of the above algorithm is $O(n + m)$ where `n` is the length of the array and `m` is the length of the pattern

- The space complexity is $O(M)$, since in the worst case, the whole pattern can have distinct characters, which needs to be stored in the hashmap
