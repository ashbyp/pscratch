question = "https://adventofcode.com/2024/day/16"
input_data = "https://adventofcode.com/2024/day/16/input"

pdata = """#############################################################################################################################################
#.........#.................#.........#...#.............................#...#.........#.....#.....#.....#.........#.....#.............#....E#
#.#####.###.#####.#.#########.#.#####.#.#.#.###.#.#######.###.#######.#.#.#.#.###.#.###.###.#.#.###.#.#.#.#######.#.###.#.#####.#####.#.###.#
#.....#...#.#.....#.#...#.....#.....#.#.......................#.....#.............#.#...#.#...#.#...#.#...#...#...#.#.#...#.....#...#...#...#
#####.###.#.#.#.#####.#.#.#####.#####.#.#####.#.###.###.#.#.#######.#.###.#####.#.###.###.#####.#.###.###.#.#.###.#.#.#####.#####.#.#####.###
#.....#...#.#.#.#...#.#.#.#...#.........................................#...#.#.....#.#.....#...#...#...#...#...#.#...#.#...#...#.#.......#.#
#.#####.#.#.#.#.#.#.#.#.#.###.#.###.#####.#.#####.###.###.#.#.#####.#.#.###.#.###.#.#.#####.#.#.###.###.#.#####.#####.#.#.###.#.#.#######.#.#
#.#.....#.............#.#...#.#...#.......#...#...#.#...#.#...#...#...#.#...#.#...................#.#.#.#.....#.....#.#.#...#.#...#.......#.#
#.#.#.#####.###.#######.###.#.###.#####.#####.#.###.###.#.#####.#####.#.#.###.#.#.#######.###.#####.#.#.#.###.###.###.#.###.#.#####.###.#.#.#
#.#.#.#.....#.#.......#...#.#...#.#...#...............................#.#.....#...........#...#.....#.#.........#...............#.....#.#...#
#.#.#.#.###.#.#.###.#.#.###.#.###.#.#.###.#.#.###.#.#.#######.#######.#.#####.#############.###.#####.###.###############.#.###.#######.#.#.#
#.#.#.#...#.#...#.#...#.....#.....#.................#.....#...#.......#.......#...........#...#...........#...#...........#.#.........#...#.#
#.#.#####.#.#.#.#.#.#.#############.###.#.#.#####.#.#####.#.#######.#.#########.#########.###.###########.#.###.#########.#.#.#######.#.#.###
#.........#.......#.#.....#.......#.#.#...#.............#.........#.#.#.......#...#.......#.#...........#...#...#.........#.#.#...#.#.#.#...#
#.#.#######.###.###.#####.#.#####.#.#.###.#######.###############.#.#.#.###.#.###.#.#######.#.###.###.#####.#.###.#######.#.#.#.#.#.#.###.#.#
#.#.........#.....#.#...#.#...#.....#...#.......#.#...........#.....#...#...#.#...#.#.......#...#...#.......#...#...........#.#.#...........#
#.#########.#.###.#.#.#.#.###.#.#####.#########.#.#.#########.#.#######.#.###.#.###.#.###.#####.###.###########.#############.#.#.#######.#.#
#...........#...#...#.#.#...#.#.#.................#.#.......#.#.......#.#...#...#.#...#...#...#...#.#.......#.#...#...#.......#.#.....#.#...#
#.#.#######.#.#.#####.#.###.#.#.#.#################.#.###.#.#.#######.#####.#####.#####.###.#.###.#.#####.#.#.###.###.#.#######.#####.#.#.###
#.#.#.......#.#...#...#.......#.#.#.............#...#...#.#.#...#...#...#...#.........#.#.#.#.....#.....#...#...#...#.........#.#.#...#.....#
#.#.#####.#.#.###.#.###########.#.#.#####.#####.#.#######.#####.###.###.#.###########.#.#.#.###########.#.#.#.#.###.#######.###.#.#.#.###.###
#.#.....#.#.....#.#.#.#.......#...#.#...#.#.....#.......#.........#.......#.....#.....#.#.#...........#...#...#...#...#...#.#...#.#.#.#.....#
#.#####.#.#.#.#.#.#.#.#.#####.###.###.#.###.###.#######.#########.#########.###.#.#####.#.###########.#######.#######.#.###.#.###.#.#.#.###.#
#.......#...#...#.#...#.....#...#.....#.#...#.....#.#...#.....#.#.#.......#.#...#.......#.....#.#.......#.....#.......#.....#.#...#.#.#.....#
###########.###.#.###.#####.###.#######.#.#######.#.#.###.###.#.#.#.#####.#.#.###.#.#####.#.#.#.#.#####.#.#####.#.#####.#####.#.###.###.#.#.#
#.....#...#...#.#...#.#.....#...#.....#.#.....#...#.#.......#.#...#.#...#...#.#...#.#.....#.....#.....#.#.....#.#.#...#.....#.#.#...#...#.#.#
#.###.#.#.###.#####.#.#.#####.###.#.#.#.#.###.#.###.#########.#.###.#.#######.#.#.#.#####.#.#########.#.#####.#.###.#.#####.#.#.#.###.###.#.#
#...#...#...#.....#.#...#.#...#.#.#.#...#.#.#.#.......#.......#.#...#.#.......#.#.#...#...#.#...#.....#.#.....#.#...#.....#.#...#.........#.#
###.#######.#####.#.###.#.#.###.#.#.#.###.#.#.#########.#######.#.###.#.#######.#.###.#.#####.#.#.#####.#.#####.#.#######.#####.###########.#
#.#.#.....#.....#.#...#...#.#.....#.#.#.....#.....#...#.#.........#...#...#.....#.....#.#.....#.#.....#.#.#...#.#.#.....#.....#.#.....#.....#
#.#.###.#.###.###.###.###.#.#######.#.###########.#.#.#.#############.###.#.#####.#####.#.#.###.#####.###.#.#.#.#.#.###.#.###.#.#.###.#.###.#
#.#...#.#...#...#...#.....#.......#.#.........#...#.#...#...........#...#.#...#.....#...#...........#.....#.#.#.#.#.#.#.#.#...#.#...#.#.....#
#.###.#.#######.###.#############.#.#########.#.###.###.#.#########.###.#.###.#.###.###.#.#.#.#####.#.#####.#.#.#.#.#.#.###.###.###.###.#.#.#
#.....#.......#...#.....#.....#...#.#.......#.#...#...#.#.........#...#.#...#...#.#.....#.#.#.....#.#.#.....#.#...#.#.#.#...#...#...#...#...#
#.#####.#####.###.#####.#.###.#.###.#.###.#.#.###.###.#.#########.###.#.###.#####.#####.#.#.#.###.#.#.#.###.#######.#.#.#.#.#.###.###.###.###
#...#.........#.#.....#.#.#.#.#.#...#.#.#.#.#...#...#.#.#.......#.#.#.#.........#.......#...#.....#.#.#...#.........#.#.#.#.#.#.....#.#.#.#.#
###.###.#####.#.###.#.#.#.#.#.#.#.#.#.#.#.#####.#.###.###.###.###.#.#.#########.#.###########.#####.#.#.###.#.#######.#.#.#.#.#####.#.#.#.#.#
#.#.....#...#.....#.#.#.#.#...#...#.#.#.#.#.....#...#.......#...#.#.#.....#...#.#.#...........#.....#.#.#...#.#.........#.#.#.....#.#.#.....#
#.#####.#.#.#####.#.#.#.#.#.###.###.#.#.#.#.###.###.#######.###.#.#.#.###.#.#.#.#.#.###########.###.#.###.#.#.#.#####.###.#.#####.#.#.#######
#.........#.......#.#.#.#.#.#.....#.#.#.#...#.....#.....#.....#.........#.#.#...#.#.#...#.....#.#.....#...#.#.#.#.#...#...#.....#.#.........#
#.#####.###########.#.#.#.#.#####.#.#.#.#.###.###.#.###.###.#.###########.#.#######.#.#.#.#.###.###.###.###.#.#.#.#.#.#.#.#####.#.#.#######.#
#.....#.......#...#.#.#.#.#...#...#.#.......#.#...#.......#.#.............#.#.....#.#.#.#.#...#...#...#.#...#.#.#...#...#.....#.#.#.......#.#
###.#.#.#######.#.#.#.#.#.###.#.###.#.#.###.#.#.#####.###.###.#.###########.#.###.#.###.#.###.###.###.#.#####.#.#####.###.###.###.#####.###.#
#...#.#...#.....#.#.#.#...#.#...#...#...#.#.#.#.....#...#...#.#.#.......#...#...#...#...#.#.#...#.#.....#.....#.#.......#...#...........#...#
#.#.#.#.#.#.#####.#.#######.#####.#.#####.#.#.#####.###.###.#.#.###.###.#.###.#.#.###.###.#.###.#.#######.#####.#.###.#.###.#############.###
#.#...#.#.#.#...#.#.........#...#.#.......#...#...#...#...#...#.#...#...#.#...#...#.#.....#...#.#...#.....#.....#.#...#.#.....#...#.....#...#
#.#######.#.#.###.###.#####.#.#.#.#.#####.#######.###.###.###.#.#.#####.#.###.###.#.#.#######.#.###.#.#####.#####.#.#.#.#.#####.#.#.###.###.#
#.#.......#.#.#...#...#...#.#.#.........#.........#...#...#...#.#.....#.#...#.#...#.....#...#.#.....#.#...#.#.....#.#...#...#...#...#.#...#.#
#.#.#####.#.#.#.###.#.#.#.###.#############.###.###.###.#.#####.#.###.#####.#.#.###.###.#.#.#.#######.#.#.#.#.#.###.#######.#.#######.###.#.#
#...#.....#.#.......#.#.#.....#...#...#...#...#.#...#...#.#.....#.#.#.......#.#...#...#...#...#.....#.#...#...#...#.#.....#.#...#.#.......#.#
#.#######.#.#.#########.#######.###.#.#.#.###.#.#.#####.#.#.#####.#.#############.#.#########.#.###.#.###.###.###.#.#.###.#####.#.#.#######.#
#.#.....#.#...#.........#...#...#...#...#.....#.#.......#.#.#...#.........#.......#.........#.#...#.#...#...#.....#...#.#...#...#.#.........#
#.#.###.#.###.#.#########.#.###.#.###.#########.#########.#.#.#.#.#######.#.#.#######.#####.#.#.#.#.###.#.#############.###.#.###.#.#########
#.#.#.#.#...#.#.#...#.........#.#.#...#.......#.......#...#...#.#...#...#...#.#.......#.#...#.#.#.#.#...#...........#.....#.#.#.....#.....#.#
#.#.#.#.#####.#.#.#.#.#######.#.#.#####.#####.#####.###.###.#.#.###.#.#.#.###.#.#######.#.###.###.#.#.#####.###.###.#.#.###.#.#######.###.#.#
#.#.#.........#...#.#...#.#...#.#.....#...#...#...#.#...#.#.#.#...#.....#.#...#...#.........#.#...#...#...#...#...#...#.#...#.........#...#.#
#.#.#########.#####.#.#.#.#.###.#####.#.###.#.#.#.###.###.#.#.#########.#.#.###.#.#####.#####.#.#######.#.#######.#######.###.#########.###.#
#.#...............#.#.#.#...#...#...#...#...#...#.........#.#...........#.#.#.........#.#...#...#...#...#.#.....#.#.......#.............#...#
#.###########.#.#.#.###.#.###.#.#.#.#####.###.#############.#.#######.#.###.#.#######.###.#.###.#.#.#.###.#.###.#.#.#################.#.#.###
#.#...#.......#.#.#.....#.....#.#.#.....#.#...#.#.....#.....#.#.....#...#...#.#.....#.....#...#...#.#...#...#.....#...#.........#...#.#.#...#
#.#.#.#.#####.#.###.###########.#.#####.#.#.###.#.###.#.#####.###.#.#.#.#.###.#.###.###.###.###.#.#.###.#####.#######.#####.###.###.#.#.#.#.#
#.#.#.....#...#.....#.......#...#.....#.#.#.#.......#.#.#...#.....#.#.#...#...#.......#...#.....#.#.....#.......#...#...#...................#
#.#.#######.#####.###.#####.###.#.###.#.#.#.###.#####.#.#.#.#########.#####.#####.###.###########.###############.#.###.#.#######.#.###.###.#
#.........#.........#.....#.....#.#...#...#.......#...#.#.#.........#.....#.#...#...#.#.....#.....#...#...........#...#.#.....#.#.#.........#
#########.#########.#.###.#####.###.#####.#######.#.###.#.#########.###.#.#.#.#.#.#.#.#.###.#.#####.#.#.#.#.###.###.#.#.###.#.#.#.###.###.#.#
#...#...#...............#...#.#.....#...#.#.....#...#...#...#.....#...#.#...#.#.#.#.#.....#.#.....#.#...#.......#...#.#...#.#.#.#.....#...#.#
#.#.#.#.#####.#########.###.#.#######.#.#.#.###.###.#.#.###.#####.###.#.#####.#.#.#.#####.#.#.###.#.#############.###.###.#.#.#.#######.###.#
#.#...#...#.........#.....#.#.........#...#...#...#.#.#...#.......#...#.......#.#.#...#.....#...#...#...#.#.......#.#...#.#.#.#.........#.#.#
#.#######.#####.###.#.#####.#.#####.#.#######.#.###.#.###.#####.###.###.#.###.###.###.#.#######.#####.#.#.#.#######.#.#.#.###.#######.#.#.#.#
#.......#.....#...#.#.#...#.#...#...#.....#.#.......#...#.#.........#...#...#.#...#...#.#...#.....#...#...#.#.#.....#...#.....#.....#.#.#...#
#######.#####.###.#.###.#.#.#.#.#######.#.#.#.#########.###.#.###.#######.#.###.###.#.#.#.#.#####.#.###.###.#.#.###.###.#######.###.#.#.#.###
#.....#...#...#...#.....#.#.#.#.#.......#...#.#.........#...#...#.......#.#.#...#...#...#.#...#.....#.......#.#.#.#.#...#...#.....#.....#...#
#.###.###.#.###.#.#####.#.#.#.#.#.#####.###.#.#####.#.#.#.###.#.#########.#.#.#.#.###.#.#.###.#######.###.###.#.#.#.#.###.#.#.###.###.#####.#
#...#.....#.....#.#...#.#...#.#.#...#.....#.#.........#.#.#...#...........#...#.......#...#.......#...#...#.....#.#.......#.#...#...#.......#
#.#.###########.###.#.#.#####.#.###.#.#####.#########.#.#.###.#.###############.###########.#####.#.###.#.#####.#.#####.#.#####.###.#.#.#####
#...#...#...#.#.#...#.#.....#.#.....#.....#.......#...#.#.#...#.#.......#.........#.........#...#.#...#.#.#...#.....#.#.#.#.....#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#.#.###.#.###########.#######.#.###.#.#.###.#.#.###.#.###.#.#.#.#####.#.#.###.#####.#.#.#.#####.#.#.#.#.#####.###.#.#.#.#
#.#...#...#.#...#...#.#...#.........#...#.....#...#.#.#...#...#.#.#...#.#.#...#.#.#.#.#...#.#.....#.....#...#.#...#.#...#.#...............#.#
#.#########.#.#####.#.#############.###.#####.#.###.#.#######.###.###.#.#.#.###.#.#.#.#.###.#.#.###.#######.#.#.#.#.#####.###.#.#.#.#.#.#.#.#
#.....#.#...#.....#.#.........#...#.....#...#...#.#.#.......#.....#...#...#.#...#.#...#.#.#.#.#...#.........#...#.#.....#...#...#.#.#.#.#.#.#
#####.#.#.#########.#########.#.#.#####.#.#.#####.#.###.#.#.#######.#######.#.###.###.#.#.#.#.###.#.###.#########.#.###.#.#######.#.#.###.#.#
#...#.#.#.....#...#...#.....#...#.#.#...#.#.......#.....#.#.........#...#...#.#.....#.#.#.....#...#.......#.#...#.....#...#.........#.....#.#
###.#.#.#####.#.#.###.#####.#####.#.#.###.###.#######.#.#.###########.#.#.#.#.#.#####.#.#######.#########.#.#.#.#####.#####.#######.#######.#
#...#.....#.#.#.#.....#.....#.....#.#...#...#.......#.#.#.........#...#...#.#.#.......#...#...#.#.......#.#...#.#...#.......#.....#.#.....#.#
#.#######.#.#.#.#######.###.#.#####.###.###.#######.#.###.#######.#.#.#######.###########.#.#.#.#.#.#.#.#.#####.#.#.#.#######.###.#.#####.#.#
#.....#.#...#.#.....#...#.#.#...#...#...#.....#...#.#...#.........#.#.......#.#.......#.#.#.#.#...#.#.#.#...#...#.#.#.......#...#.#.......#.#
#.#.#.#.###.#.#.###.#.###.#.###.#.#.#.#########.#.#.#.#.#####.#.###########.#.#.#####.#.#.#.#.#####.#.#####.#.###.#.###.###.###.#.#########.#
#...#.....#.......#.#...#...#.#.#.#.#.#.........#...#.#.#.....#.#.........#.#.#...#.....#...#.....#.#...#.....#...#.#.......#.#.#.......#...#
###.#####.#.#####.#.#.#.#.###.#.###.#.#.###########.#.#.###.###.#.#.#####.#.#.#.#.#.###########.#.#.#.#.#.#####.###.#####.###.#.#######.#.###
#...#.....#...#.#...#.#.#...#.#...#.....#.........#...#...#.#...#.#.#...#.#.#.#.#.....#...#.....#.#.#.#...#...#.#.......#.....#.#.#...#.#...#
#.###.#######.#.#####.#.###.#.###.#.#####.#.#########.###.###.###.#.#.#.#.#.#.#.#.#####.#.#.###.###.#.#.###.#.#.#####.#.#####.#.#.#.#.#.###.#
#.#.....#...#...#.....#...#.....#...#...#.#.#.........#...#...#...#.#.#.....#.#.#.......#.#...#.#...#...#...#.#.......#.....#.#.#.#.#.#.....#
#.#####.###.###.#.#.#.###.#.#######.#.#.#.#.#.#####.###.#.#.###.###.###.#####.#.#########.###.#.#.#####.#.###.#.#.###.#####.###.#.#.#.#.#.###
#...#.........#.#...#.....#.#.......#.#.#.#...#.........#...#.#...#...#.#.....#.....#.......#.#.#.#.....#.#.#.#.#.....#...#.....#...#...#...#
#.#.###.#######.#.#######.###.#######.#.#.#########.#########.#.#.###.#.#.#####.#####.###.###.#.#.#.#.###.#.#.###.#####.#.#.#####.#########.#
#.#...#.#.....#...#.......#...#.......#.#...#.....#.........#...#...#.#.#.......#.....#...#...#.#.#.....#.#.#.#...#.....#...#...#...#.......#
#.###.###.###.#####.#.#####.###.#######.###.#.#.#.###.###.#.#.###.###.#########.#.#####.###.#####.#####.#.#.#.#.###.###.#####.#.###.#.#.#####
#...#.....#.......#.#.....#...#.#.....#.#.#.#.#.#...#.#...#.#...#...#.....#...#...#...#.#.#.#...#.....#.#.#...#.#...#...#.....#.#...#...#...#
#.#.#######.#.#.#.#.#####.###.#.###.#.#.#.#.###.###.###.###.###.###.###.###.#.#####.###.#.#.#.#.#####.###.#.###.#.#####.#.#####.###.#.#.#.#.#
#.#...#.....#...#...#...#.#.#.#.....#.#.#.#.....#.#...#.#.....#...#...#.....#.............#...#.....#...#.#.....#.......#.#...#...#.#.#...#.#
#.###.#.#####.#####.#.###.#.#.#.###.###.#.#######.###.#.#########.#.#.###########.#.###############.###.#.###############.###.###.#.#####.#.#
#...#.#.#.........#.#...#...#.#.#...#...#...........#.......#.....#.#...........#...#.#.............#...#...........#...#.#.....#.#.....#.#.#
#.#.#.#.#####.###.#.#.#.###.#.#.#.#.#.#.###.#.#.#####.#####.#.#####.#########.#######.#.#####.#######.#####.#######.#.#.#.#.#####.#####.###.#
#.#.#.#.....#.#...#.#.#.#...#...#.#...#.#...#.#.....#.......#...#.........#...........#...#...........#...#.#.#.....#.#.....#...#.....#.....#
#.#.#.#####.#.#.#.#.#.#.#.###.###.#####.#.#.#.#####.#####.#####.#####.#.#.#.#.#.###.#####.#####.#######.#.#.#.#.#.###.#######.#.#.###.#####.#
#.#.#...#...#.#.#.#.#.#.#...#...#...#.#.#.#.#.....#...#...#.......#...#.#.#.#.#.#.#.....#.......#.......#.#.#.#...#...#.#.....#.#.#...#...#.#
#.#.###.#.#.#.#.###.###.#.#.#.#####.#.#.#.#.#####.#.###.###.#.###.#.#####.#.#.#.#.#####.#############.###.#.#.###.#.###.#.#####.#.#.###.#.#.#
#.#.....#...#.#...#.#.....#...#.....#...#.#...#...#.....#...#.#...#.#.....#.#.#.......#.......#.......#.#.#.....#...#...#.....#.#.#.....#.#.#
#.#########.#.###.#.#.#######.#.#####.#.#.###.###.#######.###.#.###.###.#.#.###.#########.###.#.#.#####.#.#####.#####.#.#####.#.#####.#.#.#.#
#.#.#.......#.#...#.#.....#...#.#.#...#.#...#...#.....#...#...#.#.......#.#.............#...#...#.#...#.......#.#.....#.....#.#.....#.#.#.#.#
#.#.#.#####.#.#.###.#####.#.###.#.#.###.###.###.###.###.###.###.###.#####.#######.#.###.#.#######.#.#.#######.#.#.#######.###.#####.###.#.#.#
#...#.....#...#...#.....#.#.#...#.........#.#.#.....#...#...#...#...#...........#...#.#.#.#.....#...#.....#.#.#...#.......#...#...#.#...#.#.#
#.#.#####.#.#.#.#.#####.#.#.#.#.#.#######.#.#.###.###.###.###.###.#.#####.#.###.###.#.#.#.#.###.#########.#.#.#.###.#.#.###.#####.#.#.###.#.#
#...#...#.#.....#.....#.#.#...#.#.#...#...#.#...#.......#...#.....#.....#...#...#...#.#.#.#.#.#...#.....#.#.......#.#...#...#.....#.#.#.#...#
#.#####.#.###.#.###.#.#.#.###.#.###.#.###.#.###.#######.###.###########.#####.#.#.###.#.#.#.#.###.#.###.#.#.###.#.#.#####.#####.#.#.#.#.#.###
#.....#.#.#...#.#...#.#.#...#.#.#...#...#.#...#...#...#.#...#.........#...#.#.#...#...#.#.#.#...#...#...#.#.....#.#.#.#...#.....#.#...#.#...#
#.###.#.#.#.#.###.#.#.#.#.#.#.#.#.#####.#.###.#.###.#.###.#.#.#######.###.#.#.#.###.#.#.###.#.#.#####.###.#######.#.#.#.###.#.#########.###.#
#...#.#.#.......#.#...#.#.#.#.#.#...#.#.#...#...#...#...#.....#.....#.#.#.#...#.#...#.#.#...#.#.....#...#.......#.#.#.#...#.#.#.......#...#.#
#.#.#.#.#####.#.#.#####.#.###.#.###.#.#.#####.###.#####.#.#####.###.#.#.#.#.#.#.#.#####.#.###.#####.###.#.#####.#.#.#.###.###.#.###.#.#.#.#.#
#.#.#.#.#.....#.#.#...#...#...#.......#.......#...#...#.#.....#.#...#...#.#.#.#.#.....#...#.#.#...#...#.#.#.#...#.#...#.#...#.....#.#.#.#.#.#
#.#.#.#.#.###.#.#.#.#.#.###.###################.#####.#.#####.#.#.#######.#.#.#.#####.#####.#.#.#.#.###.#.#.#.###.###.#.###.#######.#.#.###.#
#...#...#.#.....#...#.......#.......#...........#.....#.......#.#.#...#...#.#.#.#...#.......#.#.#.#.....#...#.#.#...#...#...#.......#.#...#.#
#.#####.#.#.#######.#.###.#########.#.###########.#.#.###.#.###.#.#.#.#.###.#.#.#.#.#####.###.#.#############.#.###.#.###.###.#####.#.###.#.#
#...#...#.#.#.......#.#...#.........#...#.............#.....#...#.#.#...#...#.#.#.#.....#.....#.#.....#.......#.....#.#...#...#...#...#...#.#
#.#.#.#.#.###.#####.###.#####.###.#.###.#.#######.#.###.#####.###.#.#####.###.#.#.#####.#.#####.#.#.#.###.#####.#######.###.#.#.#.#.###.#.#.#
#...#...#.........#...#.#.....#.#.#...#.#...#...#.#...#...#...#...#.#.#...#...#...#.....#.#.....#.#.#...#...#.#.#.......#...#...#.......#.#.#
#.#####.#########.#.#.#.###.###.#.#.#.#.###.#.#.#.#.#####.#.###.###.#.#.#.#.#######.#####.###.###.#.###.###.#.#.#.#####.###.#.#.###.###.###.#
#.#.......#.....#...#.#.....#...#...#.#...#.#.#.#.#.#.....#.#.#...................#...#.#...#.#...#.#.......#.#...#.........#.#.............#
#.#.#######.#.#.#.###.#######.#.#####.###.#.###.#.###.#####.#.#.#.###.###.#.#.#######.#.###.#.#.###.#########.#####.#####.###.#.#.#.#####.###
#.#...#...#.#.#.........#.....#.....#.................#.....#.................#.....#.#.....#.........................................#.#...#
#.#.###.#.#.#.###.#####.#.#.#######.###.#.#.###########.#####.#.#.#.#.#.#.#.#.#.###.#.###.###.#######.#.#.#####.#.#.#.#.###.#.#.#.#.#.#.###.#
#...#...#...#...............#.....#...#.#.#.#...........#.....#.#.#.#.#...#.#.#...#.#...................#.....#.#.#...#.....#...#.#.#...#.#.#
#.###.#######.###.#####.#.#####.#####.#.#.#.#.###############.#.#.#.#.#.###.#.###.#.#.#.###.#####.#.#########.###.###.#######.#.#.#.###.#.#.#
#.....#...#...#.#.....#.....................#.#.............#.#.#.#...#.#.......#.#.#.#.#...#.....#...........#.....#...#.......#.#.......#.#
#.#####.#.#.#.#.#.###.###.###.#########.#.###.#####.#######.#.#.#.#.###.#.#.#####.#.#.#.#.###.#.#.#############.#######.#####.#.#.#.#######.#
#...#...#.#.....#.#.#...#.#.#...#.....#.#...#.#...#.....#.#.#.#...#...#...#.................................#.........#.#...........#.......#
#.#.#.###.#.#.###.#.###.#.#.###.#.###.#.###.#.#.#.#####.#.#.#.#########.###.#######.#.#.###.#.#####.#.#####.#.#####.###.#.#.#.#.#.###.#######
#...#.#.#.#.#...#...#.#.#.#.#...#.#.#.#...#.....#...#...#.#...#.......#...#.#.....#.#.#.#.#...#.....#...#.#.#.....#.....#.#...#.#.#...#.....#
#.###.#.#.###.#.#.#.#.#.#.#.#.###.#.#.###.#####.###.#.###.###.#####.#.#.#.#.#.###.#.###.#.#####.#######.#.#.#####.#######.###.#.###.#######.#
#S......#.....#.......#.....#.......#...........#...................#...#...#...#.......#.................#...............#...#.............#
#############################################################################################################################################"""

