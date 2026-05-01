"""Link: https://leetcode.com/problems/basic-calculator/"""

# Working Code from GPT
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        result = 0
        sign = 1  # 1 represents '+', -1 represents '-'

        for char in s:
            if char.isdigit():
                # Handle multi-digit numbers (e.g., '12' -> 1*10 + 2)
                current_num = (current_num * 10) + int(char)
            
            elif char in ["+", "-"]:
                # Add the previous number to result
                result += sign * current_num
                # Update sign and reset current_num
                sign = 1 if char == "+" else -1
                current_num = 0
                
            elif char == "(":
                # Push the result and sign onto stack for later
                stack.append(result)
                stack.append(sign)
                # Reset for the new sub-expression
                result = 0
                sign = 1
                
            elif char == ")":
                # Finish the current sub-expression
                result += sign * current_num
                # Multiply by the sign before the parenthesis
                result *= stack.pop()
                # Add the result to the previous total
                result += stack.pop()
                current_num = 0
                
        # Final add for the last number
        return result + (sign * current_num)

# Attempt 1: (It didn't work obviously)
class Solution:
    def calculate(self, s: str) -> int:
        def check_string_int(s):
            try:
                int(s)
                return True
            except ValueError:
                return False

        def show_stack(st):
            st = [str(i) for i in st]
            print(" ".join(st))


        # Start a stack with first element
        stack = []

        # loop through each characters
        for i in range(len(s)):
            # Skip appending to stack if is space
            if s[i] == " ":
                continue
            
            if s[i] in ["(",")"]:
                continue

            # if it already contains 2 elements, then add them up
            if len(stack) >= 2 and stack[-1] in ("+", "-"):
                el1, el2 = stack[-1], stack[-2]
                # print("el1, el2", el1, el2)
                if el1 in ("+", "-") and check_string_int(el2) and check_string_int(s[i]):
                    el1, el2 = stack.pop(), stack.pop()
                    if el1 == "+":
                        new_num = int(el2) + int(s[i])
                    else:
                        new_num = int(el2) - int(s[i])
                elif el1 in ("+", "-") and s[i] in ("+", "-"):
                    el1 = stack.pop()
                    if el1 == s[i]:
                        new_num = "+"
                    else:
                        new_num = "-"
                else:
                    new_num = s[i]
            else:
                new_num = s[i]
                
            stack.append(new_num)

            # Debugging section
            # show_stack(stack)

        st = [str(i) for i in stack]
        st = "".join(st)
        return int(st) if check_string_int(st) else int(stack[-1])
            



