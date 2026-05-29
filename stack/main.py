from collections import deque

class Solution:
    def valid_parentheses(self, s: str) -> bool:
        d = deque()
        mapeamento = {")": "(", "}": "{", "]": "["}

        for p in s:
            if p in mapeamento.values():
                d.append(p)

            elif p in mapeamento:
                if not d or d.pop() != mapeamento[p]:
                    return False

        return not d

print(Solution().valid_parentheses("({}[])"))