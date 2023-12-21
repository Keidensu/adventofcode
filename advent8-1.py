import re

def advent8():
    f = open("input8.txt")
    l=f.readlines()
    l = [word.strip("\n") for word in l]

    tree = {}

    reachedz = False
    directions = l[0]
    l = l[2:]

    for line in l:
        line = line.split("=")
        origin = line[0].strip()
        dests = line[1].strip().replace("(", "").replace(")", "").split(", ")
        dests = (dests[0], dests[1])
        tree[origin] = dests

    i = 0
    count = 0
    curr = "AAA"

    while reachedz == False:
        if i >= len(directions):
            i = 0

        if curr == "ZZZ":
            reachedz = True
            break

        d = directions[i]
        
        if d == "L":
            curr = tree[curr][0]
        else:
            curr = tree[curr][1]

        count += 1
        i += 1


    print(count)

if __name__ == "__main__":
    advent8()