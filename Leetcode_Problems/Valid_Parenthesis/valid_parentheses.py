from typing import List

def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:  # If it's a closing bracket
            top_element = stack.pop() if stack else '#'  # Use a placeholder if stack is empty
            if mapping[char] != top_element:  # Check if the closing bracket matches
                return False
        else:  # It's an opening bracket
            stack.append(char)
    
    return not stack  # If stack is empty, all brackets were matched
