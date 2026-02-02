# Two Sum

## Overview
- **Difficulty**: Easy
- **Topics**: Array, Hash Table
- **LeetCode Link**: https://leetcode.com/problems/two-sum/

## Problem Statement
Given an array of integers and a target value, find the indices of two numbers that add up to the target. Each input has exactly one valid solution, and the same element cannot be used twice.

## Prerequisites
- Hash Table fundamentals (insertion and O(1) lookup)
- Understanding of complement calculation (target - current = needed value)
- Array traversal with index tracking using enumerate
- Dictionary/map data structure usage in Python

## Approach
This solution uses a Hash Table approach with single-pass traversal. Instead of checking every pair of numbers (which would be O(n^2)), we use a dictionary to store numbers we have already seen along with their indices.

For each number in the array, we calculate its complement (target minus the current number). If the complement exists in our dictionary, we have found our answer. If not, we store the current number and its index in the dictionary for future lookups.

This approach works because if two numbers a and b sum to the target, when we encounter b, we will have already stored a in our dictionary (or vice versa). The hash table provides O(1) lookup time, making the overall solution linear.

## Visual Example
```
Input: nums = [2,7,11,15], target = 9

Step 1: i=0, num=2
        complement = 9 - 2 = 7
        seen = {}
        7 not in seen
        Add current number to seen
        seen = {2: 0}

Step 2: i=1, num=7
        complement = 9 - 7 = 2
        seen = {2: 0}
        2 IS in seen at index 0
        Found pair! Return [seen[2], 1] = [0, 1]

Output: [0, 1]
```

## Complexity Analysis

### Time Complexity: O(n)
We traverse the array exactly once, and each lookup and insertion in the hash table takes O(1) average time. Therefore, the total time complexity is O(n) where n is the length of the input array.

### Space Complexity: O(n)
In the worst case, we might need to store almost all n elements in the hash table before finding the solution. This happens when the two numbers that sum to target are at the end of the array.

## Step-by-Step Code Walkthrough

**Initialize the hash table:**
```python
seen = {}
```
Create an empty dictionary to store numbers we have encountered and their indices.

**Iterate through the array:**
```python
for i, n in enumerate(nums):
```
Use enumerate to get both the index and value at each position.

**Calculate and check complement:**
```python
complement = target - n
if complement in seen:
    return [seen[complement], i]
```
For each number, calculate what value we need to reach the target. If that value exists in our dictionary, return both indices.

**Store current number:**
```python
seen[n] = i
```
If no match found, store the current number and its index for future reference.

**Handle no solution case:**
```python
return []
```
Return empty list if no valid pair exists (though problem guarantees one exists).

## Key Insights
- The complement relationship is symmetric: if a + b = target, then both a and b are complements of each other
- Storing the index along with the value allows us to return positions, not just the values themselves
- We check for the complement before adding the current number to avoid using the same element twice
- Single-pass solution is possible because we only need to find one pair, and order of discovery does not matter

## Common Pitfalls
- Using the same element twice by checking after adding to the dictionary instead of before
- Returning values instead of indices
- Using a nested loop approach that results in O(n^2) time complexity
- Not handling duplicate values correctly (the hash table naturally handles this since we check before inserting)