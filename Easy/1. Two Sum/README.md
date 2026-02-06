# Two Sum

## Overview
- **Difficulty**: Easy
- **Topics**: Array, Hash Table
- **LeetCode Link**: https://leetcode.com/problems/two-sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to the target. Each input has exactly one solution, and you may not use the same element twice. The answer can be returned in any order.

## Prerequisites
- Hash Table fundamentals (insertion and constant-time lookup)
- Complement calculation (target minus current element)
- Array traversal with index tracking using enumeration

## Approach
This solution uses a **Hash Map (One-Pass)** technique. Instead of checking every pair of numbers with a brute-force nested loop, we use a hash map to store each number we have seen along with its index. For each element, we calculate the complement (target minus the current number) and check whether that complement already exists in our hash map.

By doing this in a single pass through the array, we turn what would be an O(n^2) brute-force search into an O(n) solution. The hash map provides constant-time lookups, so checking whether the complement exists is an O(1) operation at each step.

This approach works because if two numbers `a` and `b` sum to the target, then when we encounter `b`, we will have already stored `a` in the map (or vice versa). The one-pass method is both time-efficient and straightforward to implement.

## Visual Example
```
Input: nums = [2, 7, 11, 15], target = 9

Step 1: i=0, num=2
        complement = 9 - 2 = 7
        numMap = {}
        7 not in numMap --> skip
        Add 2 to numMap
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
We traverse the array once, performing a single pass through all `n` elements. Each hash map lookup and insertion takes O(1) on average, so the total time complexity is O(n).

### Space Complexity: O(n)
In the worst case, we store all `n` elements in the hash map before finding the answer. This happens when the two matching elements are at the very end of the array, resulting in O(n) additional space.

## Step-by-Step Code Walkthrough

**1. Initialize the hash map:**
```python
numMap = {}
```
Create an empty dictionary to store each number and its index as we iterate.

**2. Iterate through the array with index tracking:**
```python
for i, num in enumerate(nums):
```
Use `enumerate` to get both the index `i` and the value `num` at each position.

**3. Calculate the complement:**
```python
diff = target - num
```
Determine what value we need to find in order to reach the target sum.

**4. Check if the complement exists in the map:**
```python
if diff in numMap:
    return [numMap[diff], i]
```
If the complement has been seen before, return its stored index along with the current index. This gives us the two indices whose values sum to the target.

**5. Store the current number and index:**
```python
numMap[num] = i
```
If no match was found, record the current number and its index for future lookups.

## Key Insights
- The complement approach converts a two-variable search problem into a single-variable lookup problem
- Storing values as keys and indices as values in the hash map allows O(1) lookups while preserving position information
- Processing elements left to right guarantees we never use the same element twice, since we only check against previously seen elements
- A single pass is sufficient because when we reach the second number of the pair, the first number is already in the map

## Common Pitfalls
- Using the same element twice (e.g., if target is 4 and nums contains a single 2, returning its index twice)
- Storing the current number in the map before checking for the complement, which can lead to using the same element twice
- Returning the values instead of the indices
- Assuming the array is sorted (it is not guaranteed to be sorted)