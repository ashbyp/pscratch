# There are N dishes in a row on a kaiten belt, with the ith dish being of type D
# Some dishes may be of the same type as one another.
# You're very hungry, but you'd also like to keep things interesting. The N dishes will arrive in front of you,
# one after another in order, and for each one you'll eat it as long as it isn't the same type as any of the
# previous K dishes you've eaten. You eat very fast, so you can consume a dish before the next one gets to you.
# Any dishes you choose not to eat as they pass will be eaten by others.
# Determine how many dishes you'll end up eating.
# Please take care to write a solution which runs within the time limit.

from typing import List


def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    eaten = {}
    count = 0
    for x in D:
        if x not in eaten:

            eaten[x] = count
            count += 1
        else:
            last = eaten[x]
            if (count - last) > K:

                eaten[x] = count
                count += 1
    return count
