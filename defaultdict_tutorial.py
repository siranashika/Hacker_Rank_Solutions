from collections import defaultdict
import sys
input_data = sys.stdin.read().split()
n = int(input_data[0])
m = int(input_data[1])
d = defaultdict(list)
for i in range(1, n + 1):
    d[input_data[i + 1]].append(str(i))
for j in range(n + 2, n + m + 2):
    word = input_data[j]
    if word in d:
        print(" ".join(d[word]))
    else:
        print("-1")
