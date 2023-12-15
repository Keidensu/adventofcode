import re

def advent6():
    f = open("input6.txt")
    l=f.readlines()
    l = [word.strip("\n") for word in l]

    time = re.split(":", l[0])[1].replace(" ", "")
    distance = re.split(":", l[1])[1].replace(" ", "")

    sum = 0

    for k in range(int(time)):
        timegoing = int(time) - k
        dist = timegoing * k
        if dist > int(distance):
            sum += 1

    print(sum)

if __name__ == "__main__":
    advent6()