list = [1, 5, 10, 0, 4, 6, 20, 7]


def var(list):
    s = []
    for index in list:
        if index % 2 == 0:
            s.append(index)
        
    return s
print(var(list))


