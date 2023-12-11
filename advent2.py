def advent2():
    f = open("input2.txt")
    l=f.readlines()
    passable = False
    l = [word.strip("\n") for word in l]
    sum = 0
    colors = {"red":12, "blue":14, "green":13}

    for line in l:
        line = line.split(":")
        gamenum = line[0].split(" ")[1]
        game = line[1]
        game = game.split(";")
        for round in game:
            colors["red"] = 12
            colors["blue"] = 14
            colors["green"] = 13
            pull = round.split(",")
            # print(pull)
            for thing in pull:
                # print(thing)
                thing = thing.strip().split(" ")
                colors[thing[1]] -= int(thing[0])

            print(colors)
            if colors["red"] < 0 or colors["blue"] < 0 or colors["green"] < 0:
                passable = False
                break
            else:
                passable = True
        
        if passable:
            sum += int(gamenum)
        
    print(sum)


if __name__ == "__main__":
    advent2()