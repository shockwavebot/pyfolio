def rem_stars(s: str) -> str:
    res = []
    for c in s:
        if c == '*':
            if len(res) > 0:
                res.pop()
        else:
            res.append(c)
    return ''.join(res)

if __name__ == '__main__':
    s1 = "leet**cod*e"
    s1_expected = "lecoe"
    s1_res = rem_stars(s1)
    print(f"in: {s1} -> out: {s1_res}")
    assert s1_res == s1_expected
