"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""
from typing import List
import heapq
from collections import Counter
from random import randint
from time import perf_counter
from multiprocessing import Pool

class Solution:
    def find_kth_largest_1(nums: List[int], k: int) -> int:
        # amazing performace, for most cases is enough,
        # for large arrays and huge min-max-diff, it's getting slower
        sorted_array = sorted(nums, reverse=True) # O(n long(n))
        return sorted_array[k-1]

    def find_kth_largest_2(nums: List[int], k: int) -> int:
        # using heap
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        print(min_heap)
        return min_heap[0]

    def find_kth_largest_3(nums: List[int], k: int) -> int:
        # counting approach
        # up to reasonable number of min-max-diff (1 mil) it's FASTEST!
        # theoretically, for larger diff, memory could be limitation

        min_val, max_val = min(nums), max(nums) # O(n)
        
        # Create counting array
        count = [0] * (max_val - min_val + 1) # O(k)
        # [0 1 2 3 4 5]
        # [0 0 0 0 0 0]
        
        # Count frequencies
        for num in nums: # O(n)
            count[num - min_val] += 1
        # [0 1 2 3 4 5]
        # [1 2 2 1 2 1]
        
        # Walk from largest to smallest, subtracting counts
        remain = k
        for val in range(len(count) - 1, -1, -1):  # go from max → min (m)
            remain -= count[val]
            if remain <= 0:
                return val + min_val
            
        # Total: 2 * O(n) + O(k) + O(m) >>> O(n)
        # limitation: space complexity array of max_val elements


    def find_kth_largest_4(nums: List[int], k: int) -> int:
        # to overcome memory limitation use hashmap
        # in some cases it could even be fastest solution, when min-max-diff is small (1000)
        # for larger diff,  1 mil, it's the worst performace

        # Step 1: Count frequencies in a hashmap
        freq = Counter(nums)
        
        # Step 2: Get all unique numbers sorted descending
        unique_sorted = sorted(freq.keys(), reverse=True)
        
        # Step 3: Walk through and subtract frequencies
        remain = k
        for val in unique_sorted:
            remain -= freq[val]
            if remain <= 0:
                return val
            
def perf(args):
    f, input = args
    start = perf_counter()
    f(*input)
    perf_time = perf_counter() - start
    return f"Function: {f} time: {perf_time}"

if __name__ == '__main__':
    test_set = [
        {"input": ([3,2,1,5,6,4], 2), "expected": 5},
        {"input": ([3,2,3,1,2,4,5,5,6], 4), "expected": 4},
        {"input": ([21,3,3,4,5,5,6,21,21], 1), "expected": 21},
        {"input": ([0,0,0,0,0,9,9,9], 2), "expected": 9},
    ]

    large_array = [randint(1, 1_000) for _ in range(1_000_000)]
    perf_fns = []

    for name in dir(Solution):
        if '__' not in name:
            fn = getattr(Solution, name)
            perf_fns.append(fn)
            for test in test_set:
                assert fn(*test["input"]), test["expected"]

    # perf comparison
    with Pool(len(perf_fns)) as p:
        res = p.map(perf, [(f, (large_array, 7)) for f in perf_fns])
    for result in res:
        print(result)
