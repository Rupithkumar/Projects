def findMaxK(nums: List[int]) -> int:
    #  sure interally memory lekta hai ye
    nums.sort()
    l, r = 0, len(nums) - 1

    while (r > l):
        if (-nums[r] == nums[l]):
            return nums[r]
        elif (-nums[r] > nums[l]):
            l += 1
        else:
            r -= 1

    return -1


with open("user.out", 'w') as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(findMaxK(nums), file=f)

exit(0)