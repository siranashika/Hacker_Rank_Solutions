from itertools import groupby
S = input()
for key, group in groupby(S):
    count = len(list(group))
    print(f"({count}, {int(key)})", end=" ")
