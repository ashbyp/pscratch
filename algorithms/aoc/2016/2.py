pdata = """DULUDRDDDRLUDURUUULRRRURDRDULRUDDUDRULUDDUDRLDULRRLRDRUDUUULUUDLRURDUDDDDRDLLLLULRDLDRDLRLULRUURDDUULUDLRURRDDRDDRDDLDRDLLUURDRUULRRURURRDLRLLLUDULULULULUDRLLRUDUURLDRLRLRDRRDRLLLDURRDULDURDDRLURRDURLRRRLDLLLDRUUURLRDLDLLLLRDURRLDLULRLDDLDLURLRRDDRUDDUULRURRUDLRDLDUURDDDDRLRURUDULUDLRRLLLLLRDRURLLDLDULUUDLUDDDRLLDRRUDLLURRUUDDRRLLRRLDDDURLDRDRLURRRRDRRRDDUDULULDURRUUURRRDULUUUDDRULDRLLRDLDURLURRLLRUUUULRDURLLDDRLLDLRLRULUUDRURUDLLURUDDRDURLRDRRRDURLDDRDRLRLLURULUUULUDDDULDLRDDDRDLLRRLDRDULLUUUDLDDLDDDLLLLLLLDUDURURDURDRUURRRDDRDUDLULDURDUDURDDDRULDURURURRLURLURLUURLULDLLRUULURDDRLRDDLRDLRRR
LUURLRUDRRUDLLDLUDDURULURLUUDUUDDRLUULRDUDDUULDUUDRURDDRRDRLULLRDRDLRLLUURRUULRLDRULUDLDUUDDDRDDLRDLULDRLDUULDLRDLLLDLDLRDUULUDURRULLRLDUDRLLLULUUUULUUDUUURRRDULLUURUDRRLDURRUULDRDULDUDRDUUULUUDDRLUDRLDLDRUUURDLDUDRUDUURLLRRLRLLRRLDULDDULUDUUURULDDUDUDRURRDLULRUDDURDLDLLRRRLDRLULLLRUULDUDLUUDURRLLLRLUDURRDDLDRDDDLURDLDRRUDUDLUDULULRUUUDLUURLLRLDDLURULDURDLRRDDDDURLDDLLDDULLLRLDLDULDUUDDRLDUURDDLDLUUDULRRLRLUURURUURLRLURUURLDRUURLLRDDUUUDULUDDDRDRLDRDRRLRLDULLRRUDLURULULRDRURURLULDUDLRURLRDDRULDDLRD
LUDRULUULRRDDDDRRDUURUDDRLDDLDRDURRURULRDLDLDUUDRRDUUDUDLLLRRLDUDDRLDDLRRLRDRLUDLULUDDUUDULDUUULUDLDDURLDURUDLDRUUDRLRRLDLDDULDUUDDLDDLLURDRLRUURDDRUDDUDLDRRLRUDRUULRRRLRULULURDLRRURDRLRULDDDRDUULLURUUUURUDDLRRRRRDURLULDLUULUDRRUDUDRRDDRURDURLRLUDDLDLRRULUDLDDRLDDLDDDLLLLRDLLUULDDLULDLDRDDUDLURUDLDLDDRRUUDDDLRLLLDRRDDDUURDUDURUURRDRLLDUDLDUULLDLDLLUULLRRULDLDRURLDULDRUURDURRURDLRDLLLDRRUDRUUDRURLUDDRURLDURRDLUUDLUUDULLLDDDDRRDLLLDLURULDDRDLUUURRDRRUUDDUL
DUUULDUDDDURLLULDDLLUDURLLLURULULURUURDRURLRULLLLDRDDULRRDRRLLLRDDDUULLRRURRULLDDURRRLRDDLULDULLDUDLURRDLDDLURDLRLLDRURLLRLLRRRDRRRURURUUDDLLDDLDDDLRLURUUUULRDLUDDDURLLDDRLDRRLLUDUUULRLLDRRRLRUUDLDUULRLUDRULLLLDUDLLUUDDRUURLURUDRDDDLRURUDRLULLULUUDLDURDULRRDRLDURUULRDRRRDRDRRLRLRDDUULLRDLDURDDDULURRLULDDURDURDDUDURDLLUUULUDULRDDLDRDRUDLLUURDLRDURURULURULLDRLLRRULDLULULDLULRURLRRLUDLLLRLUDLURLULDULDRLLLDLDDDDRDRLRRLRDULUUDULDDLDURDLLLDDDDLLUURRDURLDLUDDLULRUUUDDRRLDLLLRDLLDRRRDDLULLURDDRRRRLDLRLLLRL
LULLRRDURRLDUUDRRURLURURRRLRDRUULUULURLLURRDRULRDURDDDDUULLLLDUULDLULURDRLDLULULDRLLDLLRLRULURUDRUUDULRULLLUDRULUDRLLUDLDRRDRUUURURLRDURDRLRDDDURLURRDLRUUUDUURULULDLUULRDLRRRDRDRLLLDLRRDRLLDDULDRUDRRLULLRDLDUDDULRDDLULRURULRLLLULDLLLLRDLDRURUDUURURLDRLUULLDUDULUDDDULUDLRUDDUDLULLUULUUURULURRULRDDURDDLURLRRDRDLDULRLRDRRRULRDDDRLLDDDDRRRRDRDLULUURDURULDLRDULDUDLDURUDLUDLUDDDUDURDURDDURLLRUDUURRRUDRRRRULLLLDDDLUULLUULRRRULDLURDLULRULDRLR"""
tdata = """ULL
RRDDD
LURDL
UUUUD"""

data = pdata

WHERE = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

BUTTONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

BUTTONS_P2 = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', '1', ' ', ' ', ' '],
    [' ', ' ', '2', '3', '4', ' ', ' '],
    [' ', '5', '6', '7', '8', '9', ' '],
    [' ', ' ', 'A', 'B', 'C', ' ', ' '],
    [' ', ' ', ' ', 'D', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
]


def part2():
    num = ""
    x, y = (3, 1)
    for ins in data.splitlines():
        for d in ins:
            new_x = x + WHERE[d][0]
            new_y = y + WHERE[d][1]
            if BUTTONS_P2[new_x][new_y] != ' ':
                x = new_x
                y = new_y
        num += str(BUTTONS_P2[x][y])
    print(num)


def part1():
    num = ""
    x, y = (1, 1)
    for ins in data.splitlines():
        for d in ins:
            x = x + WHERE[d][0]
            y = y + WHERE[d][1]
            if x > 2: x = 2
            if x < 0: x = 0
            if y > 2: y = 2
            if y < 0: y = 0
        num += str(BUTTONS[x][y])
    print(num)


if __name__ == '__main__':
    part1()
    part2()
