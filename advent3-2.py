import re

def advent3():
    f = open("input3.txt")
    l=f.readlines()
    l = [word.strip("\n") for word in l]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "/", "+", "="]
    sum = 0
    adj = 0
    gear = False

    for i in range(len(l)):
        nums = dict(((m.start(), len(m.group())+m.start()), m.group()) for m in re.finditer(r'\d+', l[i]))
        syms = dict((m.start(), m.group()) for m in re.finditer(r'[^0-9\.]', l[i]))
        numsdown = {}
        numsup = {}

        if i != len(l) - 1:
            numsdown = dict(((m.start(), len(m.group())+m.start()), m.group()) for m in re.finditer(r'\d+', l[i+1]))

        if i != 0:
            numsup = dict(((m.start(), len(m.group())+m.start()), m.group()) for m in re.finditer(r'\d+', l[i-1]))

        for sym in syms:
            nodupes = {""}
            nodupes.clear()
            adj = 0
            begin = sym - 1
            end = sym + 2
            for num in nums:
                for k in range(begin,end):
                    if k in range(num[0], num[1]):
                        if nums[num] not in nodupes:
                            nodupes.add(nums[num])
                            adj += 1
            for numd in numsdown:
                for k in range(begin,end):
                    if k in range(numd[0], numd[1]):
                        if numsdown[numd] not in nodupes:
                            nodupes.add(numsdown[numd])
                            adj += 1
                            
            for numu in numsup:
                for k in range(begin,end):
                    if k in range(numu[0], numu[1]):
                        if numsup[numu] not in nodupes:
                            nodupes.add(numsup[numu])
                            adj += 1

            if adj == 2:
                ratio = 1
                for gear in nodupes:
                    ratio *= int(gear)
                
                sum += ratio

    print(sum)

if __name__ == "__main__":
    advent3()