def MaxSubArray(nums):
    maxcurrsum = maxglobal = nums[0]
    for i in nums[1:]:
        maxcurrsum=max(i,maxcurrsum+i)
        maxglobal=max(maxglobal,maxcurrsum)
    return maxglobal


nums = list(map(int,input("Enter the array elements: ").split()))
maxsum = MaxSubArray(nums)
print("Maximum sum of sub array is ",maxsum)

