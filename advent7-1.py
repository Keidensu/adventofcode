import re

def advent7():
    f = open("input7.txt")
    l=f.readlines()
    l = [word.strip("\n") for word in l]

    five = []
    four = []
    drhouse = []
    three = []
    two = []
    one = []
    high = []

    for line in l:
        handsplit= {}
        hand = line.split(" ")[0].replace("A", "Z").replace("K", "Y").replace("Q", "W").replace("J", "V")
        bid = line.split(" ")[1]
        for card in hand:
            if card not in handsplit:
                handsplit[card] = 1
            else:
                handsplit[card] += 1
            
        
        if len(handsplit) == 1:
            five.append((hand, bid))
        elif len(handsplit) == 2:
            if 4 in handsplit.values():
                four.append((hand, bid))
            else:
                drhouse.append((hand, bid))
        elif len(handsplit) == 3:
            if 3 in handsplit.values():
                three.append((hand, bid))
            else:
                two.append((hand, bid))
        elif len(handsplit) == 4:
            one.append((hand, bid))
        else:
            high.append((hand, bid))
        
    final = sorted(high) + sorted(one) + sorted(two) + sorted(three) + sorted(drhouse) + sorted(four) + sorted(five)

    sum = 0

    for i in range(len(final)):
        sum += (i+1) * int(final[i][1])

    print(sum)

if __name__ == "__main__":
    advent7()