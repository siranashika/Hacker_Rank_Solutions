from collections import deque
for _ in range(int(input())):
    n = int(input())
    d = deque(map(int, input().split()))   
    last_picked = float('inf')
    possible = True    
    while d:
        if d[0] >= d[-1]:
            current = d.popleft()
        else:
            current = d.pop()            
        if current > last_picked:
            possible = False
            break
        last_picked = current       
    print("Yes" if possible else "No")
