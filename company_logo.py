from collections import Counter
s = sorted(input())
counts = Counter(s).most_common(3)
for char, count in counts:
    print(char, count)
