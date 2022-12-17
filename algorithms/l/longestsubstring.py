# Given a string s, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring_first(self, s: str) -> int:
        l = len(s)
        m = 0
        p = 0

        while p < l:
            seq = set()
            q = p
            while q < l and s[q] not in seq:
                seq.add(s[q])
                q += 1
            m = max(m, len(seq))
            p += 1

        return m

    def lengthOfLongestSubstring_second(self, s: str) -> int:
        l = len(s)
        m = 0
        p = 0

        while p < l:
            pos = {}
            while p < l:
                if s[p] not in pos:
                    pos[s[p]] = p
                    p += 1
                else:
                    p = pos[s[p]] + 1
                    break

            m = max(m, len(pos))

        return m

    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s: return 0
        start = 0
        end = 0
        m = 0
        seq = set()

        while end < len(s):
            if s[end] not in seq:
                print(f'add: {s[end]}')
                seq.add(s[end])
                end += 1
                m = max(m, len(seq))
            else:
                print(f'  rem: {s[start]}')
                seq.remove(s[start])
                start += 1
        return m

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcbcbb'))  # abc  3
    print(Solution().lengthOfLongestSubstring('bbbbb'))     # b    1
    print(Solution().lengthOfLongestSubstring('pwwkew'))    # wke  3
    print(Solution().lengthOfLongestSubstring('@'))  # wke  3
    print(Solution().lengthOfLongestSubstring('dvdf'))  # vdf  3
    print(Solution().lengthOfLongestSubstring_first("qrsvbspk"))
    print(Solution().lengthOfLongestSubstring("qrsvbspk"))

