import re
def is_valid_uid(uid):
    if len(uid) != 10:
        return False
    if not uid.isalnum():
        return False
    if len(set(uid)) != 10:
        return False
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False
    if len(re.findall(r'[0-9]', uid)) < 3:
        return False
    return True
for _ in range(int(input())):
    uid = input()
    print("Valid" if is_valid_uid(uid) else "Invalid")
