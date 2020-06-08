def ex2(nums):
    product = 1
    for n in nums:
        product *= n

    return [product // n for n in nums]