from collections import defaultdict

from utils.measure import timefunc
from typing import List


class Solution:
    @timefunc('first', 100_000)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tally = dict()
        for s in strs:
            ss = str(sorted(s))
            if ss not in tally:
                tally[ss] = [s]
            else:
                tally[ss].append(s)
        return tally.values()

    @timefunc('second', 100_000)
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            # keys can be strings, bcz they are immutable.
            hashmap[str(sorted(s))].append(s)
        return hashmap.values()


def main():
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(s.groupAnagrams1(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == '__main__':
    main()