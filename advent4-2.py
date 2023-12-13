def advent4():
    f = open("input4.txt")
    l=f.readlines()
    l = [word.strip("\n") for word in l]
    sum = 0

    for line in l:
        wins = 0
        line = line.split(":")[1]
        winners = line.split("|")[0].strip().split(" ")
        numbers = line.split("|")[1].strip().split(" ")

        for num in numbers:
            if num == "":
                continue
            if num in winners:
                wins += 1
        
        wins -= 1
        sum += int(2**wins)

    print(sum)

if __name__ == "__main__":
    advent4()