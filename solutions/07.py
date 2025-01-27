from collections import deque


def parseInput(inp):
    """
    Return a list of tuples:
    (left integer, list of right integers)
    """
    ans = []
    inp = inp.split("\n")
    for line in inp:
        line = line.split(": ")
        ans.append((int(line[0]), [int(x) for x in line[1].split(" ")]))
    return ans


class Node:
    def __init__(self, val, idx, ops=["+", "*"]):
        self.val = val
        self.idx = idx
        self.operations = ops
        self.children = []

    def createChildren(self, target, numbers):
        # return bool indicating if valid child found
        if self.idx == len(numbers) - 1:
            return self.val == target
        nextIdx = self.idx + 1
        for op in self.operations:
            if op == "*":
                nextval = self.val * numbers[nextIdx]
            if op == "+":
                nextval = self.val + numbers[nextIdx]
            if op == "||":
                nextval = int(str(self.val) + str(numbers[nextIdx]))
            child = Node(nextval, nextIdx, ops=self.operations)
            self.children.append(child)
        return False


def createTree(target, numbers, ops=["+", "*"]):
    current = Node(numbers[0], 0, ops=ops)
    valid = current.createChildren(target, numbers)
    toSearch = deque([current])

    while not valid and toSearch:
        current = toSearch.pop()
        valid = current.createChildren(target, numbers)
        toSearch.extend(current.children)
    return valid


def solution1(inp):
    inp = parseInput(inp)
    ans = 0

    for target, numbers in inp:
        # current node is cumulative value, last idx of numbers used in cumulative value
        # edges are operations, all nodes have the same edges except if idx is last, then
        # this is a leaf node
        # start from root node = numbers[0] and idx = 0
        # do a DFS
        if createTree(target, numbers):
            ans += target
    return ans


def solution2(inp):
    inp = parseInput(inp)
    ans = 0

    for i, (target, numbers) in enumerate(inp):
        # current node is cumulative value, last idx of numbers used in cumulative value
        # edges are operations, all nodes have the same edges except if idx is last, then
        # this is a leaf node
        # start from root node = numbers[0] and idx = 0
        # do a DFS
        print(f"{i}/{len(inp)}")
        if createTree(target, numbers, ops=["+", "*", "||"]):
            ans += target
    return ans


