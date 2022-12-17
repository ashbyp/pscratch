from utils.measure import checker


def solution1(blocks):
    N = len(blocks)
    distance = 0
    for i in range(N):
        j = i

        while j > 0 and blocks[j - 1] >= blocks[j]:
            j -= 1
        low = j
        j = i

        while j < N - 1 and blocks[j + 1] >= blocks[j]:
            j += 1
        high = j

        distance = max(distance, high - low)

    return distance + 1


def solution2(blocks: list[int]) -> int:
    curr_peak = prev_peak = 0
    repeats = 0
    distance = 0
    up = False

    for i in range(len(blocks) - 1):
        curr_h = blocks[i]
        next_h = blocks[i + 1]
        if next_h >= curr_h:
            curr_peak = i + 1
            if next_h == curr_h:
                repeats += 1
            else:
                up = True
                if repeats > 0:
                    repeats = 0
        else:
            if up:
                prev_peak = curr_peak - repeats
                up = False
                repeats = 0
            curr_peak = i + 1
        distance = max(distance, curr_peak - prev_peak)

    return distance + 1


if __name__ == '__main__':
    with checker(solution1, repeat=10) as c:
        c.check_1([2, 6, 8, 5], 3)
        c.check_1([1, 5, 5, 2, 6], 4)
        c.check_1([1, 1], 2)
    with checker(solution2, repeat=10) as c:
        c.check_1([2, 6, 8, 5], 3)
        c.check_1([1, 5, 5, 2, 6], 4)
        c.check_1([1, 1], 2)

