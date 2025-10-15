def prod(nums):
    temp=1
    for i in range(len(nums)):
        temp=temp*nums[i]
    ar=[]
    for j in range(len(nums)):
        t=temp//nums[j]
        ar.append(t)
    return ar

nums = list(map(int,input("Enter the array of numbers: ").split()))
print(prod(nums))
