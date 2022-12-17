class Solution:

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
        """
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            last_end = output[-1][1]

            if start <= last_end:
                # merge
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
        return output


def main() -> None:
    print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
    print(Solution().merge([[1, 4], [4, 5]]))  # [[1,5]]


if __name__ == '__main__':
    main()
