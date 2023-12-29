pdata = """L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4"""
tdata = """R8, R4, R4, R8"""

data=pdata

N=1
S=2
E=3
W=4

def part2():
    seen = {(0, 0)}
    x, y, h = 0, 0, N
    for direction in data.replace(' ', '').split(','):
        d, s = direction[0], int(direction[1:])
        if h == N:
            if d == 'R':
                for i in range(x+1, x + s + 1):
                    if (i, y) in seen:
                        print(abs(i) + abs(y))
                        return
                    seen.add((i, y))
                x += s
                h = E
            else:
                for i in range(x-1, x - s + 1, -1):
                    if (i, y) in seen:
                        print(abs(i) + abs(y))
                        return
                    seen.add((i, y))
                x -= s
                h = W
        elif h == S:
            if d == 'R':
                for i in range(x-1, x - s + 1, -1):
                    if (i, y) in seen:
                        print(abs(i) + abs(y))
                        return
                    seen.add((i, y))
                x -= s
                h = W
            else:
                for i in range(x+1, x + s + 1):
                    if (i, y) in seen:
                        print(abs(i) + abs(y))
                        return
                    seen.add((i, y))
                x += s
                h = E
        elif h == E:
            if d == 'R':
                for i in range(y + 1, y + s + 1):
                    if (x, i) in seen:
                        print(abs(x) + abs(i))
                        return
                    seen.add((x, i))
                y += s
                h = S
            else:
                for i in range(y - 1, y - s + 1, -1):
                    if (x, i) in seen:
                        print(abs(x) + abs(i))
                        return
                    seen.add((x, i))
                y -= s
                h = N
        elif h == W:
            if d == 'R':
                for i in range(y - 1, y - s + 1, -1):
                    if (x, i) in seen:
                        print(abs(x) + abs(i))
                        return
                    seen.add((x, i))
                y -= s
                h = N
            else:
                for i in range(y + 1, y + s + 1):
                    if (x, i) in seen:
                        print(abs(x) + abs(i))
                        return
                    seen.add((x, i))
                y += s
                h = S



def part1():
    x, y , h = 0, 0, N
    for direction in data.replace(' ', '').split(','):
        d, s = direction[0], int(direction[1:])
        if h == N:
            if d == 'R':
                x += s
                h = E
            else:
                x -= s
                h = W
        elif h == S:
            if d == 'R':
                x -= s
                h = W
            else:
                x += s
                h = E
        elif h == E:
            if d == 'R':
                y += s
                h = S
            else:
                y -= s
                h = N
        elif h == W:
            if d == 'R':
                y -= s
                h = N
            else:
                y += s
                h = S

        # print(d, s, f'({x},{y})')

    print(abs(x) + abs(y))



if __name__ == '__main__':
    part1()
    part2()
