def advent6():
    f = open("input6.txt")
    l=f.readlines()
    l = [word.strip("\n") for word in l]

    for line in l:
        