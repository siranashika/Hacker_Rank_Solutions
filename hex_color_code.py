import re
n = int(input())
in_block = False
for _ in range(n):
    line = input()    
    if '{' in line:
        in_block = True
    elif '}' in line:
        in_block = False
    elif in_block:
        matches = re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}(?=[;,\s)])', line)
        for match in matches:
            print(match)
