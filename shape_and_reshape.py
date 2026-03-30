import numpy
input_list = list(map(int, input().split()))
my_array = numpy.array(input_list)
print(numpy.reshape(my_array, (3, 3)))
