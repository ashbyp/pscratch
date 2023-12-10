# # A positive integer is considered uniform if all of its digits are equal. For example,
# # 222 is uniform, while 223 is not.
# # Given two positive integers A and B, determine the number of uniform integers between A and B, inclusive.
# # Please take care to write a solution which runs within the time limit.
#
# def getUniformIntegerCountInInterval(A: int, B: int) -> int:
#     count = 0
#
#     def check(s):
#         for i in range(1, len(s)):
#             if s[i] != s[0]:
#                 return 0
#         return 1
#
#     for n in range(A, B + 1):
#         if n < 10:
#             count += 1
#             continue
#         elif n < 100:
#
#         count += check(str(n))
#     return count
#


def count_uniform_integers(A, B):
    def is_uniform(num):
        # Convert the number to a string to easily check if all digits are equal
        num_str = str(num)
        return all(digit == num_str[0] for digit in num_str)

    count = 0
    for num in range(A, B + 1):
        if is_uniform(num):
            count += 1
            print(num)

    return count

# Example usage:
A = 100
B = 500000
result = count_uniform_integers(A, B)
print(f"The number of uniform integers between {A} and {B} is: {result}")
