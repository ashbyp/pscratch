from typing import List
from utils.measure import checker


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapping_s_t = {}
        mapping_t_s = {}

        for c1, c2 in zip(s, t):

            # Case 1: No mapping exists in either of the dictionaries
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1

            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False

        return True


if __name__ == '__main__':
    with checker(Solution().isIsomorphic, repeat=0, check_success=True) as c:
        c.check_2('egg', 'add', True)
        c.check_2('foo', 'bar', False)
        c.check_2('paper', 'title', True)
        c.check_2("badc", "baba", False)
