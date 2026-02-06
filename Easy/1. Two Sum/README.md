# Two Sum

## Overview
- **Difficulty**: Easy
- **Topics**: Array, Hash Table
- **LeetCode Link**: [Problem](https://leetcode.com/problems/two-sum/)

## Problem Statement
Given an array of integers and a target value, find the indices of two numbers that add up to the target. Each input has exactly one solution, and the same element cannot be used twice. The answer can be returned in any order.

## Prerequisites
- Hash Table fundamentals (insertion and O(1) average-case lookup)
- Complement technique: reframing "find two numbers that sum to target" as "for each number, check if target minus that number exists"
- Array traversal with index tracking using enumerate
- Understanding of trade-offs between brute-force O(n^2) and hash-map-based O(n) approaches

## Approach
This solution uses the **Hash Map (One-Pass)** technique. The core idea is to iterate through the array once, and for each element, compute its complement (target minus the current number). If the complement already exists in the hash map, we have found our pair and return their indices immediately. Otherwise, we store the current number and its index in the hash map for future lookups.

The one-pass approach works because by the time we reach the second number in any valid pair, the first number has already been stored in the hash map during an earlier iteration. This eliminates the need for a second loop or nested iteration entirely.

This strategy transforms the problem from a nested search into a single linear scan with constant-time lookups, making it both time-efficient and straightforward to implement.

## Visual Example
```
Input: nums = [2, 7, 11, 15], target = 9

Step 1: i=0, num=2
        complement = 9 - 2 = 7
        numMap = {}
        7 not in numMap --> store current number
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
We traverse the array exactly once, performing a single pass through all n elements. Each hash map lookup and insertion operation takes O(1) on average, so the total time is O(n).

### Space Complexity: O(n)
In the worst case, we store nearly all n elements in the hash map before finding the answer (e.g., the valid pair is at the very end of the array). Therefore, the space used by the hash map is O(n).

## Step-by-Step Code Walkthrough
1. **Initialize an empty hash map** (`numMap = {}`): This will store each number as a key and its index as the value, allowing O(1) lookups.

2. **Iterate through the array with index tracking** (`for i, num in enumerate(nums)`): Using `enumerate` gives us both the index `i` and the value `num` at each step.

3. **Compute the complement** (`diff = target - num`): For the current number, calculate what value is needed to reach the target sum.

4. **Check if the complement exists in the map** (`if diff in numMap`): If the complement was seen in a previous iteration, we have found the two indices that form the solution.

5. **Return the result** (`return [numMap[diff], i]`): Return the index of the complement (stored earlier) and the current index.

6. **Store the current number** (`numMap[num] = i`): If the complement was not found, add the current number and its index to the map for future lookups.

## Key Insights
- The complement technique converts a two-variable search problem into a single-variable lookup: instead of asking "do any two numbers sum to target?", we ask "have I already seen target minus this number?"
- Storing numbers as we go (one-pass) is sufficient because when we encounter the second number in a valid pair, the first number is guaranteed to already be in the map.
- The hash map provides O(1) average lookup, which is what brings the solution down from O(n^2) to O(n).
- The problem guarantees exactly one valid answer, so we can return immediately upon finding a match without worrying about duplicates or multiple solutions.

## Common Pitfalls
- **Using the same element twice**: If you check the map before confirming the indices are different, you might incorrectly match an element with itself (e.g., target=4 with nums=[2,3] checking index 0 against itself). The one-pass approach naturally avoids this since we only check against previously stored elements.
- **Inserting before checking**: If you add the current number to the map before checking for its complement, you risk matching the element with itself when the complement equals the current number (e.g., nums=[3,3], target=6). Always check first, then insert.
- **Assuming sorted input**: The array is not guaranteed to be sorted, so two-pointer approaches that require sorting would change the original indices and need extra bookkeeping.
- **Not considering negative numbers**: The input can include negative values (constraints allow -10^9 to 10^9), so the solution must not make assumptions about positive-only inputs.

---

I wasn't able to write the file due to permission restrictions. The content above follows the exact structure required by your project's `build_readme_content()` pattern. To save it, you can either:

1. Grant write permissions when prompted, and I'll retry
2. Copy the content above into `algo-atlas-vault/Easy/1. Two Sum/README.md` manually