tdata = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

# tdata= """#################
# #...#...#...#..E#
# #.#.#.#.#.#.#.#.#
# #.#.#.#...#...#.#
# #.#.#.#.###.#.#.#
# #...#.#.#.....#.#
# #.#.#.#.#.#####.#
# #.#...#.#.#.....#
# #.#.#####.#.###.#
# #.#.#.......#...#
# #.#.###.#####.###
# #.#.#...#.....#.#
# #.#.#.#####.###.#
# #.#.#.........#.#
# #.#.#.#########.#
# #S#.............#
# #################"""

import sys

sys.setrecursionlimit(10000)

north = (-1, 0)
south = (1, 0)
west = (0, -1)
east = (0, 1)

compass = (north, east, south, west)
clockwise = {
    north: east,
    south: west,
    east: south,
    west: north
}
anti_clockwise = {
    north: west,
    south: east,
    east: north,
    west: south
}


def draw(grid, n_rows, n_cols, pts):
    for r in range(n_rows):
        for c in range(n_cols):
            if (r, c) in pts:
                print('^', end='')
            else:
                print(grid[r][c], end='')
        print()
    print()


def find_start(grid, n_rows, n_cols):
    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] == 'S':
                return r, c
    return None


def both_parts_recursive(data: str, _debug: bool = False):
    grid = list(line for line in data.splitlines())
    n_rows = len(grid)
    n_cols = len(grid[0])
    start_r, start_c = find_start(grid, n_rows, n_cols)

    if _debug:
        print('Grid size:', n_rows, n_cols, 'Start at:', start_r, start_c)

    if _debug:
        draw(grid, n_rows, n_cols, [])

    success = []
    min_score = [float('inf')]
    score_cache = {}

    def search(r, c, direction, route, score):
        if (r, c) in route: return
        if grid[r][c] == '#': return

        if (r, c, direction) in score_cache and score > score_cache[(r, c, direction)]:
            return
        score_cache[(r, c, direction)] = score

        if score > min_score[0]: return
        route = route + [(r, c)]

        if grid[r][c] == 'E':
            success.append((score, route))
            min_score[0] = min(min_score[0], score)
            # print('found route pts=', len(route), 'score=', score)
            return

        nr, nc = r + direction[0], c + direction[1]
        search(nr, nc, direction, route, score + 1)

        clock = clockwise[direction]
        nr, nc = r + clock[0], c + clock[1]
        search(nr, nc, clock, route, score + 1000 + 1)

        anti = anti_clockwise[direction]
        nr, nc = r + anti[0], c + anti[1]
        search(nr, nc, anti, route, score + 1000 + 1)

    search(start_r, start_c, east, [], 0)

    print('Num routes:', len(success), sorted(success)[0])
    print('Min score: ', min_score[0])
    print('Unique points', len({point for score, points in success if score == min_score[0] for point in points}))


