with open("input") as fp:
    lines = fp.read().splitlines()

data = [tuple(line.split(',')) for line in lines]

fully_contained = 0
for pair in data:
    elf1from, elf1to = (int(r) for r in pair[0].split('-'))
    elf2from, elf2to = (int(r) for r in pair[1].split('-'))

    if (elf1from in range(elf2from,elf2to+1) or elf1to in range(elf2from,elf2to+1) or
        elf2from in range(elf1from,elf1to+1) or elf2to in range(elf1from,elf1to+1)):
        fully_contained += 1

print(fully_contained)
