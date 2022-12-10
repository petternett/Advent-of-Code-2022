with open("input") as fp:
    data = fp.read()[:-1].split('\n\n')

print(sum(sorted([sum([int(cal) for cal in elf.split('\n')]) for elf in data])[-3:]))