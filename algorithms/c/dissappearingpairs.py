
def solution(s):
    aa='AA'
    bb='BB'
    cc='CC'

    #print(f'start: {s}')

    while True:
        removed = False
        for i in range(0, len(s) - 1):
            chunk = s[i:i+2]
            #print(chunk)
            if chunk == aa or chunk == bb or chunk == cc:
                s = s[0:i] + s[i+2:]
                #print(f'rem: {s}')
                removed = True
                break
        #print(f'loop end {i}')
        if not removed:
            return s


def solution1(s):
    modified = ""

    for x in s:
        size = len(modified)
        if size > 0 and modified[size - 1] == x:
            modified = modified[0:-1]
        else:
            modified += x
    return modified


if __name__ == '__main__':
    # print(f"Res: {solution('ACCAABBC')}")
    # print(f"Res: {solution('ABCBBCBA')}")
    # print(f"Res: {solution('BABABA')}")
    # print(f"Res: {solution('AAAAA')}")
    # print(f"Res: {solution('B')}")
    # print(f"Res: {solution('')}")
    # print('===========')
    # print(f"Res: {solution1('ACCAABBC')}")
    # print(f"Res: {solution1('ABCBBCBA')}")
    # print(f"Res: {solution1('BABABA')}")
    # print(f"Res: {solution1('AAAAA')}")
    # print(f"Res: {solution1('B')}")
    # print(f"Res: {solution1('')}")

    print(f"Res: {solution1('ACCAABBC')}")
    print(solution1('ABBCDDC'))
    print(solution1('AABBAA'))
    #
    # "ABBCDDC" -> "ABBCC" -> "ABB" -> "A"
    # "AABBAA" -> "AAAA" -> "AA" -> ""
