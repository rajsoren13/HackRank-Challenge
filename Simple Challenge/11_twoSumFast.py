def two_sum_fast(nums, target):
    print("\n--- FAST Solution: O(n) ---")
    print("Strategy: Use a dictionary to remember what we've seen")
    print("          For each number, check if its 'complement' was seen before")
    print(f"          complement = target - current number\n")

    seen = {}   # stores: number → index

    for i, num in enumerate(nums):
        complement = target - num
        print(f"  step {i+1}: current number = {num}")
        print(f"           complement needed = {target} - {num} = {complement}")
        print(f"           seen so far = {seen}")

        if complement in seen:   # O(1) — hash lookup, NOT a loop
            print(f" {complement} IS in seen! Return [{seen[complement]}, {i}]")
            return [seen[complement], i]
        else:
            print(f"  {complement} not in seen yet. Add {num} → index {i} to seen.")
            seen[num] = i

            print(f"  {i}={seen[num]}==> {seen} to seen.")
        print()

    return []



nums=[12,7,11,2]
target=9
result_fast = two_sum_fast(nums, target)
print(f"Answer: {result_fast}")
print("→ O(n): one loop, dictionary lookup inside is O(1)")
print("        Total = n × O(1) = O(n)")