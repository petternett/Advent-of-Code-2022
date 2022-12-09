import re

stack_re = re.compile(r'\[(\w)\]')
move_re  = re.compile(r'move (\d+) from (\d+) to (\d+)')
NO_STACKS = 9

with open("input") as fp:
    stacks = [[] for i in range(9)]
    data = fp.read().splitlines()

    for line in data:
        for match in stack_re.finditer(line):
            stacks[match.start(1)//4].insert(0, match.group(1))

        move = move_re.findall(line)
        if move != []:
            _move = move[0]
            stacks[int(_move[2])-1] += stacks[int(_move[1])-1][-int(_move[0]):]
            del stacks[int(_move[1])-1][-int(_move[0]):]

    for stack in stacks:
        print(stack[-1], end="")
    print()
