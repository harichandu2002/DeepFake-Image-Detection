def countpairs(n,nums,t):
    count=0
    for i in range(n):
        for j in range(n):
            if i<j and nums[i]+nums[j]==t:
                count+=1
    return count

n=int(input("Enter the size of the array: "))
nums = list(map(int,input("Enter the array of numbers: ").split()))
t=int(input("Enter the target variable: "))
print(countpairs(n,nums,t))
