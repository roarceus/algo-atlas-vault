# Two Sum

## Overview
- **Difficulty**: Easy
- **Topics**: Array, Hash Table
- **LeetCode Link**: https://leetcode.com/problems/two-sum/

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Each input has exactly one solution, and you may not use the same element twice. The answer can be returned in any order.

## Prerequisites
- Hash Table fundamentals (insertion and constant-time lookup)
- Complement calculation (target minus current element)
- Array traversal with index tracking using enumeration
- Understanding of single-pass vs brute-force trade-offs

## Approach
This solution uses the **Hash Map (One-Pass)** technique. Instead of checking every pair of numbers with a nested loop (which would be O(n^2)), we use a hash map to store each number we have seen along with its index. For each element, we calculate the complement (target minus the current number) and check if that complement already exists in the hash map.

By doing this in a single pass through the array, we reduce the problem to a series of constant-time lookups. When we find that the complement exists in the hash map, we immediately return the stored index and the current index as our answer.

This approach works because the problem guarantees exactly one valid solution exists. We build up knowledge of previously seen numbers as we iterate, so by the time we reach the second number of the valid pair, the first number is already recorded in the hash map.

## Visual Example
```
Input: nums = [2, 7, 11, 15], target = 9

Step 1: i=0, num=2
        diff = 9 - 2 = 7
        numMap = {}
        7 not in numMap --> add 2 to numMap
        numMap = {2: 0}

Step 2: i=1, num=7
        diff = 9 - 7 = 2
        numMap = {2: 0}
        2 is in numMap! --> return [numMap[2], 1] = [0, 1]

Output: [0, 1]
```

## Complexity Analysis

### Time Complexity: O(n)
We traverse the array exactly once, performing a constant-time hash map lookup and insertion at each step. With `n` elements in the array, this results in O(n) time.

### Space Complexity: O(n)
In the worst case, we store almost every element in the hash map before finding the answer. This requires O(n) additional space for the hash map.

## Step-by-Step Code Walkthrough
1. **Initialize the hash map**: `numMap = {}` creates an empty dictionary to store numbers as keys and their indices as values.

2. **Iterate through the array**: `for i, num in enumerate(nums)` loops through each element with its index.

3. **Calculate the complement**: `diff = target - num` computes the value needed to form the target sum with the current number.

4. **Check for the complement**: `if diff in numMap` performs a constant-time lookup to see if the complement was encountered earlier.

5. **Return the result**: `return [numMap[diff], i]` returns the index of the complement (stored earlier) and the current index.

6. **Store the current number**: `numMap[num] = i` records the current number and its index for future complement checks.

## Key Insights
- The hash map transforms a nested search (O(n^2)) into a single-pass solution (O(n)) by trading space for time.
- We only need to look backward -- by the time we process the second number of a valid pair, the first is already stored.
- The complement calculation (`target - num`) is the core idea: instead of searching for a pair, we search for a specific value.
- The problem guarantees exactly one solution, so we can return immediately upon finding a match without worrying about duplicates or multiple answers.

## Common Pitfalls
- Using the same element twice (e.g., if `target = 4` and `nums = [2, 3]`, you cannot use index 0 twice). This solution avoids this naturally because we check the map before inserting the current element.
- Forgetting to store the index (not just the value) in the hash map, which would prevent returning the correct indices.
- Attempting a brute-force O(n^2) approach that may time out on large inputs when a linear solution exists.
- Assuming the array is sorted -- this problem does not guarantee sorted input, which rules out a simple two-pointer approach without sorting first.