testinput = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20\
"""

input = """\
10274: 2 923 7 658 40 4 70
25816825: 3 1 838 9 3 6 2 53 95 4 5
18880346235: 59 5 8 1 8 3 462 35
386803: 6 1 1 65 7 76 356 10 7 6
169532496: 457 6 8 92 1 1 131 84
671: 4 6 1 5 546
6947: 34 253 5 63 611 7 185
3188884821: 938 909 1 44 85
9717885883: 7 9 37 57 4 5 746 7 306
948797635491: 7 7 4 98 9 8 664 7 49 9 9
302243: 14 384 7 7 5 4 8 5 718
24372240066: 6 1 2 89 7 2 3 1 692 4 66
58905: 37 425 1 846 45 1
915: 2 3 3 14
3457815537: 376 161 9 4 73 3 9 7 7 2
280173: 75 5 83 1 9 6 33
2183231472: 41 2 463 806 4 6 5 9 71
176256: 44 60 5 719 34
10054: 8 601 2 5 433
170131879263: 275 294 303 103 6 6
55282217865605: 5 464 871 1 242 480 2
24208233: 2 3 55 52 4 230
80626267: 3 318 2 8 249 69
356674: 5 7 884 397 962
8249306: 7 69 19 51 8 7 7 6 534 2
399468005: 65 5 6 4 779 6 5 9 542 2
1411: 9 8 260 993 87 2
343586887: 40 7 513 52 23 2 7
6363: 2 2 64 9 24
11065750: 5 22 4 2 5 662 88
1962072751: 9 66 5 671 4 330
715803712: 102 7 1 803 70 2 8
25202: 1 94 268 6 3
415525: 5 81 884 7 5 3 85 1 44
15876: 5 1 9 3 98
19497: 8 554 464 8 9 2 885
1405908: 13 3 8 68 3 342 755 7 9
966: 9 9 46 80 57
1947023027: 7 49 4 717 37 638 4 37
76309160: 9 4 2 7 958 1 1 5 28 2 8 4
30782013216: 32 1 3 1 53 7 479 2 770
82856866545: 9 285 921 9 66 3 34
29936583: 760 4 6 47 9 827 10
2113: 4 5 3 98 9 8 145 918 10
62042: 8 95 14 43 36
123796261: 8 9 63 2 2 9 4 7 404 53 8
197026459: 803 4 17 9 42 61
88686722: 1 819 9 8 201 49 527 1
15823848368: 30 93 8 9 9 8 7 4 7 599 5
2773892: 7 82 5 4 4 2 66 385 9 4 7
32568708: 7 6 9 319 6 6 242 9 45 3
1530: 85 24 9 6 423
6388837: 6 305 3 783 52 34
630825: 8 700 27 33
17671495149: 99 500 3 67 601 81 7 9
746845765851: 7 4 6 845 76 5 820 34
238574: 336 23 214 30 314
19007365480173: 8 80 4 8 7 91 53 2 739 7
3294: 36 6 9
47142: 4 3 3 8 3 3 8 57 4 860 1 4
17716: 13 66 6 6 20 274 7 2 33
161371308859: 87 49 4 9 5 506 9 9 2 79
4538235580: 9 10 762 2 7 1 5 80
756: 1 72 2 299 311 1
746064: 463 4 8 2 7 7 1 7 3 132
3568: 71 4 5
6440: 1 2 3 9 90 7 73 3 1 8 3 5
942417520: 8 3 9 407 268 5 8 8 816
11645128982: 2 91 5 641 8 1 4 8 3 398
308207697: 6 4 7 1 6 116 7 891 97 8
1181585194: 6 66 56 7 35 14 905
83722416: 37 9 5 499 21 1 40 2 9 2
60905947650906: 49 509 74 77 73 55 6 6
2379481825: 237 9 2 9 561 75 5 5
111198: 2 207 896 6 98
1349388288: 679 75 3 9 138 8 8
3796730516: 81 678 346 5 516
74876: 1 1 742 4 78
132842936: 332 1 4 27 56 82 8 89
22130: 822 26 383 8 367
3100: 7 43 8 8 2
525626: 91 76 85 37 411
484623240541: 3 939 7 459 2 18 8 9 14
2951: 30 2 35 67 14 57 626
571540783260: 6 3 5 9 40 775 8 263
78027357: 1 5 58 4 6 4 27 35 7
2259: 7 6 169 57 5
1248: 8 14 30 577 8 3
1971567: 490 63 44 7 9 2 3 7 9
83624: 821 8 96 629
2633267922: 56 8 7 7 99 2 9 3 6 6 877
2339069040: 9 7 3 4 7 7 3 7 744 3 770
2074547583: 59 1 1 7 8 9 37 57 1 3 69
1409: 9 114 6 8 47 117
6240: 47 6 4 1 888 8
430: 14 10 42 186 63
2723187096: 864 3 4 38 41 5 63 8
255: 3 65 60
5615083: 147 48 7 9 438 79
347646107: 887 4 4 5 78 4 3 2 3 4 27
1777861: 9 2 3 11 9 670 7 1 9 36
280380657: 466 387 914 6 57
771349: 7 707 79 567 3
109666: 2 50 8 729 58 18 858
128635584: 8 5 17 5 924 7 4 22
14636: 284 3 51
116712657: 9 3 6 3 68 6 4 5 5 3 41
540615: 82 5 1 8 649
176142: 420 611 277 586 93
111787430762: 630 8 3 8 7 7 851 3 7 98
42111749222: 9 7 9 8 3 8 852 2 9 8 4 22
1074: 29 77 1 5 7
132692685: 24 867 911 7 69
376402668501: 7 448 6 888 9 2 2 81 2 6
9486541: 9 94 60 9 541
336236: 6 589 51 5 4 187
9733786: 6 1 76 9 8 71 1 4 3 67 35
61796744851: 727 85 1 736 4 4 842 6
1074330: 173 2 69 9 5
340095668251: 872 331 74 589 125 2
10336987: 66 14 73 83 814
194152788391: 6 698 575 95 5 95 562
5419577: 576 7 448 68 3 2 3 360
6188339: 972 618 7 556 59
70936194: 89 65 2 9 791 107
468: 90 42 1 3 63 6
1028060554: 643 17 99 950 4
85198845698: 979 3 8 711 51 98
13714512: 2 357 98 4 49
3002656983: 306 39 35 7 98
10500342: 52 50 2 3 42
2423280031: 46 6 52 80 2 5 29
12152027478: 4 6 6 5 5 250 3 27 1 4 3 6
1547419402: 924 3 5 3 4 9 6 31 587
654378491: 711 16 9 784 88
409268: 682 6 68
2391520: 81 738 8 2 40
3012307274: 67 156 74 6 19 786 3 5
47498375332: 5 805 2 78 8 20 9 59
511997: 855 597 52 637 871 2
66191289: 1 767 548 6 31 1 835 6
1555572251: 20 16 74 169 847 813
4488: 2 9 2 4 88 21 2 981 2
281359589: 1 48 19 75 82 1 7 17 89
3885427042: 124 19 260 1 5 6 209 1
98286: 98 281 5
582153845: 12 2 9 2 7 1 890 8 7 6 1 4
299816771: 746 54 254 4 42 4 7 71
14721005: 9 4 550 2 7 6 7 9 6 6 7 5
43729086461: 780 8 89 304 629 61
211602: 68 1 382 8 28 6 694 1 9
4469841253: 2 77 787 5 7 8 7 1 922 5
2832397: 116 872 5 4 7 1
584243168: 1 6 912 8 383 8 3 166 3
3044292: 553 5 11 9 5
76834: 909 79 6 73 12 3 2 1 9
18890533577: 5 16 6 8 61 5 3 4 8 9 81 4
3250888646: 4 837 6 672 210 3 1 4 7
91142970: 2 9 3 6 3 38 269 4 5 9 8 8
5368731410454: 372 8 2 1 857 4 9 6 1 4 4
23920: 9 1 8 2 16 7 7 9 7 1 86 52
1311393: 51 7 445 808 390
3182298: 5 3 5 1 9 4 2 55 89 42 1
194808: 474 9 63 15 3
151690163: 6 78 9 36 58 16 5
3742922: 3 817 24 2 9 8 3 4 7 47 3
4571390610: 8 413 5 799 6 453
69327369379: 6 4 448 612 8 3 938 2
41697: 9 801 937 5 967
325916990: 8 139 8 92 47 4
80511264: 192 8 8 91 4 72
44839905: 64 8 2 73 3 6 52 8 41 4
119865: 99 4 14 2 865
300876553: 38 6 9 334 439 1
17489: 8 5 1 3 54 1 1 8 6 9 184 9
97159080: 1 4 2 4 1 5 858 986 9 7
4752238481: 66 8 90 2 15 9 59 48 1
105485: 1 6 4 1 2 2 9 1 7 8 8 365
22883090: 8 2 236 37 831 3 6 79 9
8148429: 925 9 88 51 2
336385: 6 186 8 219 3
13656603: 22 3 14 612 436
19920: 6 1 42 5 83
622484: 5 1 22 485
126126: 283 3 1 49 9
2126000: 1 29 99 142 4 2 8 7 88 8
341588001: 750 9 863 2 2 2 9 6 34
14013642240: 6 96 61 676 590
12840932608847: 287 269 185 88 447 9
3238472: 400 8 9 628 844 4 38 5
28228: 11 26 314 2 8 4 114
8543957: 57 3 794 39 57
14960: 6 10 62 1 487 8 8 10
1030539: 17 4 856 541
5677781: 5 115 7 7 759 9 52 3 3 5
14619221: 3 4 9 16 2 6 2 7 1 44 5 7
1532253495: 71 681 668 4 51 1 3 8
7865876688: 433 9 4 2 69 39 914 8
13129: 25 4 5 7 66 270 2 4 79
6165088: 444 60 2 2 8 41 37
96220574: 2 827 2 12 581
10842232893: 85 58 83 53 48 6
37946617: 4 3 893 489 855 7
34455402: 3 3 3 86 523 6 2 7 2 9 61
1292284: 4 890 363 3
5360867976: 77 94 33 22 683 975
38410: 6 1 5 68 9 2 3 169 47
1852: 5 4 8 6 1 7 9 3 294 5 35 3
526461: 13 4 1 408 610 457
2082810511: 3 4 438 9 3 1 28 4 8 1 16
5750258: 592 81 97
252337: 3 111 7 9 52 9 77 2 85
14140158827: 7 8 4 76 604 863 2 827
516824: 18 955 6 35 88
1700: 5 951 745
244599099: 6 267 6 7 1 9 3 6 90 297
206912584: 1 9 3 51 9 6 5 5 4 39 7 9
24388094: 6 19 8 48 8 684 65 91 1
8663547: 8 34 4 48 106 511 53
9471603: 820 57 48 3 75
202002139: 3 67 89 6 98 56 757 9
1184028: 545 460 178 65 5 370
152544: 516 3 9 9 135 227
7101: 6 644 18 1 142 276
9853663387: 2 96 536 63 385
7211757: 7 21 1 7 58
2410277: 8 429 3 4 916 591 2 6 9
51182: 1 42 8 18 5
2279: 52 2 18 81 73 577 576
1359: 14 4 629 8 666
52244436: 1 5 1 1 42 4 2 521 970 7
125859: 8 5 5 3 7 709 2 9 7 36 4 3
8341220: 446 550 23 7 2 17 1
13377387: 8 1 5 86 2 9 8 7 73 90
9503: 949 9 4
67285784: 841 8 523 5 34 512
16568074654: 3 588 5 2 4 6 7 808 7
65897675: 26 44 94 9 7 6 75
33904005960: 41 26 115 455 86 4 44
42575: 6 505 2 2 8 5 7 1 35
26981999631363: 7 268 64 540 8 774 43
20109536: 40 21 5 3 863 676 1
5253241360: 52 532 41 358 4
713609452528: 7 9 713 4 2 34 5 938 7 8
9212527584: 73 666 8 911 26
7569893: 6 7 7 660 4 47 7 1 17 9 3
16536638282: 15 506 529 2 6 86 2 81
251003153737725: 3 585 75 9 3 391 7 726
35760: 123 1 5 1 6 262 2 8 5 1 8
838483986975: 4 79 848 3 98 69 72
2421605: 7 6 2 2 4 9 6 8 8 2 3 97
44218: 900 8 6 2 77 8 2
58416001768: 93 1 3 47 89 4 809 54 5
10839530: 6 7 5 3 5 1 8 6 92 8 6 199
969048475: 1 59 950 51 339 25
49899635: 8 9 5 46 1 7 4 8 7 55 5 1
49527142865: 206 3 6 2 48 4 9 9 6 3 4 2
1691: 8 7 1 5 8 9 5 3 54 7 4 987
695: 80 7 226 345 36
308483: 77 77 52 15 87 56 17 1
3161109374: 453 733 3 952 38
70043: 1 13 60 7 89
168: 2 1 22 87 8 6
1274860920: 4 4 7 3 3 7 7 8 6 72 158 1
1617: 1 6 5 14 899 2 408 140
10188640: 7 5 6 7 6 9 7 426 8 440 4
859: 63 3 226
819484: 89 9 93 11 61
3145716000: 5 2 6 5 8 7 855 2 120 6 5
4199: 42 10 1
1107874375: 791 338 84 7 2
348268543: 43 4 8 9 14 924 9
189493: 888 1 998 8 90
2346724: 2 22 54 882 4 3 2 6 950
8855291977: 7 251 42 120 11 977
34562968: 80 36 3 7 42 4
2078881006882: 772 794 5 7 1 36 969 1
7739979: 7 71 1 269 8 71 981
365933403: 40 39 302 15 20
278068: 69 46 331 79 176 997
3346157: 7 5 9 2 47 9 161 26 69
38718: 8 4 6 709 6
2470438: 24 70 328 92 20
4378673: 4 5 6 75 14 5 16 987 1
952240: 5 3 3 721 2 4 9 6 5 1 5 5
45335554919: 7 55 59 2 574 8 6 2
486944619969: 9 7 502 46 199 65 7
368565339: 778 524 33 904 19
20718: 48 9 38 128 2 2 9 3 33
54053925: 9 8 9 2 94 93 3 552 775
26117287623: 720 52 2 992 3 127 6 3
11063628180: 3 74 1 1 45 90 1 38 29
34424: 34 990 8 748 8
1237: 83 61 8 83
1321: 620 9 691
3454602: 9 385 997
803055899437: 5 4 9 749 1 3 3 6 3 9 57 7
537130171: 5 9 26 8 1 14 905
1269294703: 8 9 7 33 2 4 376 2 718 2
193: 2 91 4 7
33651: 2 310 8 558 4 159 68 9
96525889: 87 46 60 5 1 2 4 9 9 9 2
35523840: 53 5 407 75 5 50 5 704
6119571: 7 47 186 67 28 76
557972: 587 949 1 863 45
137: 4 9 7
16075722: 85 6 626 1 5 3
4894356531: 7 9 769 59 9 2 5 5 890 7
8652051492: 6 96 80 334 7 5 9 1 3 66
3607175233: 41 12 68 3 1 752 31
58: 4 46 8
518221854357: 49 2 897 30 524 23 57
9450: 407 37 5 1 21
52179924968: 8 85 6 48 9 796 76 8
1827917: 203 1 9 15 4
54004: 50 108 6
362559: 1 6 3 1 8 7 296 5 2 9 4 3
75755316: 51 24 730 9 3 3 4 6 316
116047085245: 469 1 84 6 9 3 9 5 23 5 7
112: 46 8 39 13 6
7134939: 7 7 31 2 526 2 97 7 63
11271332: 109 74 297 33 3
34887212: 93 3 81 434 459
46650328550: 478 5 92 457 964
763835431: 2 2 9 3 288 844 30 68
1331853886: 719 92 1 37 7 5
3104: 3 2 9 722 4
18677: 993 18 625 174 4
11626152: 58 3 253 9 7 9 6 9 606 8
3488586968: 7 267 78 6 3 29 33 7 1 8
425954621: 9 1 8 562 8 986 2 7 260
37136: 5 2 29 37 28 3 1 56 3 4 2
1741069140: 7 3 5 329 2 3 4 5 3 2 2 6
17598206: 8 32 41 4 7 56 52 820 8
4129: 1 717 5 76 8 461
955: 2 76 2 37 762
4414: 421 20 1 1
43121605: 69 513 94 243 5 40
2603641885: 66 7 6 39 18 83
35221227: 831 9 67 42 27
31458: 62 17 390 91 8 2 548
14706: 747 19 442 62 9
26259408: 420 58 9 7 872
101752: 9 2 5 71 632
7896111996181: 5 34 1 6 9 7 967 5 8 1 8 1
81667: 7 8 349 3
60817806: 4 3 367 699 754 5 11 4
23869235: 451 6 7 5 9 63 3 7 4 6 1
241118711659: 2 9 1 7 2 8 5 69 97 506
3266457078: 8 929 7 7 232 235 5 7 9
178547021: 34 828 54 6 207
935310428: 3 22 34 9 74 51 22 5 8
1600021: 98 8 5 408 661
3779270: 71 864 94 43
4365848: 4 83 3 5 848
96718: 880 71 16 11 6
500207996: 2 5 2 951 8 8 73 7 3 313
1666885614: 28 592 2 1 907 561 4
200111: 2 23 26 8 3 1 68 753 62
104200: 50 5 104 1 1 48 4
221548122840: 834 49 675 935 92 62
20616: 2 20 1 1 364 1 4 9 5 293
9573809: 27 334 555 731 9 70 2
6466456137528: 357 26 2 77 181 526
58959566670: 6 8 9 2 9 2 685 622 6 5 6
4731958538: 6 9 4 132 7 16 4 9 39 6 4
316723680: 863 6 50 2 54 65 7 2 8
55746501: 2 1 2 8 4 2 524 7 4 9 503
5026248: 557 2 7 24 6 2 526 7 7 9
41097948: 4 40 640 961 2 46 6
15810074: 30 2 1 2 26 835 923 1 7
1296043391: 348 9 8 87 9 7 7 703 84
1371102: 366 52 9 6 71 21 1 8 1 5
101663: 8 4 8 397 30
77467230185: 1 537 9 2 6 2 24 7 9 4 9 7
9195802: 319 84 49 682 7
43440: 87 594 63 3 534
44569578320: 2 21 8 6 723 13 340 4 5
64377: 63 985 392
815725: 44 7 4 456 351 46
48009771: 6 667 99 8 12 9 38 88 7
61335224: 1 8 1 662 1 9 5 357 22 2
14106595: 5 47 6 65 95
10204857: 282 4 8 904 2 96 405
2808: 340 9 2 8
871862616: 11 6 1 2 3 4 9 4 829 9 6 9
272358551484: 6 606 1 592 6 2 741 84
52636579: 10 548 4 499 60
51652328: 6 5 6 2 9 1 520 4 1 2 330
6408: 3 5 1 2 351 31 1 3 7 7 41
1295205629: 4 318 968 5 2 10 56 26
32102428: 45 860 6 7 8
4036544331: 7 2 3 39 48 311 5 7 86
288830003: 809 97 708 5 4 707
1203899: 479 82 846 6 30
191950: 33 74 27 89 55
31672: 5 8 3 23 6 39 1 2 9 76 6
93219: 8 2 9 9 1 3 15 9 381
905861: 493 5 6 170 343
2221585: 93 526 38 9 59 4 93
571907419: 3 3 7 282 26 7 8 4 3 2 1 9
7478: 9 1 3 31 4 4 4 7 7 364 8 9
3543142: 217 5 266 4 6
1715568324: 85 778 2 8 323
136325: 189 8 8 95 7
1660659452: 61 505 2 6 5 6 9 9 220 5
8289313: 82 88 57 4 739
43340110056: 2 983 44 5 5 4 3 5 2 2 59
164434127000: 16 4 1 44 13 898 985 5
22864049: 8 3 2 99 4 29 196 1 84 2
984742777: 303 108 100 759 3 8
495671024: 278 218 1 198 73 69 2
51417297410: 5 1 417 1 297 412
30885: 3 355 86 5 92
227200267: 7 1 7 2 9 238 2 59 70 6
31865468737: 318 64 1 8 6 58 8 99 34
305803: 2 6 463 6 9 888 6 127
1844699: 8 973 585 193 6
2394960: 559 50 80 146 85
535685: 5 46 9 1 7 375 3 45 2 6 5
2116530: 286 74 54 73 3
44901: 461 3 95 80 178
1516: 968 62 486
59244: 9 65 1 89 512 44
433479059: 77 6 72 3 758 672 86
776794088: 83 4 1 2 6 23 31 26 3 69
923427204853: 949 5 218 7 1 6 74 854
1973525: 1 9 5 185 67 5 4 80 7 88
4609452500: 58 347 47 3 790
266136: 60 55 31 166 853
8888090408: 82 46 6 95 112 21 8
430920: 105 9 6 76 1
9870138315: 36 5 494 165 37 3
84873: 30 818 73
190579647: 29 9 1 14 6 5 3 123 5 9 7
9138: 359 62 3 33 9 7
583847361946: 6 82 5 4 3 4 594 6 5 9 4 5
2072400: 759 3 5 3 7 3 3 2 5 3 44 4
11562019: 145 51 7 781 2 95
3786592318: 210 9 8 914 274
267216582: 38 8 879 58 3
7388316276: 2 3 947 13 15 2 16 273
1976463552: 8 2 5 5 770 8 7 934 47 8
2485918: 5 80 62 59 20
117857: 7 88 155 4 2 57
1375824490: 2 85 3 605 637 7 40
68946560: 6 88 1 5 9 65 58
165564: 49 5 9 63 73
1113408: 1 381 2 4 518 3 9 5 8 4 9
97000: 300 80 75 213 85
115024: 2 2 1 518 543
887722500: 190 32 875 5 914
148216311360: 316 76 7 31 72 8 5 711
19859238: 6 44 13 42 3 569
643119180: 5 2 34 6 83 87 68 465
1000: 84 325 1 78 513
1129710: 42 6 3 2 438 306 99 10
7928008: 938 46 7 250 32 7
8976449: 81 5 38 338 451
202123597: 4 4 441 33 5 779 6 93 4
32107000: 210 3 2 508 2 9 29 82 2
31388325351: 8 705 3 71 44 55 6 795
867: 51 5 95 195 60
12012328: 1 788 7 5 6 8 7 94 1 3 2 7
4552200269: 600 15 562 3 90
9321: 5 4 3 21
52651: 633 485 13 9 2 348 5 6
2422222: 9 7 5 16 650 75 44 8 14
540941113: 15 91 34 11 16
2106220944: 8 9 774 5 880 20 17 8 8
77: 1 52 20 2 1 2
5527977: 62 3 5 34 6 5 7 58 5
182: 1 3 4 5 6 6 2 8 8 4 68 1
17298244: 11 273 96 2 5 9 60 3 1
4585758: 76 5 111 85 58 6
112232: 4 134 55 36 179
12483627: 602 64 324 481 65 9 1
45570: 4 183 58 729 30
20827088: 199 6 1 8 8 8 6 95 4 4 8 4
1301: 3 406 9 69 6
4293025138: 8 8 518 5 737 139
1141: 5 5 6 2 81
2027005050051: 4 800 367 9 7 5 28 51
1268364825: 50 43 18 5 725 117
46428: 8 58 21 3 5
2719: 183 61 430 4 23
5099969487: 2 7 240 9 97 91 56 2 87
7269614380: 9 2 3 6 97 56 73 69 8
31190171875: 489 9 3 275 5 7 463 6
1657232: 716 877 63 341 889
18260347686: 882 5 712 92 5 9 7
89729745030293: 4 941 1 981 810 3 2 91
11304: 94 610 552 9
341649258590: 8 317 4 778 9 6 5 9 3 44
148614: 1 34 431 2 2 664 93
10545: 4 38 227 82 929
1501452050: 500 4 5 4 15 1 1 6 298 9
324566: 9 4 49 408 8 6
99973448: 87 97 1 81 8 87 540 8
173488: 79 7 2 516 972
9620828323472: 9 718 99 832 3 475
16013933178: 2 2 868 9 7 33 161 1 7 8
1998720: 6 6 347 6 80
95631331: 2 1 823 25 59 970 1
2810740: 73 423 91 63 6 682
526100048: 939 376 250 4 49
7727772106: 4 3 314 2 445 79 4
18573499: 96 259 83 9 91
737254677: 755 7 410 106 629
1409526782: 4 8 138 87 255 566 38
145126343015: 5 30 77 4 6 730 889 45
9527008: 2 280 17 8 33 250 28 8
13279560: 204 113 576 697 909
2063488: 196 12 5 31 2 64
116095: 77 34 15 8 78
1538979361263: 18 29 25 19 2 83 12 65
46930788030: 3 372 965 434 715 42
9893490: 1 3 7 441 1 456 2 6 8 9 9
28545053346: 251 468 79 3 169 6 81
165669022158: 6 8 8 1 88 551 7 725 61
88306: 5 3 3 2 621 2 3 732 7
6540800: 1 5 584 448 5
6034871: 3 7 7 862 2 5 2 9 523 71
229912: 504 57 8 88 1
3478010: 552 9 55 7 26
1056560: 5 1 6 2 9 131 4 7 8 1 7 4
202418: 1 6 1 6 2 8 301 67 79
6336: 4 9 9 16 2 9
6756678588: 5 5 6 53 12 5 654 9 4 1 3
69300293636: 7 2 550 1 7 4 1 74 5 5 5 9
1601928000: 96 187 784 95 10 90
55892200: 6 4 3 53 5 7 740 26
2522791: 9 338 9 725 519
896831: 82 30 8 826 4
3173522: 634 155 68 476 6 1 5
1371838: 342 4 2 36 37 1
291757680: 6 9 3 1 125 3 3 4 6 3 80 9
90804: 6 6 4 1 5 6 34 5 6 81 188
10930523: 5 85 45 993 969 20 6
36927468270: 52 9 5 253 8 43 770 9 9
13101: 9 9 51 18 14
115200: 97 7 6 4 79 451 5 5
205333081197: 9 70 49 805 60 45 5 72
5495857: 58 4 3 90 8 7 9 531 9 7
1155432936: 96 3 858 4 521 414
722223008: 7 6 3 8 7 839 93 106 8 8
19389607459: 60 5 8 806 17 219 4 77
584952456: 55 3 495 24 58
322349: 72 62 60 4 69 2 2 5 49
33119267452: 2 7 3 5 8 2 83 9 170 3 9 2
346948360330: 482 861 8 836 327
211665: 81 13 26 718 9
225225: 165 97 7 91 479 67 9
17764412982758: 94 9 4 4 7 8 353 5 695 8
959052886: 4 555 24 71 3 8 2 6 3 42
1714129535: 67 1 26 672 38
630: 6 2 79
40994257: 122 336 641 830 784
22694445782: 38 4 5 3 4 2 6 152 6 3 2 1
40714036899: 848 20 91 8 6 99
1107642: 269 3 6 3 6 9 4 7 93 9
29772424: 4 99 3 90 416 7 5 3 9 8 1
6601525: 954 6 877 52 5
203151: 1 1 3 29 942 1 6 4 8 7 8
198114456: 35 7 1 903 8 69
17643: 1 83 8 3 9 4 26 3 7
131307201904: 647 974 9 6 891 90 2
1527944971111: 2 76 7 2 7 4 497 1 1 14
2776387711: 5 4 311 852 6 68 870 8
1075140: 61 5 905 9 2
6472293751: 76 9 318 159 625 65 1
558692339: 2 31 3 6 76 1 7 85 3 3 8 1
6684204507: 921 93 68 85 775 7
26647495: 1 4 9 5 10 8 2 832 3 3 6 2
467656: 6 2 1 3 11 135 3 530 9 8
205144: 6 921 19 2 3 1 27 94 4
150044712: 69 4 42 7 539 6 12 4
101048: 3 4 976 40 5
103049601: 288 34 32 4 3 53 4 5 5
41951092: 1 3 75 518 2 968 9 57 4
706013770: 4 8 22 5 9 164 973 69
2624892: 36 42 56 2 31
20585875: 41 20 250 858 78
166166: 1 845 1 3 9
3101: 309 4 7
1159944430: 33 2 2 711 912 349
3018: 128 3 23 4 1
106997605: 587 897 2 91 20 8 325
355364898369: 533 9 52 7 1 2 537 8 8
254814266: 6 1 49 66 79 437 61 3
103141: 52 7 972 39
6372617067: 65 65 7 67 773 84 4 6
104571794: 1 79 866 612 105 94
76038057: 3 1 9 2 57 460 59
8777133: 8 777 133
16027: 8 4 3 37 28
70483278: 979 708 981 7 629 9 6
24921604: 8 8 4 440 885 4
46899489: 8 5 168 997 1 80 7 7
35151942730: 99 86 5 2 97 516 8 1 1
120879745851281: 831 36 727 925 6 40 2
3071: 4 3 460 1 18 40 4 83 5 6
48120: 1 9 1 1 7 92 3 34 3 6 5
283885: 2 9 93 18 354 9 577 1
134591197: 466 4 58 63 7 64 6 9 5
279981: 44 634 8 93 1 1
2569077024: 669 8 1 2 2 2 8 3 6 21 6
724795458615: 959 3 6 820 9 9 41 83 5
5315050272: 497 2 2 541 952 893 6
2572983: 4 734 5 8 5 300 69 320
15564683: 191 281 58 5 93
95080: 5 3 385 559 5 3 5 30 35
463421: 342 5 6 82 16 5 280
39374057: 3 55 867 87 7 5 9 3 8
8943993: 7 90 922 99 494
460707: 19 553 805 78 169
8835: 875 3 4 52
19482024: 506 713 6 1 9
6500: 216 7 3
8522092: 788 9 2 8 704 8 1 5 3 52
24279886: 912 1 783 17 231 80 2
61173671130: 53 585 526 121 31
17641800505: 5 5 2 9 4 5 891 414 8 80
71114: 890 69 2 74
11847820: 3 864 9 85 506 5 5 832
1090375401: 5 275 793 397 6
4731215040: 78 3 656 4 7 538 372 8
11178126957: 3 5 1 23 578 49 286 4
1810644: 6 391 76 6 638
562076182741: 3 1 6 7 37 3 51 8 2 741
519277338: 8 5 472 4 20 321 5 423
4942206: 5 7 6 7 69 2 8 2 4 3 4 62
148173: 569 6 9 824 7 9 104 77
26066988: 325 46 2 98 656 685
10063906209607: 1 1 7 2 768 61 8 7 7 608
169673263205: 354 6 743 92 70 5
7577331: 1 84 190 1 25 9
1179: 3 3 7 98 3 8 6 5 5 2 4 51
70514001: 722 190 6 514 397
90327831967: 5 1 840 900 938 88 22
858123614: 836 9 6 352 490 54
265703: 26 529 1 2 8 394
2226099086894: 274 6 29 684 647 802
31834247210: 20 3 3 1 693 6 52 8 7 2 8
4478407712: 7 4 5 8 9 1 4 46 9 1 928 4
203221448: 5 1 59 9 509 6 4 5 7 7 4 5
154774: 7 10 987 82 87
6566471: 160 65 55 628 731
257562114: 68 1 7 540 5 2 1 501 9 2
2068421: 56 7 9 44 18 2 2 3 6 16 5
11037712: 108 90 60 63 7 16 2
34883: 404 2 3 7 9 7 3 7 4 283 8
16713: 12 608 26 160 419 14
1803289766: 1 5 468 236 7 89 769
1454723695: 2 49 7 396 1 7 3 5 9 51 1
37650: 6 8 2 26 3 54
27433: 9 8 5 1 76
88807048: 269 428 289 92 979
37170142: 4 9 7 2 565 4 525 1 39
122341: 9 6 55 163 3 3 123 70 9
85439740: 7 8 2 299 561
316050214: 347 65 4 909 4
23890266: 39 816 2 6 54 5
215375: 716 1 3 5 7 3
1627751777: 2 74 22 7 9 5 4 1 3 7 37
23145906: 6 1 378 7 458 908
106768248: 1 5 4 386 4 2 6 8 5 37 24
300: 33 9 3
26465: 5 659 8 45 57
844867817160: 4 9 2 509 9 79 917 5 9
7347: 347 57 18 75
1797080: 5 2 4 503 66 4 9 735 5
1568: 6 650 8 660 244
66376890: 18 7 8 439 6 15
1849227: 201 23 4 19 8
793203: 984 239 25 635 723
3424616103: 37 8 96 8 149 5 23 78 2
23875504: 90 719 59 263 4 885
954640: 4 772 2 55 185
1489130: 1 1 15 45 9 9
477400704: 4 14 5 4 60 34 40 698 3
26314: 36 295 79 85 80
2736: 141 4 7 6 3
160877644: 65 7 8 5 899 7 4 7 44 4
6761974: 67 616 3 7 4
691978: 9 4 4 5 3 7 2 944 7 37 2 4
4030615623: 6 9 4 6 7 97 6 617 9 8 88
326082: 29 506 7 1 3 29 93 8 79
850433: 6 6 8 69 2 324 3 905
470846: 37 70 1 44 1 43
81983340: 2 699 8 62 81 90
124225: 23 6 6 150 25
47144387: 53 20 515 8 464 386
17579: 30 65 9 24 5
190605: 69 6 4 754 88 2 2 636 3
110477429: 4 6 58 8 56 8 6 26
13152: 6 7 4 79 50
23639868072: 7 85 705 365 255
110028: 5 68 3 274 28 436 8 3
104918: 80 9 240 1 8
11373: 9 5 48 94 2 2 5 3 1 3 2 9
65743427: 218 6 3 6 6 97 369 55 3
33522001: 5 1 68 94 49 7 444 1 2 1
895876284: 7 7 7 6 9 77 7 756 6 8 1 5
168473: 29 938 769 97 81
5997059403: 8 1 88 7 598 9 88 4 75
6939815239: 69 37 2 803 12 242
39330: 8 521 734 5 1 8 74
51465024: 7 86 9 190 522 96
193506: 68 1 47 4 6 553 7 873 7
261121: 673 51 4 681 73
7226: 46 2 41 6 892 7 9
11776320178: 98 4 48 6 3 8 5 9 1 8 5 60
244416: 35 25 93 97 3
2029580: 54 74 604 22 279 20
36676944: 78 76 4 549 740 4 944
133523338979: 5 5 4 32 506 6 9 4 980
135977500: 190 5 6 9 40 545 998
1086571178: 6 678 8 37 242 4 149
1403207094: 8 3 7 598 19 5 9 1 4
97050783: 47 65 9 44 85 52 9 7 6
3894377940: 7 91 2 1 6 2 99 5 9 9 570
48262523: 4 30 634 6 6 157 1 4
3557636392: 9 3 838 9 3 509 8 473 1
19786377: 4 429 51 128 7 9
33888: 60 2 91 6 6
3582088: 96 5 222 37 51
83376844: 6 463 1 5 92 9 4 9 2 3 2
6524: 21 4 77 16 42
87550085951: 8 51 522 54 4 476
14985: 1 29 8 46 4
1425078: 8 178 15 93 1
229140719: 3 378 359 1 202
612190840: 6 8 56 73 6 7 78 4 1 1
282377107345: 73 4 783 549 1 6 2 7 1 9
6148875: 9 4 2 9 6 92 79 35 14 3
590144047: 1 167 4 89 568
268416: 3 8 360 82 576
8216264: 31 787 3 62 61
43456287: 609 485 53 3 609 7 7
366996852: 8 6 5 71 4 8 6 4 8 4 842 9
10929484: 332 823 4 1 4 28
607695266132: 88 92 753 956 6 9 47 7
1821: 60 19 680
944541090: 413 937 845 828 90
3825717: 20 65 45 7 17
591340880: 2 9 2 2 9 9 385 8 6 46 27
4458: 14 9 5 6 678
748135: 18 725 5 13 5
22239973: 4 8 10 526 38 2 17 75
16994: 59 3 48 2 2
75665606: 75 66 5 603 3
81767622: 6 7 8 1 304 7 7 733 8 1 6
502348: 52 671 9 17 77
7575408278: 7 2 9 8 4 3 9 3 307 951 9
16838830: 2 9 4 48 3 5 9 869 3 47 1
2547054637: 423 6 9 2 172 7 94 3 9 1
1281662: 8 80 757 74 2
7872: 5 2 7 188 252 474 8
28959990: 45 7 1 55 92 321 86 30
34984171951835: 43 73 8 171 95 18 3 6
52504426946478: 72 7 98 67 53 8 33 6 61
9435: 18 8 92 707 5
248923365: 88 8 4 902 2 98 33
27158400: 18 27 82 5 4 368
1337442625: 19 268 695 9 40 745
1914517976: 89 273 598 8 8 66 8
1779: 27 9 48 4 47
23304: 73 9 3 2 342 3 7 495
3156484: 541 7 64 9 5
185134742105: 6 2 6 84 1 16 5 6 231 9 3
1365370: 369 37 68
2340875: 6 4 4 1 395 3 3 543 1 4
1488310275: 1 3 767 77 4 2 1 9 4 768
435855553: 2 7 30 60 1 230 584 8
2165524226: 89 4 4 2 7 1 8 9 971 6 2 6
11791177: 293 6 6 7 657
55846: 8 67 6 8 3 4 80 6 2 10 6
51140487580: 47 794 13 8 7 178 962
95628170581: 2 8 46 4 3 5 3 5 3 56 9 20
421116463: 2 6 7 8 3 78 95 616 5
2646360: 1 6 9 77 69 7 8 961
16911824: 7 29 315 6 3 1 3 9 7 8 8
508164021: 9 964 510 24
14638508807: 12 224 5 3 97 8 5 9 399
6355295184: 7 8 901 8 532 5 9 4 9 2 8
137362: 68 1 6 2 71 91
827873: 813 9 5 851 7 12
196192: 3 323 91 8 6
158146: 5 2 5 6 2 6 3 5 37 4 617 7
258810: 317 6 39 8 98
3685626961: 729 1 7 5 626 95 5 7
15031: 55 54 10 5 66 4 61
4859278: 48 59 21 6 9
64466: 1 4 8 1 8 1 202 3 737 99
5144691549: 716 1 143 628 8
50463263: 50 35 7 17 89 260
70125: 1 69 6 935
24519476757302: 9 77 645 97 532 1 685
5165: 49 9 89
373902203: 8 15 2 8 2 19 917 7 5
2919060663: 42 305 219 8 69
559293182: 7 8 48 2 6 2 9 43 5 72 9
1136278: 421 6 8 653 4 6 4 4 5 2 5
1695220198: 6 6 14 542 469
598958: 561 1 37 239 719
11297453608: 1 815 1 29 865 16 1 1 3
277623015278: 6 421 99 754 30 754 7
71396807: 440 3 2 1 2 4 4 9 4 37 6 3
2402476: 238 2 20 473
52645: 186 73 4 2 45
3675880: 3 69 179 181 824 52
9565103: 7 6 3 929 620 9 13 459
4313140: 10 31 3 4 265 13
103899212: 50 2 529 9 2 707 212
221160779429: 6 2 6 82 7 1 3 8 6 79 813
58306432822: 5 5 98 84 47 548 1 4 5 1
25157838012: 769 53 16 413 498 2 3
289182: 36 8 1 6 88 4 59 77 5
136725: 2 84 4 9 401 2 7 59 5
221095170: 5 57 720 4 5 67 219
87196: 365 369 59 2 584
224122627: 7 2 9 2 661 117 63 1
177120: 883 94 7 36 5
66177725: 911 282 88 60 9 7 5
742541913: 73 748 110 396 1 910
171987: 245 7 98 389
26135429: 40 5 88 3 525 42 448 5
461463: 190 6 24 402 3
136650185: 3 2 23 450 987 38
244964: 84 5 32 1 86 1 35 1
102939624: 49 959 77 9 27 203 9 9
67204571: 38 44 8 1 4 3 3 15 8 5 5
1591297472: 7 4 65 1 3 9 3 9 5 7 9 86
1050488981435: 71 787 94 6 907 2 37
836077982: 835 839 234 4 983
17594724: 5 464 2 46 1 7
7488: 7 2 9 287 867 18
385032453: 2 58 3 12 5 27 92 6 5
7536: 84 77 92 8 961 7
3665717582: 6 3 5 1 21 8 8 2 5 6 1 33
649686: 8 75 84 95 834
4905: 379 3 3 48 32 4
63189: 1 6 832 96 3 3 614 7 49
14658206: 1 826 8 67 91 912 758
56028: 96 99 287 63 1
105684258502220: 461 917 5 170 5 2 217
12510: 4 138 833 5 9
783766376248: 7 3 70 88 9 748 9 9 6 8 6
944: 8 647 51 238\
"""

if __name__ == "__main__":
    ans1 = solution1(input)
    print(ans1)

    ans2 = solution2(input)
    print(ans2)
