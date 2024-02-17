question = "https://adventofcode.com/2020/day/10"
input_data = "https://adventofcode.com/2020/day/10/input"

pdata = """17
110
146
144
70
57
124
121
134
12
135
120
19
92
6
103
46
56
93
65
14
31
63
41
131
60
73
83
71
37
85
79
13
7
109
24
94
2
30
3
27
77
91
106
123
128
35
26
112
55
97
21
100
88
113
117
25
82
129
66
11
116
64
78
38
99
130
84
98
72
50
36
54
8
34
20
127
1
137
143
76
69
111
136
53
43
140
145
49
122
18
42"""

tdata = """16
10
15
5
1
11
7
19
6
12
4"""

tdata2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


def part2(data: str, debug: bool = False):
    start_nums = sorted(list(map(int, data.splitlines())))
    start_nums.append(start_nums[-1] + 3)

    ans = {}
    ans[0] = 1
    for a in start_nums:
        ans[a] = ans.get(a - 1, 0) + ans.get(a - 2, 0) + ans.get(a - 3, 0)

    print(ans[start_nums[-1]])


def part1(data: str, debug: bool = False):
    nums = sorted(list(map(int, data.splitlines())))
    nums.insert(0, 0)
    nums.append(nums[-1] + 3)

    if debug:
        print(nums)

    one, three = 0, 0
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        if diff == 1:
            one += 1
        elif diff == 3:
            three += 1

    if debug:
        print('1s', one, '3s', three)

    print(one * three)


def main():
    import timeit

    def run(msg, data, fn, debug):
        if data:
            print(f'*** {msg:13} ---------------')
            start = timeit.default_timer()
            fn(data, debug)
            elapsed_ms = (timeit.default_timer() - start) * 1000
            print(f'Time {elapsed_ms:.10f} ms ------------')
            print()

    run("Part 1 test", tdata, part1, True)
    run("Part 1 puzzle", pdata, part1, False)
    run("Part 2 test", tdata, part2, True)
    run("Part 2 puzzle", pdata, part2, False)


if __name__ == '__main__':
    main()
