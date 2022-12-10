import re

cmd_re = re.compile(r'\$ (.*)(?:\s(.*)?)')  # cmd_re[0]: cmd, cmd_re[1] (optional): args

class Tree():
    def __init__(self, parent, data):
        self.parent = parent
        self.data = data
        self.children = []

    def dfs(top):
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
            print("CD!!!!!!!!!!!!")
            # if (f[1] == ".."): cur_dir = cur_dir.parent; continue

            # cur_dir.children.append(new_dir := Tree(cur_dir, f[1]))
            # cur_dir = new_dir
            
        if (f[0] == "ls"):  # TODO: needed?
            print("ls !!!!!!!!!!!!!!!!")
            continue

        continue

    # Line is result (size filename / dir x)
    print(line)
    # fsize = int(line.split()[0])
    # fname = line.split[1]