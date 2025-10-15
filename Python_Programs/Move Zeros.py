def MoveZeros(nums):
    for i in range(len(nums)):
        if nums[i]==0:
            nums.append(nums[i])
            nums.remove(nums[i])
    return nums

nums = list(map(int,input("Enter the array of numbers: ").split()))
print(MoveZeros(nums))

