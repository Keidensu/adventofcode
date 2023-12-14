import re

def advent5():
    f = open("input5.txt")
    l=f.readlines()
    l = [word.strip("\n") for word in l]

    games = {}

    sum = 0

    for line in l:
        line = line.strip().split(":")
        gamenum = int(re.split("\s+", line[0])[1])
        
        if gamenum not in games:
            games[gamenum] = 1
        else:
            games[gamenum] += 1
        
        wins = 0
        winners = line[1].split("|")[0].strip().split(" ")
        numbers = line[1].split("|")[1].strip().split(" ")

        for num in numbers:
            if num == "":
                continue
            if num in winners:
                wins += 1
        
        
        for i in range(1, wins+1):
            for k in range(games[gamenum]):
                if gamenum+i not in games:
                    games[gamenum+i] = 1
                else:
                    games[gamenum+i] += 1
                
        
    print(games)
        
    for num in games:
        sum += games[num]

    print(sum)

if __name__ == "__main__":
    advent5()