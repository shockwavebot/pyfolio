"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
"""

PICKED = 1

# Given API:
# def guess(num: int) -> int:
def guess(num: int) -> int:
    # let's assume picked number to get from globals
    picked_number = PICKED
    if num == picked_number:
        return 0
    elif num < picked_number:
        return 1
    else:
        return -1

class Solution():
    def guess_number_non_recursive(n: int) -> int:
        first, last = 1, n
        while first <= last:
            mid = first + (last - first) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                last = mid - 1
            else:
                first = mid + 1
        return -1
    
    def guess_number_recurs(n: int) -> int:
        def num(i,n):
            mid=(n+i)//2
            if guess(mid)==0:
                return mid
            if guess(mid)==-1:
                return num(i,mid-1)
            else:
                return num(mid+1,n)
        return num(1,n)
    

if __name__ == '__main__':
    PICKED = 6
    assert Solution.guess_number_non_recursive(10) == 6
    assert Solution.guess_number_recurs(10) == 6
