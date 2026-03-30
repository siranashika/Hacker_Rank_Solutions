def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s1=""
        for c in string[i:i+k]:
            if c not in s1:
                s1+=c
        print(s1)
