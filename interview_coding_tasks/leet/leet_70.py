"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""
from math import factorial

def perm_dup(a: list[int]) -> int:
    """
    permutation with duplicates: 
        n!/(n1!x...nx!)
    """
    duplicates = {}
    for i in a:  # O(n)
        if i in duplicates:
            duplicates[i] += 1
        else:
            duplicates[i] = 1
    denom = 1
    for v in duplicates.values(): # O(n)
        denom *= factorial(v)
    return int(factorial(len(a))/denom)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        twos_start = n // 2  # how many 2s?
        ones_start = n % 2  # how many 1s?
        perms = 0
        for i in reversed(range(0, twos_start+1)):
            perms += perm_dup([2]*i + [1]*(2*(twos_start-i) + ones_start))
        return perms

if __name__ == "__main__":
    # print(perm_dup([1, 1, 2]))  # 3
    # Solution().climbStairs(4) # [2, 1, 1] [2,2] [1, 1, 1, 1]
    print(Solution().climbStairs(3)) # 3
    print(Solution().climbStairs(4)) # 5
    print(Solution().climbStairs(5)) # 8
