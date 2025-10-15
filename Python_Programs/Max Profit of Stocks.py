def price(p):
    mp=0
    for i in range(len(p)):
        for j in range(i,len(p)):
            if p[j]-p[i]>mp:
                mp=p[j]-p[i]
    return mp
    
p = list(map(int,input("Enter the day wise stock prices: ").split()))
profit = price(p)
print(profit)