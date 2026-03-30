if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    m=max(arr)
    arr.remove(m)
    print(max(arr))
