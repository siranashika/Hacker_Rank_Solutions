import re
def check_float():
    try:
        t = int(input())
    except EOFError:
        return
    pattern = r'^[+-]?[0-9]*\.[0-9]+$'
    for i in range(t):
        try:
            s = input()
            if re.match(pattern, s):
                float(s)
                print(True)
            else:
                print(False)
        except ValueError:
            print(False)
if __name__ == "__main__":
    check_float()
