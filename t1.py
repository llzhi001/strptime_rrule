__author__ = 'llzhi'
def triangle(n):
    for i in range(n+1):
        print((' *'*i).center(2*n+1))
# triangle(10)
def lrsort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if (nums[j]%2==0) & (nums[j + 1]%2==1):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
# print(lrsort([1,2,3,4,5,6]))