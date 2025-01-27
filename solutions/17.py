from re import findall


def parseInput(inp):
    inp = inp.split("\n\n")
    abc = findall("\d+", inp[0])
    program = findall("\d", inp[1])
    return [int(x) for x in abc], [int(x) for x in program]


class Computer:
    def __init__(self, abc, program, Debug=False):
        self.A = abc[0]
        self.B = abc[1]
        self.C = abc[2]
        self.program_counter = 0
        self.program = program
        self.out = []
        self.Debug = Debug

    def debug(self):
        if self.Debug:
            print(f"Register A: {self.A}")
            print(f"Register B: {self.B}")
            print(f"Register C: {self.C}")
            print(f"PC: {self.program_counter}")
            print(f"out: {self.out}")

    def run(self, start=None):
        if start is None:
            start = self.A
        self.reset(start)
        done = False
        while not done:
            self.debug()
            done = self.step()
        return self.out

    def reset(self, a):
        self.A = a
        self.B = 0
        self.C = 0
        self.out = []
        self.program_counter = 0

    def run2(self):
        # brute force too slow
        found = False
        count = 0
        while not found:
            self.A = count
            self.B = 0
            self.C = 0
            self.out = []
            self.program_counter = 0

            done = False
            while not done:
                self.debug()
                done = self.step()
                if self.out != self.program[: len(self.out)]:
                    break
            if self.out == self.program:
                break
            count += 1
            if count % 10000 == 0:
                print(count, self.out)
        return count

    def run3(self, start=0, digits=0):
        # Credit to Eric Wastl, this is his solution
        out = self.run(start)
        if out == self.program:
            return start
        if out == self.program[-digits:] or not digits:
            for n in range(8):
                out = self.run3(8 * start + n, digits + 1)
                if out is not None:
                    return out

    def step(self):
        if self.program_counter > len(self.program) - 2 or self.program_counter < 0:
            return True
        self.runInstruction(
            self.program[self.program_counter], self.program[self.program_counter + 1]
        )
        return False

    def runInstruction(self, opCode, operand):
        if opCode == 0:
            self.A = self.A // (2 ** self.comboOp(operand))
        elif opCode == 1:
            self.B = self.B ^ operand
        elif opCode == 2:
            self.B = self.comboOp(operand) % 8
        elif opCode == 3:
            if self.A:
                self.program_counter = operand
                return
        elif opCode == 4:
            self.B = self.B ^ self.C
        elif opCode == 5:
            self.out.append(self.comboOp(operand) % 8)
        elif opCode == 6:
            self.B = self.A // (2 ** self.comboOp(operand))
        elif opCode == 7:
            self.C = self.A // (2 ** self.comboOp(operand))
        self.program_counter += 2

    def comboOp(self, val):
        if 0 <= val <= 3:
            return val
        if val == 4:
            return self.A
        if val == 5:
            return self.B
        if val == 6:
            return self.C
        assert False


def solution1(inp):
    abc, program = parseInput(inp)
    c = Computer(abc, program, Debug=False)
    out = c.run()
    return ",".join([str(x) for x in out])


def solution2(inp):
    abc, program = parseInput(inp)
    c = Computer(abc, program, Debug=False)
    out = c.run3()
    return out


testinput1 = """\
Register A: 0
Register B: 0
Register C: 9

Program: 2, 6
"""

testinput2 = """\
Register A: 2024
Register B: 0
Register C: 9

Program: 0,1,5,4,3,0
"""

testinput = """\
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

input = """\
Register A: 22817223
Register B: 0
Register C: 0

Program: 2,4,1,2,7,5,4,5,0,3,1,7,5,5,3,0\
"""

if __name__ == "__main__":
    ans1 = solution1(input)
    print(ans1)

    ans2 = solution2(input)
    print(ans2)
