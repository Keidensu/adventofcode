import re

def advent6():
    f = open("input6.txt")
    l=f.readlines()
    l = [word.strip("\n") for word in l]

    times = re.split("\s+", l[0])[1:]
    distances = re.split("\s+", l[1])[1:]

    sum = 1

    for i in range(len(times)):
        wins = 0
        for k in range(int(times[i])):
            speed = k
            timegoing = int(times[i]) - k
            distance = timegoing * speed
            if distance > int(distances[i]):
                wins += 1
        sum *= wins

    print(sum)

if __name__ == "__main__":
    advent6()