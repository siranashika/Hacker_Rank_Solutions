if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        line=input().split()
        k=line[0]
        if k=="insert":
            l.insert(int(line[1]),int(line[2]))
        elif k=="remove":
            l.remove(int(line[1]))
        elif k=="sort":
            l.sort()
        elif k=="pop":
            l.pop()
        elif k=="reverse":
            l.reverse()
        elif k=="append":
            l.append(int(line[1]))
        elif k=="print":
            print(l)
