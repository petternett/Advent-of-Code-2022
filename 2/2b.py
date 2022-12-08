victories = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

losses = {
    'C': 'A',
    'A': 'B',
    'B': 'C'
}

with open("input") as fp:
    # Every list element (tuple) is a _round
    data = [(x[0], x[2]) for x in fp.read()[:-1].split('\n')]

    total = 0
    for _round in data:
        vs = _round[0]
        score = 0
        choose = None

        if (_round[1] == 'Y'):  # draw
            choose = vs
            score += 3
        elif (_round[1] == 'Z'):  # win
            choose = losses[vs]
            score += 6
        else:  # lose
            choose = victories[vs]

        score += ord(choose) - 64
        total += score

    print(total)

# Rock (A) = 1, Paper (B) = 2, Scissors (C) = 3
# Loss (X) = 0, Draw (Y) = 3, Win (Z) = 6
