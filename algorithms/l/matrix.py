
class Solution:

    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for row in range(n):
            for col in range(n):
                matrix[row][col], matrix[col][n-row-1] = matrix[col][n-row-1], matrix[row][col]
        return matrix


def main() -> None:
    print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])) # [[7,4,1],[8,5,2],[9,6,3]]
    print(Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
    # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

if __name__ == '__main__':
    main()