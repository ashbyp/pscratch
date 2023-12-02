
def solution(buckets_str: str) -> int:
    buckets = list(buckets_str)
    len_buckets = len(buckets)

    starting_positions = [i for i in range(len(buckets)) if buckets[i] == 'B']
    if not starting_positions:
        return 0

    sequence_length = len(starting_positions) * 2 - 1

    if sequence_length > len_buckets:
        return -1

    starting_positions_set = set(starting_positions)
    min_moves = float('inf')

    for i in range(0, len_buckets - sequence_length + 1):
        positions = [pos for pos in range(i, i + sequence_length + 1, 2)]
        moves = 0
        for pos in positions:
            if pos not in starting_positions_set:
                moves += 1
        min_moves = min(min_moves, moves)

    return min_moves



# Example usage:
buckets = "B.B.BB..B"
result = solution(buckets)
print(result)

buckets = "B....B"
result = solution(buckets)
print(result)

buckets = "BB........BB"
result = solution(buckets)
print(result)

buckets = "BBBB..."
result = solution(buckets)
print(result)

buckets = "BBBBB.."
result = solution(buckets)
print(result)