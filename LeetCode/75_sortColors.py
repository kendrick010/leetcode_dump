def sortColors(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    num_reds, num_whites, num_blues = nums.count(0), nums.count(1), nums.count(2)

    for i in range(len(nums)):
        if num_reds > 0:
            nums[i] = 0
            num_reds -= 1
        elif num_whites > 0:
            nums[i] = 1
            num_whites -= 1
        elif num_blues > 0:
            nums[i] = 2
            num_blues -= 1