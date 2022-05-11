class Solution:
    def isValid(self, s: str) -> bool:

        dict_ = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []
        
        for i in s:
            if len(s) > 1 and i in dict_:
                stack.append(dict_[i])
            elif len(stack) == 0 or stack.pop() != i:
                return False
        return len(stack) == 0
    
print(Solution().isValid("["))