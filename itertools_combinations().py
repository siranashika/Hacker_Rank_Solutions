from itertools import combinations
s, k = input().split()
s = sorted(s)
for i in range(1, int(k) + 1):
    result = list(combinations(s, i))
    for c in result:
        print("".join(c))
