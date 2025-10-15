def RomanToInteger(r):
    romanmap={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    total = 0
    preval=0
    for i in reversed(r):
        val=romanmap[i]
        if val<preval:
            total-=val
        else:
            total+=val
            preval=val
    return total

r = input("Enter the Roman Number: ")
print(RomanToInteger(r))