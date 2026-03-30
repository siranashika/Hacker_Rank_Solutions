n_a = int(input())
set_a = set(map(int, input().split()))
n_ops = int(input())
for _ in range(n_ops):
    operation_name = input().split()[0]
    other_set = set(map(int, input().split()))    
    if operation_name == "intersection_update":
        set_a.intersection_update(other_set)
    elif operation_name == "update":
        set_a.update(other_set)
    elif operation_name == "symmetric_difference_update":
        set_a.symmetric_difference_update(other_set)
    elif operation_name == "difference_update":
        set_a.difference_update(other_set)
print(sum(set_a))
