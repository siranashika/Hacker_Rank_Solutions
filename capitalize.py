def solve(s):
    words = s.split(' ')
    result = [word.capitalize() for word in words]
    return ' '.join(result)
