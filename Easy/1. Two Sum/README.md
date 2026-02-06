# Two Sum

## Overview
- **Difficulty**: Easy
- **Topics**: Array, Hash Table
- **LeetCode Link**: https://leetcode.com/problems/two-sum

## Problem Statement
Given an array of integers and a target value, find two numbers in the array that add up to the target and return their indices. Each input has exactly one solution, and the same element cannot be used twice.

## Prerequisites
- Hash Table fundamentals (insertion, lookup in constant time)
- Understanding of the complement technique (target - current = needed value)
- Array traversal with index tracking using enumeration

## Approach
This solution uses a **Hash Map (One-Pass)** approach. Instead of checking every pair of numbers with a brute-force nested loop, we use a hash map to store numbers we have already seen along with their indices. For each number in the array, we calculate its complement (target minus the current number) and check if that complement already exists in our hash map.

By performing the lookup and insertion in a single pass through the array, we avoid the need for a second loop entirely. When we encounter a number whose complement is already stored in the map, we immediately return the indices of both numbers. This reduces the time complexity from O(n^2) to O(n) at the cost of O(n) extra space for the hash map.

## Visual Example
```
Input: nums = [2, 7, 11, 15], target = 9

Step 1: i=0, num=2
        complement = 9 - 2 = 7
        numMap = {}
        7 not in numMap --> add current num to map
        numMap = {2: 0}

Step 2: i=1, num=7
        complement = 9 - 7 = 2
        numMap = {2: 0}
        2 IS in numMap --> found a match!
        Return [numMap[2], 1] = [0, 1]

Output: [0, 1]
```

## Complexity Analysis

### Time Complexity: O(n)
We traverse the array once, performing a single pass through all n elements. Each hash map lookup and insertion operation takes O(1) on average, so the overall time complexity is O(n).

### Space Complexity: O(n)
In the worst case, we store almost all n elements in the hash map before finding the answer. This occurs when the matching pair is at the end of the array, requiring O(n) additional space.

## Step-by-Step Code Walkthrough

**1. Initialize the hash map:**
```python
numMap = {}
```
This dictionary will store each number as a key and its index as the value.

**2. Iterate through the array with index tracking:**
```python
for i, num in enumerate(nums):
```
We use `enumerate` to get both the index `i` and the value `num` at each position.

**3. Calculate the complement:**
```python
diff = target - num
```
For each number, we compute what value we need to find in order to reach the target.

**4. Check if the complement exists in the map:**
```python
if diff in numMap:
    return [numMap[diff], i]
```
If the complement has already been seen, we return the stored index of the complement and the current index.

**5. Store the current number in the map:**
```python
numMap[num] = i
```
If no match is found yet, we record the current number and its index for future lookups.

## Key Insights
- The hash map trades space for time, turning an O(n^2) brute-force search into an O(n) single-pass solution
- By storing numbers as we go, we only need one pass instead of two separate passes (one to build the map, one to query it)
- The complement relationship (target - num) transforms the problem from "find two numbers that sum to target" into "for each number, check if we have already seen its partner"
- Inserting after checking prevents using the same element twice, since the current element is not yet in the map when we do the lookup

## Common Pitfalls
- Using the same element twice (e.g., if target is 6 and the array contains a single 3, checking 3 against itself). The one-pass approach avoids this by inserting after checking.
- Returning values instead of indices. The problem asks for the positions in the array, not the numbers themselves.
- Assuming the array is sorted. The input is not guaranteed to be sorted, which rules out a simple two-pointer approach without sorting first (and sorting would lose the original indices).
- Handling duplicate values incorrectly. When the same number appears twice (e.g., [3, 3] with target 6), the hash map overwrites the first index, but the one-pass approach catches the match before the overwrite happens.