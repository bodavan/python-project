def value(r):
    if (r == "I"):
        return 1
    if (r == "V"):
        return 5
    if (r == "X"):
        return 10
    if (r == "L"):
        return 50
    if (r == "C"):
        return 100
    if (r == "D"):
        return 500
    if (r == "M"):
        return 1000

def romantoint(rom):
    res = 0
    i = 0
    while (i<len(rom)):
        s1 = value(rom[i])

        if (i + 1 < len(rom)):

            s2 = value(rom[i + 1])

            if (s1 >= s2):
                res = res + s1
                i = i + 1

            else:
                # (s2>=s1)
                res = res + s2 - s1
                i = i + 2

        else:
            res = res + s1
            i = i + 1
    return res
print("your roman num is : ",end="")
ro=input()
print('Numaric num: ',romantoint(ro))