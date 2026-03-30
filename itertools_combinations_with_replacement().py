from itertools import combinations_with_replacement
s, k = input().split()
s = sorted(s)
result = combinations_with_replacement(s, int(k))
for item in result:
    print("".join(item))
