import time
import random
import string


def find_removable_indices(str1, str2):
    result = []
    for i in range(len(str1)):
        if i >= len(str2):
            result.append(i)
        if str1[i] != str2[i]:
            split_char = str1[i]
            if str1[i+1:] == str2[i:]:
                result.append(i)
                for j in range(1,i +1):
                    if str1[i-j] == split_char:
                        result.append(i-j)
                    else:
                        break
                break
    return result if result else [-1]

def find_removable_indices_unopt(str1, str2):
    result = []

    for i in range(len(str1)):
        if str1[:i] + str1[i+1:] == str2:
            result.append(i)

    return result if result else [-1]

def generate_large_test_case(size=10**6, inserted_char='x'):
    # Generate a random base string of given size
    base_str = ''.join(random.choices(string.ascii_lowercase, k=size))
    
    # Pick a random index to insert an extra character
    insert_index = random.randint(0, size)
    
    str1 = base_str[:insert_index] + inserted_char + base_str[insert_index:]
    str2 = base_str
    
    return str1, str2, insert_index


def run_performance_test():
    size = 10**6  # 1 million characters
    print(f"Generating test case with string size: {size}...")

    str1, str2, expected_index = generate_large_test_case(size)

    print("Running performance test...")
    start_time = time.time()
    result = find_removable_indices(str1, str2)
    end_time = time.time()

    print(f"Execution Time: {end_time - start_time:.4f} seconds")
    print(f"Number of valid indices: {len(result)}")
    print(f"Expected index (should be in result): {expected_index}")
    print(f"First 5 indices (if any): {result[:5]}")


if __name__ == "__main__":
    run_performance_test()
