import sys
input_data = sys.stdin.read().splitlines()
set_a = set(input_data[0].split())
n = int(input_data[1])
result = True
for i in range(2, n + 2):
    other_set = set(input_data[i].split())
    if not (set_a > other_set):
        result = False
        break
print(result)
