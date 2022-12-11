import re

cmd_re = re.compile(r'\$ (\w+)\s?(\w+)?')  # cmd_re[0]: cmd, cmd_re[1] (optional): args
dir_re = re.compile(r'dir (.*)')

class Tree():
    def __init__(self, parent, data):
        self.parent = parent
        self.data = data
        self.children = []

    def dfs(self, top):
        pass


with open("input") as fp:
    data = fp.read().splitlines()


root = Tree(None, '/')
root.parent = root
cur_dir = root

for line in data:
    f = cmd_re.findall(line)
    if f != []:  # line is cmd
        f = f[0]
        if (f[0] == "cd"):
            if (f[1] == ".."): cur_dir = cur_dir.parent; continue

            # TODO if not already there
            cur_dir.children.append(new_dir := Tree(cur_dir, f[1]))
            cur_dir = new_dir
            
        if (f[0] == "ls"):  # TODO: needed?
            continue

        continue

    # Line is result (size filename / dir x)
    f = dir_re.findall(line)
    if f != []:
        f = f[0]
        print(f"DIR {f}")
        dir_exists = False
        for child in cur_dir.children:
            if child.data
        cur_dir.children.append(new_dir := Tree(cur_dir, f))
    else:
        print(line)

    # fsize = int(line.split()[0])
    # fname = line.split[1]