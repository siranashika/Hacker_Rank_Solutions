import sys
t = int(sys.stdin.readline())
for i in range(t):
    try:
        line = sys.stdin.readline().split()
        if not line:
            break
        a, b = line
        print(int(a) // int(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)
