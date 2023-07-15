def wiggleSort(nums):
    length = len(nums)
    middle = length // 2

    nums.sort()

    # Get largest half for even indexes
    largest = nums[middle::-1]
    nums[::2] = largest

    # Get smallest half for odd indexes
    smallest = nums[:middle:-1]
    nums[1::2] = smallest

    return nums




nums = [1,5,1,1,6,4]
# print(wiggleSort(nums))

print(nums[4::-1])