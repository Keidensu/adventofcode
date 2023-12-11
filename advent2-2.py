def advent2():
    f = open("input2.txt")
    l=f.readlines()
    passable = False
    l = [word.strip("\n") for word in l]
    sum = 0
    colors = {"red":0, "blue":0, "green":0}

    for line in l:
        colors["red"] = 0
        colors["blue"] = 0
        colors["green"] = 0
        line = line.split(":")
        game = line[1]
        game = game.split(";")
        for round in game:
            pull = round.split(",")
            for thing in pull:
                thing = thing.strip().split(" ")
                if colors[thing[1]] < int(thing[0]):
                    colors[thing[1]] = int(thing[0])
        
        sum += (colors["red"] * colors["blue"] * colors["green"])
        
    print(sum)


if __name__ == "__main__":
    advent2()