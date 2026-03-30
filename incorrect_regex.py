import re
import sys
t_str = sys.stdin.readline().strip()
if t_str:
    t = int(t_str)
    for i in range(t):
        s = sys.stdin.readline().strip()
        try:
            re.compile(s)
            print(True)
        except re.error:
            print(False)
