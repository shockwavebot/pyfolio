def fib_calc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_calc(n-1) + fib_calc(n-2)

print(fib_calc(10)) # 55
print(fib_calc(30)) # 832040
print(fib_calc(37)) # 24157817 😱 24 mil !!!
print(fib_calc(50)) # couldn't calculate

# with dynamic programming
# implement cache to store results of subproblems
# memoization
# O(n) time complexity

CACHE = {0: 0, 1: 1}
def fib_calc_dyn(n):
    if n in CACHE:
        return CACHE[n]
    else:
        CACHE[n] = fib_calc_dyn(n-1) + fib_calc_dyn(n-2)
        return CACHE[n]

fib_calc_dyn(500) # 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
