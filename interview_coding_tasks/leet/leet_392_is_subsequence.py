"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative 
positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""
def is_subseq(s:str, t:str) -> bool:
    if s == "":
        return True
    s_index = 0
    t_index = 0
    while t_index < len(t):
        if s[s_index] == t[t_index]:
            s_index += 1
            if s_index == len(s):
                return True
        t_index += 1
    return False

if __name__ == '__main__':
    assert is_subseq("abc", "ahbgdc")
    assert not is_subseq("axc", "ahbgdc")
    assert is_subseq("", "ahbgdc")
