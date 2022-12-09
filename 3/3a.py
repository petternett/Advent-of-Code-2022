def get_priority(char):
    return ord(char)-38 if str.isupper(char) else ord(char)-96

with open("input") as fp:
    sacks = fp.read().splitlines()

for i, sack in enumerate(sacks):
    c1 = sack[:len(sack)//2]
    c2 = sack[len(sack)//2:]
    sacks[i] = (c1, c2)

sum_prio = sum([get_priority([item for item in sack[1] if item in sack[0]][0]) for sack in sacks])

print(sum_prio)
