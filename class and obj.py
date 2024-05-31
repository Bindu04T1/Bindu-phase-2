def performBubblesort(nums):
    n=len(nums)
    FixThisIndex=n-1
    while fixthisIndex>0:
        for index in range(fixThisIndex): 
            If nums[index]>nums[index+1]
               temp=nums[index]
               nums[index]=nums[index+1]
               nums[Index+1]=temp
            print(nums)
            FixThisIndex--1
nums-list(map(int, input("enter list:").split()))
print("Before sorting:",nums)
performBubblesort(nums)
print("After Sorting:",nums)