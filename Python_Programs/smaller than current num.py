def smaller(n):
    lst=[]
    for i in range(len(n)):
        temp=0
        for j in range(len(n)):
            if n[i]>n[j]:
                temp+=1
        lst.append(temp)

    return lst

n = list(map(int,input("Enter the list of numbers: ").split()))
sm=smaller(n)
print(sm)

