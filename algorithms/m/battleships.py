# You're playing Battleship on a grid of cells with R rows and C columns. There are 0 or more battleships on the grid,
# each occupying a single distinct cell. The cell in the ith row from the top and jth column from the left
# either contains a battleship G_{i,j} = 1 or doesn't G_{i,j} = 0
# You're going to fire a single shot at a random cell in the grid. You'll choose this cell uniformly at random from
# the R∗C possible cells. You're interested in the probability that the cell hit by your shot contains a battleship.
# Your task is to implement the function getHitProbability(R, C, G) which returns this probability.

from typing import List


def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    return sum([G[i][j] for i in range(R) for j in range(C)]) / (R * C)