from itertools import product
k, m = map(int, input().split())
all_lists = []
for _ in range(k):
    row = list(map(int, input().split()))[1:]
    squared = [x**2 for x in row]
    all_lists.append(squared)
results = []
for combo in product(*all_lists):
    total = sum(combo) % m
    results.append(total)
print(max(results))
