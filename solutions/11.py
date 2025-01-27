def howManyStones(initialVal, blinks):
    """
    If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
        The left half of the digits are engraved on the new left stone, and the right half of the digits are
        engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
    """

    if not isinstance(initialVal, list):
        stones = [initialVal]
    else:
        stones = initialVal

    for blink in range(blinks):
        print(blink)
        toAdd = []
        for i, num in enumerate(stones):
            if num == "0":
                stones[i] = "1"
            elif len(num) % 2 == 0:
                toAdd.append(str(int(num[: len(num) // 2])))
                stones[i] = str(int(num[len(num) // 2 :]))
            else:
                stones[i] = str(int(num) * 2024)
        stones.extend(toAdd)
    return len(stones)


def solution1(inp, blinks):
    inp = inp.split(" ")
    return howManyStones(inp, blinks)


def howManyStones2(num, blinks, seen):
    # This solution I did not come up with myself, I got it from here
    # https://www.youtube.com/watch?v=dfZ4uxqgT6o
    if seen is None:
        seen = {}
    if (num, blinks) in seen:
        return seen[(num, blinks)]
    if blinks == 0:
        ans = 1
    elif num == "0":
        ans = howManyStones2("1", blinks - 1, seen)
    elif len(num) % 2 == 0:
        ans = howManyStones2(
            str(int(num[: len(num) // 2])), blinks - 1, seen
        ) + howManyStones2(str(int(num[len(num) // 2 :])), blinks - 1, seen)
    else:
        ans = howManyStones2(str(int(num) * 2024), blinks - 1, seen)
    seen[(num, blinks)] = ans
    return ans


def solution2(inp, blinks):
    inp = inp.split(" ")
    seen = {}
    ans = 0
    for x in inp:
        ans += howManyStones2(x, blinks, seen)
    return ans


testinput = """\
125 17\
"""

input = """\
8435 234 928434 14 0 7 92446 8992692\
"""

if __name__ == "__main__":
    ans1 = solution1(input, 25)
    print(ans1)

    ans2 = solution2(input, 75)
    print(ans2)
