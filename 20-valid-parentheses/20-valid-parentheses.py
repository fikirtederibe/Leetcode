class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {")": "(",
                    "]": "[",
                    "}": "{"}
        stack = []
        for bracket in s:
            if bracket not in hash_map or stack == []:
                stack.append(bracket)
            else:
                if stack[-1] == hash_map[bracket]:
                    stack.pop()
                else:
                    stack.append(bracket)
        return not stack