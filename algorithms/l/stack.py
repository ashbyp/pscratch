
class Solution:

    def isValid(self, s: str) -> bool:
        '''
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        '''
        tally = []
        for x in s:
            if x in ('(', '{', '['):
                tally.append(x)
            else:
                if not tally:
                    return False
                t = tally.pop()
                if x == ')' and t != '(' or x == '}' and t != '{' or x == ']' and t != '[':
                    return False
        return len(tally) == 0



def main() -> None:
    s = Solution()
    print(s.isValid('()'))
    print(s.isValid('()[]{}'))
    print(s.isValid('(]'))
    print(s.isValid("[(({})}]"))


if __name__ == '__main__':
    main()