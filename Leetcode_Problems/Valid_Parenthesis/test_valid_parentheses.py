import unittest
import valid_parentheses

class TestValidParentheses(unittest.TestCase):
    def test_is_valid(self):
        self.assertEqual(valid_parentheses.is_valid("()"), True)
        self.assertEqual(valid_parentheses.is_valid("()[]{}"), True)
        self.assertEqual(valid_parentheses.is_valid("(]"), False)
        self.assertEqual(valid_parentheses.is_valid("([)]"), False)
        self.assertEqual(valid_parentheses.is_valid("{[]}"), True)
        self.assertEqual(valid_parentheses.is_valid(""), True)  # Edge case: empty string
        self.assertEqual(valid_parentheses.is_valid("((((()))))"), True)  # Nested parentheses
        self.assertEqual(valid_parentheses.is_valid("((((()))))}"), False)  # Extra closing bracket

if __name__ == "__main__":
    unittest.main()
