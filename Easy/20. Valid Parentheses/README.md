# Valid Parentheses

## Overview
- **Difficulty**: Easy
- **Topics**: String, Stack
- **LeetCode Link**: https://leetcode.com/problems/valid-parentheses/

## Problem Statement
Given a string containing only parentheses characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. A valid string requires that every opening bracket is closed by the same type of bracket in the correct order, and every closing bracket has a corresponding opening bracket.

## Prerequisites
- Stack data structure (push, pop, isEmpty operations)
- Hash Map for bracket pair matching
- Understanding of LIFO (Last-In-First-Out) principle
- String iteration and character comparison

## Approach
This problem uses the **Stack** data structure to track opening brackets and validate matching closing brackets. The key insight is that the most recently opened bracket must be closed first, which perfectly aligns with the LIFO nature of stacks.

The algorithm iterates through each character in the string. When encountering an opening bracket, it pushes it onto the stack. When encountering a closing bracket, it checks if the stack is non-empty and if the top of the stack contains the matching opening bracket. If either condition fails, the string is invalid.

A hash map stores the relationship between closing and opening brackets for O(1) lookup. After processing all characters, the stack must be empty for the string to be valid (all opening brackets must have been matched and removed).

## Visual Example
```
Input: s = "([])"

Initial state:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

Step 1: char = '('
        '(' not in pairs (it's an opening bracket)
        Push '(' onto stack
        stack = ['(']

Step 2: char = '['
        '[' not in pairs (it's an opening bracket)
        Push '[' onto stack
        stack = ['(', '[']

Step 3: char = ']'
        ']' in pairs (it's a closing bracket)
        pairs[']'] = '['
        stack.pop() returns '[' which equals pairs[']']
        Match found!
        stack = ['(']

Step 4: char = ')'
        ')' in pairs (it's a closing bracket)
        pairs[')'] = '('
        stack.pop() returns '(' which equals pairs[')']
        Match found!
        stack = []

Final check: len(stack) == 0 --> True

Output: true
```

## Complexity Analysis

### Time Complexity: O(n)
We iterate through each character in the string exactly once, where n is the length of the string. Each stack operation (push and pop) takes O(1) time, and hash map lookups are also O(1).

### Space Complexity: O(n)
In the worst case, if the string contains only opening brackets (e.g., "((((("), we push all n characters onto the stack. The hash map uses constant space O(1) since it only stores 3 bracket pairs.

## Step-by-Step Code Walkthrough

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
```
Initialize an empty stack to store opening brackets.

```python
        pairs = {')': '(', ']': '[', '}': '{'}
```
Create a hash map that maps each closing bracket to its corresponding opening bracket for quick lookup.

```python
        for char in s:
            if char in pairs:
```
Iterate through each character. If the character is a closing bracket (exists as a key in pairs), we need to validate it.

```python
                if not stack or stack.pop() != pairs[char]:
                    return False
```
Two checks: (1) Stack must not be empty (there must be an opening bracket to match). (2) The popped element must match the expected opening bracket. If either fails, return False.

```python
            else:
                stack.append(char)
```
If the character is an opening bracket, push it onto the stack.

```python
        return len(stack) == 0
```
After processing all characters, the stack must be empty. Any remaining opening brackets mean they were never closed.

## Key Insights
- The LIFO property of stacks naturally handles the "correct order" requirement - the most recent opening bracket must be closed first
- Using a hash map with closing brackets as keys allows O(1) lookup to find the expected opening bracket
- The solution elegantly handles both matching validation and order validation simultaneously
- An empty stack at the end confirms all brackets were properly paired

## Common Pitfalls
- Forgetting to check if the stack is empty before popping (causes index error on strings like ")")
- Only checking if brackets match without verifying correct nesting order (would incorrectly accept "([)]")
- Returning True immediately after processing without checking if the stack is empty (would incorrectly accept "((")
- Using a simple counter instead of a stack (fails to validate bracket type matching)