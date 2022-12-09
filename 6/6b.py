with open("input") as fp:
    data = fp.read()[:-1]

last = []
check = 14
for i, char in enumerate(data):
    last = data[i:i+check]
    if len(set(last)) == check:
        print(i+check)
        break
