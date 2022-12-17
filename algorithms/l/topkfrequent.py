from utils.measure import timefunc

class Solution:

    @timefunc('first', 100_100)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        tally = {}
        for n in nums:
            if n not in tally:
                tally[n] = 1
            else:
                tally[n] = tally[n] + 1
        zally = sorted(((v, k) for k, v in tally.items()), reverse=True)
        return [x[1] for x in zally[0:k]]

    @timefunc('second', 100_100)
    def topKFrequent1(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res

def main():
    print(Solution().topKFrequent([1,1,1,2,2,3], 2))
    print(Solution().topKFrequent1([1, 1, 1, 2, 2, 3], 2))

if __name__ == '__main__':
    main()

