import re
n = int(input())
pattern = r'^([a-zA-Z][\w\s]*) <([a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3})>$'
for _ in range(n):
    line = input()
    if re.match(pattern, line):
        print(line)
