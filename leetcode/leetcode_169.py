def majorityElement(nums):
    max_nums = max(nums)
    lst = [0] * (max_nums + 1)
    for i in nums:
        lst[i] += 1
    return lst.index(max(lst))

def majorityElement2(nums):
    num_list = list(set(nums))
    ans = 0
    count = 0
    for i in num_list:
        tmp = nums.count(i)
        if tmp > count:
            count = tmp
            ans = i
    return ans

i = 3
nums = [3,2,3]
majorityElement2(nums)
