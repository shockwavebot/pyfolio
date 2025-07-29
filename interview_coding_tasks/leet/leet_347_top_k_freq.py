def get_freq(nums: list[int], k: int) -> list[int]:
    import heapq
    ## instead of this block, collections Counter could be used
    freq_dict = {}
    for num in nums:
        if num in freq_dict.keys():
            freq_dict[num] += 1
        else: 
            freq_dict[num] = 1
    ## 
    priority_queue = []
    for num, freq in freq_dict.items():
        heapq.heappush(priority_queue, (freq, num))
    return [t[1] for t in heapq.nlargest(k, priority_queue)]

def get_freq_2(nums: list[int], k: int) -> list[int]:
    from collections import Counter
    return [i for i, _ in Counter(nums).most_common(k)]


if __name__ == '__main__':
    a = [1,1,1,1,1,1,1,2,2,2,2,2,3,3,3]
    k = 2
    res = get_freq(a, k)
    res2 = get_freq_2(a,k)
    print(f"Expected: [1,2], got: {res}")
    print(f"Expected: [1,2], got: {res2} (alt)")
    res = get_freq([-1, -1], 1)
    res2 = get_freq_2([-1, -1], 1)
    print(f"Expected: [-1], got: {res}")
    print(f"Expected: [-1], got: {res2} (alt)")
