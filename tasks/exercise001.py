#! /usr/bin/python3.8
# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice.
# Your task will be to return the sum of the numbers that occur only once.
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15.
# More examples in the test cases below.

# Good luck!
from collections import Counter

def repeats(arr):
    if not all(isinstance(i, int) for i in arr):
        raise TypeError("Array of integers expected")

    counter = Counter(arr)
    occuring_once = [i for i in counter if counter[i] == 1]

    if (n := len(occuring_once)) != 2:
        print(f"2 unique values are expected in the array. {n if n > 0 else 'None'} found")
    return sum(occuring_once)
