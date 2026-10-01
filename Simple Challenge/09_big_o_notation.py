import time

small_list = list(range(100))
large_list = list(range(10_000_000))

# Test Small
start = time.time()
_ = small_list[50]
print(f"Small access: {time.time() - start}")

# Test Large
start = time.time()
_ = large_list[5_000_000]
print(f"Large access: {time.time() - start}")