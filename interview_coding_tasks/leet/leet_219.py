'''Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:


Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:


Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:


Input: nums = [1,2,3,1,2,3], k = 2
Output: false'''




def v1(nums, k):
   for i in range(len(nums)-k):
       for j in range(i+k, len(nums)):
           if nums[i] == nums[j] and abs(i-j) <= k:
               return True
   return False




def v2(nums, k):
   occur = {}
   for i, num in enumerate(nums):
       if num in occur:
           if abs(i - occur[num]) <= k:
               return True
       occur[num] = i
   return False




if __name__ == '__main__':
   assert v1([1, 2, 3, 1], 3)
   assert v1([1, 2, 3, 1, 2, 3], 2) is False
   assert v1([1, 0, 1, 1], 1)


   assert v2([1, 2, 3, 1], 3)
   assert v2([1, 2, 3, 1, 2, 3], 2) is False
   assert v2([1, 0, 1, 1], 1)
