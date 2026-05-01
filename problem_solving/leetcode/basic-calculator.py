"""Link: """

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
            



