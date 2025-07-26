# merge sorted arrays 
# a1 = [1,2,3,3], a2 = [1,4,5,5]
# 

# version 1 
def merge_sorted_arrays_v1(a1, a2): #O(n^2)
    # O(nlogn) time complexity: sort(a1+a2)
    out = a1
    for i in a2:  # O(n)
        for j,v in enumerate(a1):  # O(n)
            if i < v:
                out.insert(j, i)  # O(n)
                break
        else:
            out.append(i)
    return out
