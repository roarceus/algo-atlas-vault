# Valid Parentheses

## Overview
- **Difficulty**: Easy
- **Topics**: String, Stack
- **LeetCode Link**: https://leetcode.com/problems/valid-parentheses/

## Problem Statement
Given a string containing only parentheses characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. A string is valid if every opening bracket has a matching closing bracket of the same type, and brackets are closed in the correct order (properly nested).

## Prerequisites
- Stack data structure (push, pop, peek operations)
- Hash Map for bracket pair mapping
- Understanding of LIFO (Last In, First Out) principle
- String iteration and character comparison

## Approach
This problem uses a **Stack-based matching** approach. The key insight is that valid parentheses follow a LIFO pattern - the most recently opened bracket must be the first one closed. This naturally maps to stack behavior.

The algorithm iterates through each character in the string. When we encounter an opening bracket, we push it onto the stack. When we encounter a closing bracket, we check if the stack's top element is the corresponding opening bracket. If it matches, we pop from the stack and continue; if not, the string is invalid.

At the end, if the stack is empty, all brackets were properly matched. If the stack still contains elements, there are unmatched opening brackets, making the string invalid.

## Visual Example
```
Input: s = "([])"

Initial State:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

Step 1: char = '('
        '(' is NOT in pairs (it's an opening bracket)
        Push '(' onto stack
        stack = ['(']

Step 2: char = '['
        '[' is NOT in pairs (it's an opening bracket)
        Push '[' onto stack
        stack = ['(', '[']

Step 3: char = ']'
        ']' IS in pairs (it's a closing bracket)
        pairs[']'] = '['
        Pop from stack: '[' == '[' ? YES, match!
        stack = ['(']

Step 4: char = ')'
        ')' IS in pairs (it's a closing bracket)
        pairs[')'] = '('
        Pop from stack: '(' == '(' ? YES, match!
        stack = []

Final Check:
        len(stack) == 0 ? YES
        
Output: true
```

## Complexity Analysis

### Time Complexity: O(n)
We iterate through each character in the string exactly once, where n is the length of the string. Each stack operation (push and pop) takes O(1) time, so the overall time complexity is O(n).

### Space Complexity: O(n)
In the worst case, we might push all characters onto the stack. This happens when the string contains only opening brackets (e.g., "(((("). The hash map for pairs uses constant space O(1) since it always contains exactly 3 key-value pairs.

## Step-by-Step Code Walkthrough

```python
stack = []
pairs = {')': '(', ']': '[', '}': '{'}
```
Initialize an empty stack to track opening brackets. Create a dictionary mapping each closing bracket to its corresponding opening bracket.

```python
for char in s:
```
Iterate through each character in the input string.

```python
if char in pairs:
```
Check if the current character is a closing bracket by looking it up in the pairs dictionary.

```python
if not stack or stack.pop() != pairs[char]:
    return False
```
If it's a closing bracket, check two conditions: (1) the stack must not be empty, and (2) the popped element must match the expected opening bracket. If either fails, return False.

```python
else:
    stack.append(char)
```
If the character is an opening bracket, push it onto the stack.

```python
return len(stack) == 0
```
After processing all characters, return True only if the stack is empty (all brackets matched).

## Key Insights
- The stack naturally handles the nesting requirement because LIFO order ensures the most recent opening bracket is matched first
- Using a dictionary to map closing to opening brackets makes the matching check clean and O(1)
- Checking `not stack` handles the edge case of a closing bracket with no corresponding opener
- The final empty stack check catches unmatched opening brackets

## Common Pitfalls
- Forgetting to check if the stack is empty before popping (causes error on inputs like ")")
- Only checking if brackets match without verifying correct nesting order (would incorrectly accept "([)]")
- Returning True immediately after all characters match without checking for remaining items in the stack (would incorrectly accept "(((")
- Using a counter instead of a stack, which cannot detect wrong ordering like "([)]"