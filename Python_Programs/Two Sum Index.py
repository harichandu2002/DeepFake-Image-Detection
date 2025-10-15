def TwoSuM(nums,target):
    left=0
    right=len(nums)-1
    while left < right:
        checksum=nums[left]+nums[right]
        if checksum==target:
            return [left+1,right+1]
        elif checksum<target:
            left+=1
        else:
            right-=1

    return []


nums = list(map(int,input("Enter the sorted array of Increasing Order: ").split()))
target=int(input("Enter the target variable: "))
result = TwoSuM(nums,target)
print(result)