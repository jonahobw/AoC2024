from collections import defaultdict


def parseInput(inp):
    temp = inp.split("\n")
    inp = [list(x) for x in temp]
    return inp


def numPadAdj():
    """
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+
    """

    return {
        "7": {">": "8", "v": "4"},
        "8": {"<": "7", ">": "9", "v": "5"},
        "9": {"<": "8", "v": "6"},
        "4": {"^": "7", ">": "5", "v": "1"},
        "5": {"<": "4", ">": "6", "^": "8", "v": "2"},
        "6": {"<": "5", "^": "9", "v": "3"},
        "1": {"^": "4", ">": "2"},
        "2": {"<": "1", ">": "3", "^": "5", "v": "0"},
        "3": {"<": "2", "^": "6", "v": "A"},
        "0": {"^": "2", ">": "A"},
        "A": {"^": "3", "<": "0"},
    }


def arrowPadAdj():
    """
    +---+---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    """

    return {
        "^": {">": "A", "v": "v"},
        "A": {"<": "^", "v": ">"},
        "<": {">": "v"},
        "v": {"<": "<", "^": "^", ">": ">"},
        ">": {"<": "v", "^": "A"},
    }


def sortByBestDirection(chars):
    order_dict = {"<": 0, "v": 1, "^": 2, ">": 3}
    return sorted(chars, key=lambda char: order_dict.get(char, float("inf")))


def pathSearchInternal(adj, start, target, explored=[]):
    """
    get shortest sequence of presses to get from start to target on grid with
    adjacency map <adj>, of form {node: {"v": node, ...}}:
    """

    def numChanges(proposedPath):
        ans = 0
        for i in range(1, len(proposedPath)):
            if proposedPath[i - 1] != proposedPath[i]:
                ans += 1
        return ans

    if start in explored:
        return None
    if start == target:
        return [[]]

    minSeqLen = float("inf")
    changes = float("inf")
    minSeq = []
    neighbors = adj[start]
    for neighbor in neighbors.keys():
        paths = pathSearchInternal(adj, neighbors[neighbor], target, explored + [start])
        if paths is not None:
            for path in paths:
                path = [neighbor] + path
                chg = numChanges(path)
                if len(path) < minSeqLen:
                    minSeq = [path]
                    changes = chg
                    minSeqLen = len(path)
                elif len(path) == minSeqLen:
                    if chg < changes:
                        minSeq = [path]
                        changes = chg
                    elif chg == changes and path not in minSeq:
                        minSeq.append(path)

    if len(minSeq) > 0:
        return minSeq
    return None


def pathSearch(adj, start, target, seen):
    id = (start, target)
    if id in seen:
        return seen[id]
    paths = pathSearchInternal(adj, start, target)
    ans = paths[0]
    for path in paths:
        if sortByBestDirection(path) == path:
            ans = path
            break
    seen[(start, target)] = ans
    return ans


def findPressSeq(adj, start, code, seen, thisCache):
    if (start, tuple(code)) in thisCache:
        return thisCache[(start, tuple(code))]
    ans = []
    for letter in code:
        path = pathSearch(adj, start, letter, seen)
        ans.extend(path + ["A"])
        start = letter

    thisCache[(start, tuple(code))] = ans, start
    return ans, start


def solution1(inp):
    ans = 0
    inp = parseInput(inp)

    numPadSeen = {}
    arrowSeen = {}
    sequenceCache = {}
    numAdj = numPadAdj()
    arrowAdj = arrowPadAdj()
    r1Current = "A"
    r2Current = "A"
    r3Current = "A"

    for code in inp:
        r1pressPath, r1Current = findPressSeq(
            numAdj, r1Current, code, numPadSeen, sequenceCache
        )
        r2pressPath, r2Current = findPressSeq(
            arrowAdj, r2Current, r1pressPath, arrowSeen, sequenceCache
        )
        r3pressPath, r3Current = findPressSeq(
            arrowAdj, r3Current, r2pressPath, arrowSeen, sequenceCache
        )
        minPathLen = len(r3pressPath)
        print(code, minPathLen)
        factor = int("".join(code[:-1]))
        inc = factor * minPathLen
        ans += inc
    return ans


def splitByA(path):
    result = []
    subpath = []
    for char in path:
        subpath.append(char)
        if char == "A":
            result.append(subpath)
            subpath = []
    return result


def solution2(inp, level):
    inp = parseInput(inp)
    ans = 0

    numPadCache = {}
    arrowCache = {}
    arrowSeqCache = {}
    numAdj = numPadAdj()
    arrowAdj = arrowPadAdj()
    numPadCurrent = "A"
    numPadSeqCache = {}

    for code in inp:
        numPadPath, numPadCurrent = findPressSeq(
            numAdj, numPadCurrent, code, numPadCache, numPadSeqCache
        )
        freq = defaultdict(int)
        subPaths = splitByA(numPadPath)
        for pth in subPaths:
            freq[tuple(pth)] += 1

        for _ in range(level):
            newFreq = defaultdict(int)
            for subPath, count in freq.items():
                newSubPaths, _ = findPressSeq(
                    arrowAdj, "A", subPath, arrowCache, arrowSeqCache
                )
                newSubPaths = splitByA(newSubPaths)
                for newSubPath in newSubPaths:
                    newFreq[tuple(newSubPath)] += count
            freq = newFreq

        codeLen = 0
        for subPath, count in freq.items():
            codeLen += len(subPath) * count

        print(code, codeLen)
        factor = int("".join(code[:-1]))
        inc = factor * codeLen
        ans += inc
    return ans


testinput = """\
029A
980A
179A
456A
379A\
"""

input = """\
382A
463A
935A
279A
480A\
"""

if __name__ == "__main__":
    ans1 = solution1(input)
    print(ans1)

    ans2 = solution2(input, 25)
    print(ans2)