def both_parts(data: str, _debug: bool = False):
    grid = list(line for line in data.splitlines())
    n_rows, n_cols = len(grid), len(grid[0])

    success = []
    min_score = float('inf')
    score_cache = {}

    q = [(*find_start(grid, n_rows, n_cols), 1, [], 0)]

    while q:
        r, c, d, route, score = q.pop()

        if ((r, c) in route or
            grid[r][c] == '#' or
            score > score_cache.get((r, c, d), float('inf')) or
            score > min_score
        ): continue

        score_cache[(r, c, d)] = score
        route = route + [(r, c)]

        if grid[r][c] == 'E':
            success.append((score, route))
            min_score = min(min_score, score)
            print('.', end='')
            if len(success) % 20 == 0:
                print()
            continue

        q.insert(0, (r + compass[d][0], c + compass[d][1], d, route, score + 1))
        q.insert(0, (r + compass[(d+1) % 4][0],c +  compass[(d+1) % 4][1], (d+1) % 4, route, score + 1000 + 1))
        q.insert(0, (r + compass[(d+3) % 4][0], c + compass[(d+3) % 4][1], (d+3) % 4, route, score + 1000 + 1))

    print()
    print('Num routes:', len(success))
    print('Min score: ', min_score)
    print('Unique points:', len({point for score, points in success if score == min_score for point in points}))


def main():
    import timeit

    def run(msg, data, fn, debug):
        if data:
            print(f'*** {msg:13} ---------------')
            start = timeit.default_timer()
            fn(data, debug)
            elapsed_ms = (timeit.default_timer() - start) * 1000
            print(f'Time {elapsed_ms:.10f} ms ------------')

    # run("Both", tdata, both_parts_recursive, False)
    # run("Both", pdata, both_parts_recursive, False)
    run("Both", tdata, both_parts, False)
    run("Both", pdata, both_parts, False)


if __name__ == '__main__':
    main()
