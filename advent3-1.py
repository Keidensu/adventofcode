import re

def advent3():
    f = open("input3.txt")
    l=f.readlines()
    l = [word.strip("\n") for word in l]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "/", "+", "="]
    sum = 0



    for i in range(len(l)):
        nums = dict((m.start(), m.group()) for m in re.finditer(r'\d+', l[i]))
        syms = dict((m.start(), m.group()) for m in re.finditer(r'[^0-9\.]', l[i]))
        symsdown = {}
        symsup = {}

        if i != len(l) - 1:
            symsdown = dict((m.start(), m.group()) for m in re.finditer(r'[^0-9\.]', l[i+1]))

        if i != 0:
            symsup = dict((m.start(), m.group()) for m in re.finditer(r'[^0-9\.]', l[i-1]))
        
        for num in nums:
            begin = num - 1
            end = num + len(nums[num]) + 1
            for k in range(begin,end):
                if k in syms or k in symsdown or k in symsup:
                    sum += int(nums[num])
                    # print(nums[num])
                    break

    print(sum)

if __name__ == "__main__":
    advent3()