nums = [31,-41,59,26,-53,58,97,-93,-23,84]

for i in range(1, len(nums)):
    if nums[i-1] > 0:
        nums[i] += nums[i-1]

'''
https://www.youtube.com/watch?v=2MmGzdiKR9Y
'''