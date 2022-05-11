class Solution:
    def isValid(self, s: str) -> bool:

        # Saved a couple of syntaxes
        dict_ = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        # Keep contrary syntaxes
        stack = []
        
        for i in s:
            # len(s) > 1 is created to rid celibate case for up speed to investigating
            if len(s) > 1 and i in dict_:
                stack.append(dict_[i])
            # len(stack) == 0 is created in celibate case 
            # stack.pop() that have to test pairing syntax if the syntax matches that means matching correct 
            elif len(stack) == 0 or stack.pop() != i:
                return False
        # prevention in lonely syntax case
        return len(stack) == 0

print(Solution().isValid("(("))