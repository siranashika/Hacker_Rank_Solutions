def wrapper(f):
    def fun(l):
        standardized_list = []
        for number in l:
            clean_number = number[-10:]
            formatted = "+91 " + clean_number[:5] + " " + clean_number[5:]
            standardized_list.append(formatted)
        return f(standardized_list)
    return fun
