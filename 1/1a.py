with open("input") as fp:
    data = fp.read()[:-1].split('\n\n')

print(max([sum([int(cal) for cal in elf.split('\n')]) for elf in data]))