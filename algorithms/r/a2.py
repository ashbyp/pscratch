# there are n buckets arranged in a row. each bucket either is empty or contains a ball. the buckets are specified
# as a string buckets consisting of characters "." (empty bucket) and " b " (bucket with aball).
# In one move you can take the ball out of any bucket and
# place it in another (empty) bucket. your goal is to arrange the balls to create an alternating sequence of full and empty buckets.
# in other words, the distance between two consecutive balls should be equal to 2 . note that the sequence may start at any bucket.
# python function for miminu number
from collections import Counter


def move_left(buckets, index):
    if index == 0:
        return -1

    for i in range(0, index):
        if can_place(buckets, i):
            buckets[i], buckets[index] = buckets[index], buckets[i]
            return 1

    return -1


def move_right(buckets, index):
    if index == len(buckets) - 1:
        return -1

    for i in range(len(buckets) - 1, index,  -1):
        if can_place(buckets, i):
            buckets[i], buckets[index] = buckets[index], buckets[i]
            return 1

    return -1


def needs_moving(buckets, index):
    if index == 0:
        return buckets[1] == 'B'
    if index == len(buckets) - 1:
        return buckets[len(buckets) - 2] == 'B'
    return buckets[index - 1] == 'B' or buckets[index+1] == 'B'


def can_place(buckets, index):
    if buckets[index] == 'B':
        return False
    if index == 0:
        return buckets[index+1] == '.'
    if index == len(buckets) - 1:
        return buckets[len(buckets) - 2] == '.'
    return buckets[index - 1] == '.' and buckets[index+1] == '.'


def solution(buckets):
    moves = 0
    buckets = list(buckets)
    for i, b in enumerate(buckets):



# Example usage:
buckets = "B.B.BB..B"
buckets = "B..B"
result = solution(buckets)
print(result)
