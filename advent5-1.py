import re

def advent5():
    f = open("input5.txt")
    l=f.read().strip().replace('\n',' ').split(":")
    seeds = {}
    seedtosoil = {}
    soiltofert = {}
    ferttowater = {}
    watertolight = {}
    lighttotemp = {}
    temptohumidity = {}
    humiditytoloc = {}

    for line in l:
        line = re.sub('[^0-9+\s+]', '', line).strip().split(" ")
        print(line)


    # print(s)

if __name__ == "__main__":
    advent5()