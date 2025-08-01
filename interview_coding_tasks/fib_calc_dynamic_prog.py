import time 

# Example 1: Fibonacci using Memoization (Top-Down DP)
def fib_memoization(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib_memoization(n-1, memo) + fib_memoization(n-2, memo)
    return memo[n]

# Example 2: Fibonacci using Tabulation (Bottom-Up DP)
def fib_tabulation(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Test the functions
def timer(n:int):
    start = time.perf_counter()
    fib_memoization(n)
    elapsed = time.perf_counter() - start
    print(f"Momoization elapsed for {n}: {elapsed}")

    start = time.perf_counter()
    fib_tabulation(n)
    elapsed = time.perf_counter() - start
    print(f"Tabulation elapsed for {n}: {elapsed}")

timer(500)
