with open("input") as fp:
    # Every list element (tuple) is a _round
    data = [(x[0], x[2]) for x in fp.read()[:-1].split('\n')]

total = 0
for _round in data:
    score = ord(_round[1]) - 87
    diff = abs(ord(_round[0]) - ord(_round[1]))

    if (diff == 23): score += 3  # draw
    if (diff == 24 or diff == 21): score += 6  # win

    total += score

print(total)

# Rock (A/X) = 1, Paper (B/Y) = 2, Scissors (C/Z) = 3
# Win = 6, Draw = 3, Loss = 0

# A, X = draw
# B, Y = draw
# C, Z = draw
# A, Z = lose
# B, X = lose
# C, Y = lose
# A, Y = win
# B, Z = win
# C, X = win
