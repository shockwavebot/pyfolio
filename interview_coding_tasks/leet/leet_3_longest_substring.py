'''
Given a string s, find the length of the longest substring without duplicate characters.

'''
import random
from time import perf_counter
from string import ascii_lowercase

def longest_substring(s: str) -> int: # O(n^2)
    if len(s) < 2:
        return len(s)
    max = 0
    for i in range(len(s)):
        for j in range(len(s)-i):
            sub = s[i:i+j+1]
            print(sub)
            if len(set(sub)) == len(sub) and len(sub) > max:
                max = len(sub)
    print(max)

def longest_substring_v2(s: str) -> int: # O(n)
    uniq = set()
    i_first = 0
    max = 0
    for i, ch in enumerate(s):
        if ch not in uniq:
            uniq.add(ch)
            if len(uniq) > max:
                max = len(uniq)
        elif s[i-1] == s[i]:
            i_first = i
            uniq = set([ch])
        else:
            start_i = i-len(uniq)
            sub = s[start_i:i-1]
            i_first = start_i + sub.find(ch)
            uniq = set(s[i_first:i])
    return max

def v3(s):
    # Create a set to store characters in current window
    char_set = set()
    max_length = 0
    left = 0
    
    # Iterate through string with right pointer
    for right in range(len(s)):
        # While we find a duplicate, remove chars from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # Add current character to set
        char_set.add(s[right])
        # Update max_length if current window is larger
        max_length = max(max_length, right - left + 1)
    
    return max_length

if __name__ == '__main__':
    assert longest_substring_v2('') == 0
    assert longest_substring_v2('a') == 1
    assert longest_substring_v2('aaaaaaaa') == 1
    assert longest_substring_v2('abc') == 3
    assert longest_substring_v2('abcabca') == 3
    assert longest_substring_v2("pwwkew") == 3
    assert longest_substring_v2("ckilbkd") == 5

    assert v3('') == 0
    assert v3('a') == 1
    assert v3('aaaaaaaa') == 1
    assert v3('abc') == 3
    assert v3('abcabca') == 3
    assert v3("pwwkew") == 3
    assert v3("ckilbkd") == 5

    size = 1_000_000
    s = ''.join(random.choices(ascii_lowercase, k=size))

    start = perf_counter()
    res = longest_substring_v2(s)
    duration = perf_counter() - start
    print(f"v2 duration: {duration}")

    start = perf_counter()
    res = v3(s)
    duration = perf_counter() - start
    print(f"v3 duration: {duration}")
