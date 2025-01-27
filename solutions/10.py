from collections import defaultdict


def move(grid, row, col):
    """
    Return a list of valid new locations to move from current location
    Empty list means no valid moves
    """
    val = grid[row][col]
    targetVal = val + 1
    ans = []

    # up
    if row > 0 and grid[row - 1][col] == targetVal:
        ans.append([row - 1, col])

    # down
    if row < len(grid) - 1 and grid[row + 1][col] == targetVal:
        ans.append([row + 1, col])

    # left
    if col > 0 and grid[row][col - 1] == targetVal:
        ans.append([row, col - 1])

    # right
    if col < len(grid[0]) - 1 and grid[row][col + 1] == targetVal:
        ans.append([row, col + 1])

    return ans


def search(grid, startRow, startCol, seen, locs, target=9):
    """
    starting from location at end of path, return number of reachable 9's.
    Then add all locations from path to seen so we don't have to compute again.
    seen is {(row, col): # of reachable 9's for this location}.
    locs is {(row, col): set of locations of reachable 9's for this location}
    Paths may branch.
    """

    if grid[startRow][startCol] == target:
        seen[(startRow, startCol)] = 1
        locs[(startRow, startCol)].add((startRow, startCol))
        return 1

    if (startRow, startCol) in seen:
        return seen[(startRow, startCol)]

    for row, col in move(grid, startRow, startCol):
        search(grid, row, col, seen, locs)  # branch
        locs[(startRow, startCol)].update(locs[(row, col)])

    score = len(locs[(startRow, startCol)])
    seen[(startRow, startCol)] = score
    return score


def search2(grid, startRow, startCol, seen, target=9):

    if grid[startRow][startCol] == target:
        seen[(startRow, startCol)] = 1
        return 1

    if (startRow, startCol) in seen:
        return seen[(startRow, startCol)]

    for row, col in move(grid, startRow, startCol):
        seen[(startRow, startCol)] += search2(grid, row, col, seen)
    return seen[(startRow, startCol)]


def solution1(inp):
    ans = 0
    inp = [list([int(y) for y in x]) for x in inp.split("\n")]
    starts = []

    for row, rowContent in enumerate(inp):
        for col, val in enumerate(rowContent):
            if val == 0:
                starts.append([row, col])

    seen = defaultdict(int)
    locs = defaultdict(set)
    for startRow, startCol in starts:
        ans += search(inp, startRow, startCol, seen, locs)
    return ans


def solution2(inp):
    ans = 0
    inp = [list([int(y) for y in x]) for x in inp.split("\n")]
    starts = []

    for row, rowContent in enumerate(inp):
        for col, val in enumerate(rowContent):
            if val == 0:
                starts.append([row, col])

    seen = defaultdict(int)
    for startRow, startCol in starts:
        ans += search2(inp, startRow, startCol, seen)
    return ans


testinput = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732\
"""

input = """\
3212345678121056780310106543218765210109876
7301106769012349891210237858909650987212345
8943219878734217894354345997434501896398730
7654306765025606765969876786521432345485621
1233456834110715610870945431010676541014678
0321067923230894320101234894321289239823549
7450478810301129831230128765045658178101630
8964329234532034761945219652136789017652721
7875012187645695610876106543221054787243890
4976701094556786921065987233234565692104323
3289898763216547836976856100149874563495414
4122305603407436545885445765454703454386901
5001414512518921056794039870363212325677842
6980523347676545121603128981278101210543234
7879601258989236730512789974329892105601100
0968708769076107845676697865012783416782321
1651219940145045912389546521323676545699450
2340367831231236705489030430654541236598769
4565456328900987876018121046543010167894378
3678995417811432980127630198672187098765298
2980987606321501676534548767981096523030167
1011876545450650101456759854102345614123454
9872345034968763212321876543201298705323456
8960101123879454789410989812120398676311237
1051211012567345673508989401032367985200398
2340349873498212232679876501001456810123478
1232456780341000141089845432132345210194569
0541542191232567657897894012201106761087654
5670233088943498766501703025672239872398743
4589104567652567898432612134984346765489232
5498010988961043765430543210789655159896101
4321023870870152896321432323658705014765012
2349834561431161067816521874503216723454101
1056767652521078154907890963212345894323221
0148988943652189143878903454503454513411230
3297803456789321012363212367696543201500549
4586912369878934101454201008987012102676678
5675001078767765210323123412108991343989654
6784100981059874349014056503234780256978703
7693201452342103458005347854345650107869012
8543542367033012567176218961259654398054327
9232632198124988943287307870568765212167898
0101789087235677656896478969876890103456787\
"""

if __name__ == "__main__":
    ans1 = solution1(input)
    print(ans1)

    ans2 = solution2(input)
    print(ans2)
