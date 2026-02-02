# Two Sum

## Overview
- **Difficulty**: Easy
- **Topics**: Array, Hash Table
- **LeetCode Link**: https://leetcode.com/problems/two-sum/

## Problem Statement
Given an array of integers and a target sum, find two numbers in the array that add up to the target and return their indices. Each input has exactly one solution, and the same element cannot be used twice.

## Prerequisites
- Hash Table fundamentals (insertion and O(1) lookup)
- Understanding of complement calculation (target - current = needed value)
- Array traversal with index tracking using enumeration
- Single-pass algorithm design

## Approach
The solution uses a Hash Map approach to achieve O(n) time complexity. Instead of checking every pair of numbers (which would be O(n^2)), we use a hash table to store numbers we've already seen along with their indices.

For each number in the array, we calculate its complement (target - current number). If this complement exists in our hash table, we've found our two numbers. If not, we store the current number and its index in the hash table and continue.

This approach works because if two numbers a and b sum to the target, when we encounter the second number, the first will already be in our hash table. The hash table allows us to check for the complement's existence in O(1) time.

## Visual Example
```
Input: nums = [2,7,11,15], target = 9

Step 1: i=0, num=2
        complement = 9 - 2 = 7
        seen = {}
        7 not in seen, add 2 to seen
        seen = {2: 0}

Step 2: i=1, num=7
        complement = 9 - 7 = 2
        seen = {2: 0}
        2 is in seen at index 0
        Return [seen[2], 1] = [0, 1]

Output: [0, 1]
```

## Complexity Analysis

### Time Complexity: O(n)
We traverse the array exactly once, and each hash table lookup and insertion takes O(1) average time. Therefore, the total time complexity is O(n) where n is the length of the input array.

### Space Complexity: O(n)
In the worst case, we might need to store almost all elements in the hash table before finding the answer. This happens when the two target numbers are at the end of the array, requiring O(n) space.

## Step-by-Step Code Walkthrough
```python
seen = {}
```
Initialize an empty hash table to store numbers we've encountered and their indices.

```python
for i, n in enumerate(nums):
```
Iterate through the array with both index and value using enumerate.

```python
if target - n in seen:
    return [seen[target - n], i]
```
Calculate the complement (target - n). If it exists in our hash table, we found our pair. Return the stored index of the complement and the current index.

```python
seen[n] = i
```
If complement not found, store the current number as a key with its index as the value.

```python
return []
```
Return empty list if no solution found (though problem guarantees one exists).

## Key Insights
- Using a hash table converts an O(n^2) brute force into an O(n) solution
- We only need one pass through the array because when we find the second number, the first is already stored
- Storing the index as the value allows immediate retrieval without additional lookups
- The complement approach transforms "find two numbers that sum to target" into "find if complement exists"

## Common Pitfalls
- Using the same element twice (the hash table naturally prevents this since we check before adding)
- Returning the values instead of the indices
- Forgetting to handle duplicate values in the array (the solution handles this correctly)
- Overcomplicating with two passes when one pass suffices