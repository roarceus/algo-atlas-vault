# Two Sum

## Overview
- **Difficulty**: Easy
- **Topics**: Array, Hash Table
- **LeetCode Link**: https://leetcode.com/problems/two-sum/

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Each input has exactly one solution, and you may not use the same element twice. The answer can be returned in any order.

## Prerequisites
- Hash Table fundamentals (insertion and O(1) lookup)
- Complement technique (calculating the needed value as `target - current`)
- Array traversal with index tracking using enumeration

## Approach
This solution uses a **Hash Map (One-Pass)** approach. Instead of checking every pair of numbers with a brute-force nested loop, we use a hash map to store numbers we have already seen along with their indices. For each number in the array, we calculate its complement (the value needed to reach the target) and check if that complement already exists in the hash map.

By doing this in a single pass through the array, we reduce the time complexity from O(n^2) to O(n). The hash map provides O(1) average-time lookups, so each check is constant time. As soon as we find a complement that exists in the map, we immediately return both indices -- the stored index of the complement and the current index.

This approach trades space for time. We use extra memory to store the hash map, but we gain a significant speedup by avoiding redundant comparisons.

## Visual Example
```
Input: nums = [2, 7, 11, 15], target = 9

Step 1: i=0, num=2
        complement = 9 - 2 = 7
        numMap = {}
        7 not in numMap --> add 2 to numMap
        numMap = {2: 0}

Step 2: i=1, num=7
        complement = 9 - 7 = 2
        numMap = {2: 0}
        2 IS in numMap --> found pair!
        Return [numMap[2], 1] = [0, 1]

Output: [0, 1]
```

## Complexity Analysis

### Time Complexity: O(n)
We traverse the array exactly once, performing a constant-time hash map lookup and insertion at each step. In the worst case, we visit all `n` elements before finding the answer, giving us O(n) time.

### Space Complexity: O(n)
In the worst case, we store nearly all `n` elements in the hash map before finding the matching pair. Therefore, the additional space used is O(n).

## Step-by-Step Code Walkthrough

1. **Initialize the hash map**: `numMap = {}` creates an empty dictionary to store numbers as keys and their indices as values.

2. **Iterate through the array**: `for i, num in enumerate(nums)` loops through each element, giving us both the index `i` and the value `num`.

3. **Calculate the complement**: `diff = target - num` computes the value we need to find in order to reach the target sum.

4. **Check if complement exists**: `if diff in numMap` performs an O(1) lookup to see if we have already encountered the complement in a previous iteration.

5. **Return the result**: If the complement is found, `return [numMap[diff], i]` returns the index of the complement (stored earlier) and the current index.

6. **Store current number**: If no match is found yet, `numMap[num] = i` records the current number and its index for future lookups.

## Key Insights
- The complement approach (`target - num`) transforms a two-variable search into a single-variable lookup
- Using a hash map converts the problem from O(n^2) brute force to O(n) single pass
- We only need one pass because we check before inserting -- this naturally prevents using the same element twice
- The order of checking then inserting is critical: it ensures we never match an element with itself

## Common Pitfalls
- Using the same element twice (e.g., if target is 4 and nums contains a single 2, returning [0, 0] would be incorrect)
- Using a brute-force nested loop when the follow-up explicitly asks for better than O(n^2)
- Returning the values instead of the indices -- the problem asks for indices, not the numbers themselves
- Forgetting to handle the case where duplicate values exist in the array (e.g., nums = [3, 3], target = 6)