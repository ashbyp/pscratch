# there are n buckets arranged in a row. each bucket either is empty or contains a ball. the buckets are specified
# as a string buckets consisting of characters "." (empty bucket) and " b " (bucket with aball). for example, for
# buckets = "b. bb. b. . b" the row of buckets appears as follows: in one move you can take the ball out of any bucket and
# place it in another (empty) bucket. your goal is to arrange the balls to create an alternating sequence of full and empty buckets.
# in other words, the distance between two consecutive balls should be equal to 2 . note that the sequence may start at any bucket. for
#     example, in the figure below, the balls are placed correctly: on the other hand, in both of the figures below, the balls are placed
#     incorrectly: what is the minimum number of moves required to create a correct sequence of balls in buckets write a function:




def move_fwd(buckets, index):
    return []

def move_bwd(buckets, index):
    return []

def solution(buckets):
    num_buckets = len(buckets)

    for





# Example usage:
buckets = "B.B.BB..B"
result = solution(buckets)
print(result)
