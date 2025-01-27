import re


def parseStrCols(input):
    # Given: input string containing integers separated into 2 colunns.
    # Return: a 2d list of integers where each row is a column of the input.

    lines = input.split("\n")
    ans = [[], []]
    for line in lines:
        if len(line) > 0:
            nums = re.findall("\d+", line)
            ans[0].append(int(nums[0]))
            ans[1].append(int(nums[1]))
    return ans


def parseStrRows(input):
    # Given: input string containing integers separated by whitespace and newlines.
    # Return: a 2d list of integers where each row contains the rows of the input
    # as a list.

    lines = input.split("\n")
    ans = []
    for line in lines:
        if len(line) > 0:
            nums = re.findall("\d+", line)
            ans.append([int(x) for x in nums])
    return ans


def dirs():
    return [(1, 0), (0, -1), (-1, 0), (0, 1)]
