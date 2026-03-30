import sys
input_data = sys.stdin.read().split()
if input_data:
    t = int(input_data[0])
    pointer = 1
    for _ in range(t):
        n_a = int(input_data[pointer])
        set_a = set(input_data[pointer + 1 : pointer + 1 + n_a])
        pointer += 1 + n_a        
        n_b = int(input_data[pointer])
        set_b = set(input_data[pointer + 1 : pointer + 1 + n_b])
        pointer += 1 + n_b       
        print(set_a.issubset(set_b))
