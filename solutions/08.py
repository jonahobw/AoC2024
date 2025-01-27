from collections import defaultdict


def parseInput(inp):
    inp = inp.split("\n")
    return inp


def solution1(inp):
    inp = parseInput(inp)
    validIdx = lambda row, col: 0 <= row < len(inp) and 0 <= col < len(inp[0])
    antennas = defaultdict(list)  # {freq: [locs with that frequency]}
    antinodes = set()  # locs of antinodes

    for row in range(len(inp)):
        for col in range(len(inp[row])):
            char = inp[row][col]
            if char != ".":
                if char in antennas:
                    for loc in antennas[char]:
                        dr = row - loc[0]
                        dc = col - loc[1]

                        newLoc = (dr + row, dc + col)
                        if validIdx(newLoc[0], newLoc[1]):
                            antinodes.add(newLoc)

                        newLoc = (loc[0] - dr, loc[1] - dc)
                        if validIdx(newLoc[0], newLoc[1]):
                            antinodes.add(newLoc)
                antennas[char].append((row, col))

    return len(antinodes)


def solution2(inp):
    inp = parseInput(inp)
    validIdx = lambda row, col: 0 <= row < len(inp) and 0 <= col < len(inp[0])
    antennas = defaultdict(list)  # {freq: [locs with that frequency]}
    antinodes = set()  # locs of antinodes

    for row in range(len(inp)):
        for col in range(len(inp[row])):
            char = inp[row][col]
            if char != ".":
                if char in antennas:
                    for loc in antennas[char]:
                        dr = row - loc[0]
                        dc = col - loc[1]

                        newLoc = (row, col)
                        while validIdx(newLoc[0], newLoc[1]):
                            antinodes.add(newLoc)
                            newLoc = (newLoc[0] + dr, newLoc[1] + dc)

                        newLoc = (loc[0], loc[1])
                        while validIdx(newLoc[0], newLoc[1]):
                            antinodes.add(newLoc)
                            newLoc = (newLoc[0] - dr, newLoc[1] - dc)
                antennas[char].append((row, col))

    return len(antinodes)


testinput = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............\
"""

input = """\
.....................................O..V.........
..................................................
................................O.........Z.......
....W....................................V....v...
........................m................8........
.....................................n........Z..v
.............F.....3...n....5m....................
................................................V.
................3............iv....Z.............V
...........................O..n..i........p......H
......W..6..............................i.........
......................................b...........
..................................n........p......
........M.......c...........m..5......1...........
...M............................L..5..A...........
...w...........9.............F5..................q
.W.....................................q....p.....
.......W........r.......H.....LA......q...........
................4.F....................A..........
........3.......a.....F...................A..L....
....ME...............................Q..........q.
.E..................ih...................Z........
................E...H...........h.................
.........m.........X..............................
..................0......C.................h......
.M......l.................Q.h.....................
..........C..............0........................
.............lX............3.c....................
......8.X.........c....r..a......H.....9..........
.................QE.....C.........................
..R................a........Q...................7.
...........................a......................
l..........X.R............1..I..........9.........
.................0R..............b.....z......x...
.......l.....w....r..........................b....
.8..........0...................P1z...............
.............c.........................L..........
.................C..N............o............9...
...........e..f..N................................
8.............................B...................
...........4...............................x......
....w....RY..........4.......................P....
.........yw.....Y.............o2...............7..
..6y........4..............fo..............7......
.........Y..6............o......................x.
.....Y....e.....y..I.r...........2................
....e.............................P.......z.bB....
.............6.................B........7......x..
..y.N........f...........1....I....z....B.........
.....e....f.............I.................2.......\
"""

if __name__ == "__main__":
    ans1 = solution1(input)
    print(ans1)

    ans2 = solution2(input)
    print(ans2)
