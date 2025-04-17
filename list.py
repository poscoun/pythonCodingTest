# 완전탐색 O(n^2)
def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
    return False
print(twoSum(nums=[2,1,5,7], target=14))

# sort
def twoSum2(nums, target):
    # O(nlogn)
    nums.sort()
    l, r = 0, len(nums)-1

    # O(n)
    while l<r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] == target:
            return True
    return False
print(twoSum2(nums=[4,1,9,7,5,3,16], target=14))