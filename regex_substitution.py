import re
def transform(match):
    if match.group(0) == '&&':
        return 'and'
    return 'or'
n = int(input())
for _ in range(n):
    line = input()
    while ' && ' in line or ' || ' in line:
        new_line = re.sub(r'(?<= )(&&|\|\|)(?= )', transform, line)
        if new_line == line:
            break
        line = new_line
    print(line)
