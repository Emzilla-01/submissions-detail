"""Runtime: 39 ms, faster than 75.66% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14 MB, less than 24.32% of Python3 online submissions for Valid Parentheses."""
def close2open(c):
    d = {'}':'{',
         ']':'[',
         ')':'('
        }
    return(d.get(c))

class Solution:    
    def isValid(self, s: str) -> bool:
        last_opened=list()
        for c in s:
            if c in '([{':
                last_opened.append(c)
            elif c in ')]}':
                try:
                    if close2open(c) == last_opened[-1]:
                        del last_opened[-1]
                    else:
                        return(False)
                except IndexError as e:
                    return(False)
        if last_opened == list():
            return(True)
        return(False)