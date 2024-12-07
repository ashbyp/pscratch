question = "https://adventofcode.com/2024/day/5"
input_data = "https://adventofcode.com/2024/day/5/input"

pdata = """95|51
92|45
92|39
55|51
55|91
55|43
46|93
46|69
46|84
46|99
11|43
11|99
11|63
11|39
11|88
66|86
66|96
66|68
66|24
66|76
66|81
19|95
19|45
19|66
19|44
19|64
19|55
19|86
45|88
45|69
45|57
45|44
45|86
45|54
45|51
45|58
84|37
84|55
84|18
84|28
84|76
84|66
84|86
84|68
84|71
67|69
67|66
67|71
67|37
67|61
67|26
67|55
67|52
67|45
67|19
63|88
63|73
63|97
63|37
63|84
63|42
63|52
63|95
63|19
63|64
63|45
91|38
91|84
91|26
91|43
91|77
91|82
91|39
91|97
91|99
91|35
91|92
91|73
69|88
69|86
69|61
69|51
69|57
69|18
69|58
69|24
69|68
69|38
69|81
69|62
69|32
97|44
97|19
97|55
97|81
97|24
97|68
97|69
97|58
97|96
97|71
97|64
97|14
97|76
97|18
28|54
28|62
28|86
28|91
28|81
28|23
28|61
28|52
28|76
28|64
28|57
28|95
28|18
28|88
28|96
42|96
42|95
42|26
42|35
42|68
42|84
42|69
42|55
42|97
42|88
42|28
42|81
42|67
42|86
42|71
42|66
35|37
35|95
35|76
35|96
35|52
35|97
35|69
35|24
35|88
35|61
35|81
35|68
35|86
35|18
35|19
35|44
35|14
73|86
73|77
73|26
73|96
73|67
73|66
73|52
73|35
73|45
73|84
73|69
73|24
73|18
73|19
73|37
73|55
73|64
73|97
61|93
61|91
61|57
61|92
61|44
61|63
61|42
61|51
61|65
61|54
61|38
61|62
61|73
61|58
61|46
61|39
61|77
61|23
61|43
93|67
93|95
93|97
93|18
93|52
93|81
93|35
93|96
93|45
93|71
93|19
93|73
93|77
93|69
93|86
93|64
93|28
93|37
93|66
93|88
65|35
65|28
65|39
65|99
65|84
65|67
65|19
65|45
65|37
65|71
65|93
65|97
65|63
65|42
65|77
65|32
65|73
65|43
65|92
65|26
65|46
23|84
23|77
23|38
23|65
23|93
23|26
23|73
23|11
23|43
23|46
23|62
23|39
23|67
23|92
23|63
23|99
23|82
23|35
23|54
23|42
23|51
23|91
58|62
58|92
58|82
58|43
58|93
58|99
58|77
58|23
58|65
58|39
58|54
58|51
58|63
58|46
58|73
58|26
58|38
58|91
58|11
58|84
58|35
58|32
58|42
52|32
52|57
52|11
52|14
52|23
52|68
52|44
52|55
52|43
52|91
52|76
52|54
52|18
52|51
52|61
52|65
52|82
52|58
52|46
52|62
52|39
52|38
52|92
52|86
76|99
76|62
76|82
76|73
76|46
76|42
76|61
76|32
76|54
76|44
76|93
76|63
76|38
76|57
76|51
76|43
76|91
76|14
76|65
76|58
76|39
76|23
76|92
76|11
38|77
38|99
38|84
38|35
38|66
38|65
38|43
38|28
38|46
38|92
38|67
38|97
38|82
38|32
38|42
38|39
38|19
38|26
38|63
38|37
38|93
38|11
38|71
38|73
44|57
44|32
44|63
44|77
44|51
44|67
44|65
44|58
44|23
44|84
44|93
44|73
44|82
44|11
44|92
44|42
44|39
44|62
44|99
44|43
44|54
44|46
44|38
44|91
62|77
62|42
62|73
62|84
62|43
62|11
62|32
62|35
62|67
62|26
62|92
62|54
62|63
62|65
62|38
62|91
62|99
62|97
62|19
62|46
62|39
62|51
62|93
62|82
54|11
54|71
54|99
54|51
54|42
54|35
54|39
54|67
54|65
54|43
54|93
54|46
54|77
54|73
54|26
54|84
54|38
54|82
54|92
54|19
54|32
54|63
54|97
54|66
43|66
43|45
43|37
43|99
43|69
43|67
43|93
43|26
43|28
43|19
43|97
43|71
43|24
43|35
43|63
43|42
43|88
43|95
43|64
43|96
43|77
43|81
43|73
43|84
24|39
24|38
24|11
24|14
24|55
24|91
24|51
24|58
24|86
24|62
24|61
24|65
24|76
24|82
24|44
24|32
24|23
24|46
24|68
24|54
24|57
24|52
24|18
24|92
37|44
37|86
37|64
37|69
37|96
37|24
37|14
37|91
37|57
37|76
37|52
37|88
37|68
37|55
37|54
37|45
37|62
37|58
37|95
37|61
37|81
37|51
37|18
37|23
39|69
39|97
39|88
39|26
39|45
39|96
39|35
39|71
39|19
39|77
39|64
39|67
39|28
39|63
39|73
39|99
39|84
39|93
39|37
39|66
39|42
39|95
39|81
39|43
82|77
82|73
82|67
82|96
82|93
82|26
82|37
82|43
82|19
82|99
82|39
82|11
82|95
82|28
82|97
82|42
82|69
82|71
82|64
82|84
82|35
82|66
82|63
82|45
81|38
81|51
81|18
81|55
81|52
81|76
81|44
81|92
81|68
81|14
81|86
81|32
81|24
81|61
81|62
81|57
81|91
81|23
81|46
81|58
81|54
81|82
81|65
81|11
71|86
71|55
71|62
71|66
71|57
71|45
71|76
71|69
71|96
71|23
71|64
71|44
71|28
71|95
71|24
71|37
71|18
71|61
71|68
71|88
71|58
71|52
71|14
71|81
99|19
99|52
99|66
99|84
99|88
99|42
99|95
99|28
99|69
99|64
99|35
99|45
99|24
99|93
99|97
99|96
99|81
99|73
99|71
99|26
99|67
99|77
99|37
99|86
32|37
32|71
32|46
32|11
32|39
32|96
32|45
32|66
32|28
32|43
32|63
32|35
32|19
32|92
32|73
32|93
32|26
32|84
32|67
32|99
32|77
32|82
32|42
32|97
26|64
26|37
26|69
26|55
26|44
26|86
26|61
26|76
26|24
26|81
26|45
26|19
26|14
26|95
26|97
26|88
26|71
26|66
26|35
26|28
26|96
26|52
26|68
26|18
14|99
14|43
14|44
14|46
14|54
14|32
14|65
14|84
14|82
14|93
14|23
14|57
14|39
14|42
14|63
14|73
14|62
14|38
14|11
14|92
14|77
14|58
14|91
14|51
57|91
57|93
57|54
57|99
57|58
57|42
57|23
57|67
57|26
57|77
57|82
57|11
57|92
57|38
57|65
57|39
57|63
57|73
57|43
57|32
57|51
57|84
57|46
57|62
18|23
18|99
18|91
18|44
18|61
18|62
18|82
18|58
18|63
18|43
18|55
18|38
18|51
18|46
18|76
18|57
18|32
18|68
18|39
18|11
18|65
18|54
18|14
18|92
96|65
96|23
96|51
96|52
96|38
96|88
96|44
96|76
96|61
96|86
96|64
96|62
96|55
96|18
96|14
96|95
96|57
96|24
96|54
96|91
96|69
96|58
96|68
96|81
68|44
68|61
68|82
68|63
68|46
68|92
68|62
68|23
68|91
68|32
68|76
68|43
68|38
68|65
68|99
68|73
68|11
68|14
68|39
68|57
68|93
68|51
68|54
68|58
77|66
77|28
77|86
77|64
77|19
77|45
77|84
77|71
77|68
77|67
77|35
77|69
77|52
77|96
77|55
77|18
77|76
77|24
77|26
77|37
77|95
77|81
77|88
77|97
88|18
88|86
88|52
88|65
88|32
88|61
88|92
88|81
88|76
88|38
88|23
88|24
88|58
88|68
88|44
88|62
88|82
88|14
88|51
88|46
88|55
88|54
88|91
88|57
51|39
51|42
51|93
51|99
51|71
51|97
51|38
51|84
51|67
51|28
51|65
51|73
51|82
51|11
51|32
51|26
51|77
51|66
51|19
51|43
51|63
51|35
51|46
51|92
86|58
86|62
86|46
86|32
86|55
86|92
86|38
86|39
86|43
86|44
86|23
86|91
86|76
86|54
86|18
86|63
86|57
86|68
86|65
86|61
86|14
86|11
86|51
86|82
64|95
64|81
64|23
64|54
64|18
64|51
64|55
64|61
64|86
64|88
64|62
64|52
64|91
64|14
64|57
64|32
64|92
64|58
64|44
64|65
64|68
64|38
64|76
64|24
95|57
95|68
95|76
95|23
95|92
95|81
95|24
95|55
95|54
95|58
95|46
95|86
95|14
95|32
95|62
95|38
95|18
95|91
95|65
95|44
95|52
95|88
95|61
92|77
92|67
92|42
92|97
92|96
92|73
92|71
92|37
92|82
92|84
92|63
92|26
92|35
92|28
92|46
92|99
92|69
92|43
92|19
92|93
92|66
92|11
55|44
55|11
55|23
55|92
55|57
55|65
55|54
55|68
55|76
55|32
55|61
55|58
55|38
55|82
55|63
55|93
55|46
55|14
55|99
55|39
55|62
46|19
46|42
46|39
46|97
46|63
46|77
46|67
46|28
46|73
46|66
46|37
46|43
46|82
46|11
46|26
46|71
46|45
46|96
46|35
46|64
11|73
11|93
11|69
11|19
11|95
11|84
11|71
11|96
11|77
11|64
11|45
11|67
11|26
11|66
11|37
11|42
11|35
11|97
11|28
66|88
66|55
66|44
66|91
66|95
66|52
66|23
66|61
66|18
66|45
66|37
66|62
66|69
66|58
66|64
66|14
66|57
66|28
19|69
19|52
19|96
19|28
19|24
19|37
19|68
19|14
19|76
19|57
19|61
19|71
19|58
19|81
19|23
19|18
19|88
45|62
45|55
45|64
45|52
45|24
45|14
45|18
45|81
45|38
45|95
45|96
45|76
45|61
45|23
45|91
45|68
84|69
84|61
84|81
84|88
84|97
84|35
84|95
84|64
84|19
84|24
84|52
84|45
84|26
84|96
84|67
67|64
67|14
67|96
67|18
67|24
67|81
67|35
67|28
67|68
67|86
67|76
67|88
67|97
67|95
63|66
63|77
63|67
63|81
63|71
63|24
63|96
63|93
63|69
63|35
63|99
63|28
63|26
91|63
91|54
91|46
91|67
91|19
91|71
91|65
91|51
91|42
91|93
91|32
91|11
69|55
69|14
69|52
69|54
69|95
69|23
69|91
69|44
69|76
69|65
69|64
97|57
97|61
97|86
97|52
97|28
97|66
97|45
97|37
97|88
97|95
28|58
28|24
28|69
28|45
28|14
28|55
28|68
28|37
28|44
42|19
42|77
42|64
42|24
42|45
42|18
42|52
42|37
35|64
35|55
35|66
35|71
35|57
35|45
35|28
73|95
73|42
73|81
73|88
73|28
73|71
61|32
61|14
61|11
61|99
61|82
93|84
93|24
93|42
93|26
65|82
65|11
65|66
23|97
23|32
58|67

37,45,96,69,95,88,81,24,52,86,18,55,68,76,61,57,58,23,62,91,54
97,71,66,28,95,86,18,76,61,14,57
11,58,62,65,82,76,43
35,93,66,42,86,45,88,67,96,26,73,71,95,81,24
64,95,88,81,24,52,86,18,55,68,76,61,14,44,57,58,23,62,91,51,38,65,32
69,88,81,24,86,18,55,68,76,61,14,44,57,58,23,62,91,54,51,38,65
54,65,32,92,82,39,43,99,93,73,42,84,26,97,19
92,46,82,39,43,73,84,67,19,71,96
65,32,67,99,77,57,39,93,11,51,42,63,91,58,62,38,73
92,26,93,66,51,39,42
73,63,35,77,37,19,43,93,26,95,28,66,71,45,67,42,84
99,93,73,42,84,26,97,71,66,28,37,45,64,24,52
97,71,66,28,45,96,69,64,95,88,81,24,52,86,18,55,68,14,57
39,54,92,91,51,11,46,84,77,43,23,73,63,58,62,99,32
37,95,55,76,58,91,54
11,44,54,46,62
26,99,11,97,39,62,32,46,92
14,44,58,23,54,38,92,39,43,63,77
99,93,42,84,26,35,97,71,66,37,69,64,95
61,44,57,23,62,91,51,38,32,92,82,11,39,43,63,93,42
51,63,93,73,42,84,67,26,97,71,66
88,81,86,14,23
18,55,68,76,61,44,57,58,62,91,54,38,65,92,46,82,11,43,63
93,63,11,23,51,68,76
38,43,82,77,91,23,14
42,84,37,45,88,52,55
44,61,54,62,76,82,92,23,63,57,99,38,32,14,65,93,11
97,64,96,66,88,86,68,76,28,61,24,37,18,19,69,14,44,71,45,52,35,55,81
91,38,65,32,92,46,11,39,43,63,99,93,73,77,84,67,19
91,38,65,46,63,99,84,97,19
73,63,43,51,99,92,38,82,26,65,84,46,97,93,11,77,42,54,35,19,71
84,26,64,95,24,86,18
28,37,44,19,58,76,52,14,96
55,68,76,61,14,44,57,58,23,91,54,51,65,32,92,82,11,39,43,63,99
46,82,11,39,43,63,99,93,73,42,77,84,67,26,35,97,71,66,28,37,45,96,69
35,37,96,64,52,55,44
37,63,66,84,64,45,26,67,35,88,69,71,28,81,77,42,93,95,99,97,24,96,19
24,81,19,88,18,37,26,95,45,84,67,28,97,52,66,73,69,86,35
14,76,95,57,68,86,92,55,51,91,52,61,81,54,65,24,18,58,44,32,23
65,73,19,43,99,26,92,71,11,67,39,66,84,28,46,93,97,35,32
45,96,86,76,61,44,58,54,51
32,92,46,82,11,39,63,99,93,73,42,77,84,67,26,35,97,19,71,66,28,37,45
69,61,44,62,91,54,65
91,54,32,99,57,92,65,14,39,46,63,42,43,58,44,82,61,51,93
92,82,11,63,93,73,42,77,97,19,71,66,37,45,96
42,26,71,37,45,64,24,52,86,18,55
82,18,61,62,57,14,46,58,54,24,91,11,86,68,52,92,65,76,23
39,43,38,71,46,84,99,73,67,77,51,19,35,92,11,97,66,63,65,82,93,32,26
37,82,42,43,39,64,28
68,69,71,64,14,96,86,52,28,44,57,95,19,55,18,76,61,88,37,97,66
54,58,18,52,44,11,39,82,92,76,51,86,14,55,57
37,45,96,69,95,81,24,52,86,18,68,61,14,44,58,62,91
84,67,26,35,19,71,66,28,37,45,96,69,64,95,88,81,24,52,86,18,55,68,76
71,66,28,37,45,69,64,88,81,24,52,86,18,68,76,61,14,44,57,58,23
77,73,35,28,96,71,43,39,66,95,69,37,84,26,93,19,99
71,96,66,11,73,37,35,28,97,84,69,39,93,77,43,45,99,63,46
91,54,51,38,65,32,92,46,82,39,43,99,93,73,42,77,84,67,26,97,19
68,38,86,32,61,54,44
92,46,82,11,43,63,99,93,73,42,77,84,67,26,35,97,19,71,66,28,37,45,96
86,95,96,28,52,26,88,97,69,19,35,55,66,24,45,67,37,76,71
65,46,82,39,63,42,67,26,35,19,71,66,37
68,76,14,44,57,58,62,91,54,51,32,92,46,82,43,99,93
45,64,95,81,52,86,18,55,68,61,23
69,64,86,55,68,61,44,58,62,38,65
14,62,91,51,65,46,82,11,77
39,91,63,46,11,84,82,65,35
69,64,95,88,81,24,52,86,18,55,68,76,61,14,44,57,58,23,62,54,51,38,65
92,82,39,93,73,42,77,84,67,97,19,71,66,28,37,45,96
19,71,66,28,37,45,96,69,64,88,81,24,52,86,18,55,68,76,61,14,44,57,58
67,19,42,96,18,24,55
84,67,26,35,97,19,71,66,45,69,24
32,92,46,82,11,43,99,93,42,84,67,35,19,71,66,28,37
39,43,99,73,42,77,84,26,97,19,66,28,37,96,64,95,88
84,91,32,97,73,93,46,19,11,99,39
93,67,91,39,54
24,65,86,32,57,55,44
38,65,46,11,39,42,77,84,28
11,43,63,99,93,73,77,84,67,35,97,19,71,28,45,96,95
91,57,39,65,76,46,38,55,58,54,18,44,62,51,86,68,92,14,52,32,82
81,24,52,68,76,61,14,57,58,23,62,54,38,92,82
66,63,82,99,97,42,64,11,45,67,37,69,35,71,84,26,93,43,73,96,28
67,38,46,19,11,99,82,54,63,92,32,91,65,51,73
96,28,24,26,45,84,88,99,97,67,77,93,69,42,19,64,95
32,45,39,26,73,37,35
14,57,58,62,91,54,92,39,43,99,93
67,26,35,97,19,71,28,45,95,88,81,24,18,55,68
11,97,66,26,63,93,77,42,39,96,82,69,46
55,76,61,14,57,58,23,62,54,51,38,65,32,92,46,82,11,39,43,63,99
35,37,45,19,73,93,63,24,77,88,67,42,66,28,71
62,32,57,43,63,11,51,82,42,38,61
73,42,77,84,67,26,35,97,19,71,66,28,37,45,96,64,95,88,81,24,52,86,18
45,96,77,37,66,84,73,63,99,97,67,39,95
23,62,82,11,93,67,35
93,42,51,11,58,54,82
51,24,14,65,55,44,86,88,57,58,46
18,55,68,61,14,44,57,23,62,91,54,51,38,65,32,46,82,11,39,43,63
43,99,93,73,42,35,19,71,66,28,96,64,95,88,81
43,73,58,65,99,63,38,51,32,67,39,26,42
61,14,23,46,11,43,99,93,42
46,82,39,63,99,73,42,77,84,67,26,35,19,71,66,28,45,96,69
81,24,52,86,55,68,76,61,14,44,57,58,23,62,54,51,38,32,92,46,82
97,19,71,66,45,88,52,68,57
69,14,88,24,97,52,96,86,76,45,26,81,35,66,37
91,69,57,14,88,38,96,23,76,68,64,61,95,58,81,54,55,18,52,86,51
65,42,39,46,43,77,91,57,58,67,23,38,51
68,77,19,67,69,37,66
38,51,76,44,46,68,65,92,32,91,14,61,39,43,55,54,63,82,18,62,57,23,11
26,35,97,71,28,37,45,69,64,95,88,81,52,86,18,55,68,76,14
95,81,24,52,86,18,68,76,14,44,57,58,23,62,91,54,51,38,65,32,92
14,44,51,32,92,46,77
82,77,84,67,35,28,64
77,84,45,81,24,18,68
62,54,51,38,65,32,46,39,43,63,93,84,67,35,97
95,81,52,55,44,38,92
88,71,55,28,37,95,97,18,64,35,44
91,58,61,38,11,32,92,39,65,23,68,76,14,43,82
91,54,51,38,32,92,46,82,11,63,99,77,84,67,26,35,19
18,68,14,44,57,23,62,51,65,32,46,82,43
91,55,69,96,86,62,81,58,44,28,88
57,81,24,66,96,76,68,97,45,37,55
96,69,95,24,86,68,76,61,44,57,23,62,91,54,51
18,86,95,69,52,97,96,28,19,67,81,76,35,45,64
81,54,46,65,24,76,52,51,55,91,86,68,44,57,18,23,82,38,58,62,92,32,14
61,14,95,55,37,69,96,81,71,68,18,26,76,88,66,97,52
84,67,71,66,28,37,45,64,88,68,76
38,32,19,46,54,63,67,65,26,51,97,39,77,84,42,99,43,82,71,11,35,93,73
92,46,82,11,39,63,99,73,77,67,35,66,28
66,28,61,37,58,44,14,71,52,88,68,64,55,18,23,45,95,86,96,57,81
67,97,91,65,46,54,26,35,62
32,92,46,99,73,77,26,35,97,19,71,28,45
86,95,19,77,71,24,66,18,55,68,88,45,67,64,28,37,97
69,64,95,88,81,24,52,86,18,55,68,76,61,14,44,57,58,23,62,91,54,38,65
55,61,86,92,46,14,76,39,51,32,44
88,24,55,52,28,68,45,71,35,64,97,14,26,18,37,76,61
26,73,63,84,58,32,39,92,54,93,38,42,82,77,67
37,45,69,64,95,81,24,52,86,18,68,76,61,14,58,23,62,91,54
44,73,51,93,62,57,38,63,99,54,92,76,58,23,14,32,91
88,81,18,68,61,44,58,23,62,91,54,51,32,92,46
76,73,57,99,63,61,91,14,32,93,23,58,65
84,66,28,64,81,55,76
44,82,39,93,42
92,82,39,63,93,42,66
38,32,82,11,73,77,66
73,42,84,67,97,64,95,24,18
73,92,84,91,57,42,39,77,99,58,54,46,23,65,67
96,64,95,88,81,24,52,86,18,55,68,76,61,14,44,57,58,23,62,91,54,51,38
99,73,35,71,66,28,37,69,52
65,92,46,82,39,63,99,93,42,84,19,71,37
76,71,26,64,86,66,18,95,69,35,28,96,24,37,88,55,81
11,39,43,63,93,73,42,77,84,26,97,19,71,66,37,45,96,69,95
55,62,95,96,66,86,61,28,45,58,81
64,88,18,44,54,65,32
38,43,77,26,97,71,28
46,43,93,73,42,19,28,45,69
18,61,58,54,51,38,65,32,46,82,11
14,92,82,68,51,76,44,18,32,86,46,55,65,62,52,54,57,39,23,91,58,61,38
99,93,73,42,77,84,67,26,97,66,28,37,45,69,64,95,24
26,92,42,67,19,99,43,46,28,66,84,73,71,93,82,35,97,11,63,45,39,77,96
81,55,44,92,62,52,88,91,24,54,18,58,46,65,61
84,43,51,39,91,42,99,32,38,23,82,65,11,77,62,73,46
39,43,63,99,93,73,42,77,67,35,97,19,71,66,28,37,45,96,69,95,88
42,97,67,52,96,84,35,45,55,77,81,66,86,71,95,37,24,64,69
38,92,46,82,11,39,63,99,42,97,19
26,35,71,19,77,92,11,65,42,99,51,43,67,63,73,66,93
67,26,35,19,66,37,88,81,52,86,55,68,61
86,68,76,65,92,39,43
81,24,52,61,18,44,76,96,28,64,37,58,14,57,88,68,45,95,86,91,62,69,23
52,18,55,68,57,23,65,82,39
52,91,69,62,51,88,14,24,68,38,55,86,65,64,61,54,18,95,57,81,58
18,14,64,24,68
97,37,96,69,76
26,95,35,77,67,84,71,42,55
58,43,54,65,18,62,38,39,44,14,68,32,86,76,46,91,11,92,51
55,14,91,54,11,39,99
81,45,18,52,37,61,64,95,19,66,58
82,73,54,92,58,44,43,46,61,57,42
35,69,88,24,76,14,44
62,91,54,51,38,65,32,92,46,82,11,39,43,63,93,73,42,77,84,67,26,35,97
88,76,45,96,28,24,95,18,68,55,61,52,19,67,71,86,37,26,69
62,54,51,46,82,11,43,63,99,93,73,77,84,67,26
42,77,84,67,26,35,45,96,52
23,51,38,65,46,82,11,43,99,93,84,26,35
64,44,81,58,66,55,61
84,19,97,26,64,81,28,35,63,99,73,67,93,69,43,88,37,71,95,77,45,66,42
81,24,52,86,55,68,76,61,14,44,57,58,23,62,91,51,38,32,92,46,82
24,18,68,44,57,23,62,91,54,51,38,65,92,82,11
66,28,45,96,69,64,95,88,81,52,86,18,76,14,62
95,86,88,57,71,61,37,18,66,96,24,81,97
65,23,42,91,11,82,43,39,62,57,63
26,24,19,35,81,86,55
46,28,84,73,11,32,82,63,26,99,43,67,66,38,39,97,42,65,35
37,96,88,61,14,44,62
77,84,26,35,97,19,71,66,28,37,45,96,69,64,95,88,81,24,52,86,18,55,68
81,68,57,23,91,54,82
18,55,68,44,57,23,62,91,54,51,38,65,32,43,63
99,93,73,77,26,97,19,71,66,28,37,45,96,64,95,88,81,24,52
95,73,93,99,19,43,64"""

