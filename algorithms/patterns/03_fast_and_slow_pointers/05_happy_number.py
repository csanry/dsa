"""
Problem Statement
A number is a happy number if,
after repeatedly replacing it with a number equal to the sum of the square of all of its digits,
leads us to number `1`.

All other numbers (not happy) will never reach `1`.
Instead, they will be stuck in a cycle of numbers which does not include `1`.

Determine if a numbers is happy or not.
"""


def find_happy_number(num):
    # create slow and fast pointers
    slow, fast = num, num

    while True:
        fast = square(square(fast))
        slow = square(slow)

        # cycle found
        if fast == slow:
            break

    # not happy numbers never have `1`` in their cycles
    return slow == 1


def square(num):
    square_num = 0

    while num > 0:
        square_num += (num % 10) ** 2
        num //= 10

    return square_num


def main():
    print(find_happy_number(23))  # True
    print(find_happy_number(12))  # False


if __name__ == "__main__":
    main()


"""
Time Complexity
Running through sequence examples, the algorithm has a time complexity of O(log N).

Space Complexity
The algorithm runs in constant space O(1).
"""
