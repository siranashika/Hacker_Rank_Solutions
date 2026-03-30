if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    scores = sorted(list(set([x[1] for x in students])))
    second_lowest = scores[1]
    low_names = []
    for s in students:
        if s[1] == second_lowest:
            low_names.append(s[0])
            
    low_names.sort()
    for name in low_names:
        print(name)
