"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
from typing import List


def rem_elem(nums: List[int], val: int) -> int:
    occurancies_indices = []
    nums_len = len(nums)
    for i in range(nums_len):
        if nums[i] == val:
            occurancies_indices.append(i)
    for i in occurancies_indices[::-1]:
        nums.pop(i)
    return nums_len - len(occurancies_indices)


if __name__ == '__main__':
    a = [2,3,3,2]
    assert rem_elem(a, 3) == 2
    assert a == [2,2]
