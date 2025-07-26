# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

def remove_intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return [list(set1 - set2), list(set2 - set1)]

if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [4, 5, 6, 7, 8]
    expected_answer = [[1,2,3], [6,7,8]]
    answer = remove_intersection(nums1, nums2)
    assert expected_answer == [sorted(answer[0]), sorted(answer[1])], f"{answer}"
