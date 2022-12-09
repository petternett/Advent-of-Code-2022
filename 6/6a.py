with open("input") as fp:
    data = fp.read()[:-1]

    last = []
    for i, char in enumerate(data):
        last = data[i:i+4]
        if len(set(last)) == 4:
            print(i+4)
            break
