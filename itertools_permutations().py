from itertools import permutations
s, k = input().split()
s = sorted(s)
result = list(permutations(s, int(k)))
for p in result:
    print("".join(p))
