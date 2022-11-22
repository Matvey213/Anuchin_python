list_1 = [1, 5, 10, 0, 4, 6, 20, 7]
list_2 = [ 1, 5, 8, 6]
list=(input("список из предложенных: "))

def var(list): 
    
    s = []
    for i in range(len(list)-1):
        a = (list[i])
        i += 1
        b = (list[i])
        if b > a:
            s.append(b)
        
    
    return s


if  list == "list_1":
    print(var(list_1)) 

elif list == "list_2" :
    print(var(list_2))

else:
    print("введен не тот список ")