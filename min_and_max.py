import numpy
n, m = map(int, input().split())
rows = []
for _ in range(n):
    rows.append(list(map(int, input().split())))
my_array = numpy.array(rows)
min_list = numpy.min(my_array, axis=1)
print(numpy.max(min_list))
