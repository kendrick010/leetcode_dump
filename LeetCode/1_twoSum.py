def twoSum(nums, target):
    cache = {}

    for index, num in enumerate(nums):
        difference = target - num
        cache.update({difference: index})

    for index, num in enumerate(nums):
        try:
            result = cache[num]
        except KeyError:
            continue
            
        if index != result and target - num in nums:
            return [index, result]
        

# # Hashmap
# cache = {}

# for index, num in enumerate(nums):
#     difference = target - num

#     if difference in cache:
#         return [index, cache[difference]]
    
#     cache.update({num: index})