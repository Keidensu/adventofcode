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
        dests = line[1].strip()
        tree[origin] = dests

    i = 0

    while reachedz == False:
        if i >= len(directions):
            i = 0
        
        

        i += 1



if __name__ == "__main__":
    advent8()

    # left = line[1].split(", ")[0].replace("(", "").strip()
    # right = line[1].split(", ")[1].replace(")", "").strip()