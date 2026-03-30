from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())
all_groups = list(combinations(letters, k))
count_with_a = 0
for group in all_groups:
    if 'a' in group:
        count_with_a += 1
probability = count_with_a / len(all_groups)
print(round(probability, 4))
