list = [1, 5, 10, 0, 4, 6, 20, 7]
def var(list):
    for el in list:
        el_1 = max(list)
        a = (list.index(el_1))
        list.remove(el_1)

        el_2 = min(list)
        b = (list.index(el_2))
        list.remove(el_2)


        list.insert(a-1, el_2)
        list.insert(b, el_1) 
        return list

print(var(list))

