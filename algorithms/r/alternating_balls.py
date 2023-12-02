
def solution(bucket_list: str, debug=True) -> int:
    bucket_list = list(bucket_list)
    len_buckets = len(bucket_list)

    if not len_buckets:
        return 0

    starting_positions = [i for i in range(len(bucket_list)) if bucket_list[i] == 'B']
    num_balls = len(starting_positions)

    if not num_balls:
        return 0

    sequence_length = len(starting_positions) * 2 - 1

    if sequence_length > len_buckets:
        return -1

    if debug:
        print('--------------------------------------------------')
        print('Buckets           ', buckets)
        print('Len buckets       ', len_buckets)
        print('Num balls         ', num_balls)
        print('Starting positions', starting_positions)
        print('Sequence length   ', sequence_length)

    def sequence_to_string(test_positions) -> str:
        to_print = ''
        for pos in range(len_buckets):
            if pos in test_positions:
                to_print += 'B'
            else:
                to_print += '.'
        return to_print

    starting_positions_set = set(starting_positions)

    def calc_moves(test_positions) -> int:
        m = 0
        for pos in test_positions:
            if pos not in starting_positions_set:
                m += 1
        return m

    min_moves = float('inf')

    for i in range(0, len_buckets - sequence_length + 1):
        positions = [pos for pos in range(i, i + sequence_length + 1, 2)]
        moves = calc_moves(positions)
        if debug:
            print('   Test sequence', sequence_to_string(positions))
            print('   Moves        ', moves)
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