tdata = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def part2(data: str, _debug: bool = False):
    from collections import defaultdict

    blocks = data.split('\n\n')
    before = defaultdict(set)

    for line in blocks[0].splitlines():
        x, y = line.split('|')
        before[int(y)].add(int(x))

    not_ok = []
    for line in blocks[1].splitlines():
        seq = list(map(int, line.split(',')))
        for i in range(len(seq)):
            n = seq[i]
            a = set(seq[i + 1:])

            if a.intersection(before[n]):
                not_ok.append(seq)
                break

    new_ok = []

    for seq in not_ok:
        new_seq = [seq[0]]
        for i in range(1, len(seq)):
            for j in range(0, len(new_seq)):
                if seq[i] in before[new_seq[j]]:
                    new_seq.insert(j, seq[i])
                    break
            else:
                new_seq.append(seq[i])

        new_ok.append(new_seq)

    print(sum(seq[len(seq) // 2] for seq in new_ok))


def part1(data: str, _debug: bool = False):
    from collections import defaultdict

    blocks = data.split('\n\n')
    before = defaultdict(set)

    for line in blocks[0].splitlines():
        x, y = line.split('|')
        before[int(y)].add(int(x))

    ok = []

    for line in blocks[1].splitlines():
        seq = list(map(int, line.split(',')))
        for i in range(len(seq)):
            n = seq[i]
            a = set(seq[i + 1:])
            if a.intersection(before[n]):
                break
        else:
            ok.append(seq)

    print(sum(seq[len(seq) // 2] for seq in ok))


def main():
    import timeit

    def run(msg, data, fn, debug):
        if data:
            print(f'*** {msg:13} ---------------')
            start = timeit.default_timer()
            fn(data, debug)
            elapsed_ms = (timeit.default_timer() - start) * 1000
            print(f'Time {elapsed_ms:.10f} ms ------------')

    run("Part 1 test", tdata, part1, True)
    run("Part 1 puzzle", pdata, part1, False)
    run("Part 2 test", tdata, part2, True)
    run("Part 2 puzzle", pdata, part2, False)


if __name__ == '__main__':
    main()
