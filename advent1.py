def findpair(line):
    help_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    d = {}
    dr = {}
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numerics = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for num in numbers:
        if line.find(num) > -1:
            d[num] = line.find(num)

    for num in numbers:
        if line.rfind(num) > -1:
            dr[num] = line.rfind(num)
    
    mi = min(d.values())
    ma = max(dr.values())

    keysd = list(d.keys())
    valsd = list(d.values())

    keysdr = list(dr.keys())
    valsdr = list(dr.values())

    pos_min = valsd.index(mi)
    pos_max = valsdr.index(ma)
    
    mi = keysd[pos_min]
    ma = keysdr[pos_max]

    if mi in numerics:
        mi = help_dict[mi]
    if ma in numerics:
        ma = help_dict[ma]

    pair = mi + ma
    return pair

def advent1():
    f = open("input1.txt")
    nums = []
    l = f.readlines()
    for line in l:
        nums.append(findpair(line))
    
    sum = 0
    for num in nums:
        sum += int(num)
    
    print(sum)

if __name__ == "__main__":
    advent1()
