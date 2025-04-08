def first_repeated(nums):
    checked = set()
    for num in nums:
        if num in checked:
            return num
        checked.add(num)
    return None
