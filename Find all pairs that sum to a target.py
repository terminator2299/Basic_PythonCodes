#BruteForce

def find_pairs(arr, target):
    pairs = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs


#Optimized approach
def find_pairs_optimized(arr, target):
    seen = set()
    pairs = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))  # Sorted to avoid duplicates
        seen.add(num)

    return list(pairs)

