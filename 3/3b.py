def get_priority(char):
    return ord(char)-38 if str.isupper(char) else ord(char)-96

with open("input") as fp:
    sacks = fp.read().splitlines()

    groups = []
    group_idx = 0

    for i, sack in enumerate(sacks):
        if (i % 3 == 0):
            groups.append(tuple(sacks[group_idx:group_idx+3]))
            group_idx += 3

    print(sum([get_priority([item for item in group[0] if item in group[1] and item in group[2]][0]) for group in groups]))
