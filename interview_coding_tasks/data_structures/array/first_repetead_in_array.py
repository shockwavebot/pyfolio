def first_repeated(nums):
    checked = set()
    for num in nums: # O(1)
        if num in checked: # O(1) for set()
            return num
        checked.add(num) # O(1) for set()
    return None
