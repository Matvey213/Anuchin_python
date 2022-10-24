def  find_sum(i):
    return sum(i)

i = list()
for u in range(10):
    i.append(int(input('введи число: ')))

print(find_sum(i))





def find_zero(i):
    s = 0
    for el in i:
        if el == 0:
            s += 1 
    return s 

i = list()
for u in range(10):
    i.append(int(input('введи число: ')))
print(i)

print(find_zero(i))





def stairs(a):
    for i in range(1, a+1):
        m = ''
        for j in range(1, i+1):
            m += str(j)
        print(m)

    return 

a = 0
a = int(input('введи число: '))

print(stairs(a))
  



n = int(input('Введите натуральное число: '))
for i in range(1, n+1):
    for a in range(1, n+1-i):
        print(' ', end = '')
    for b in range(1, i+1):
        print(b, end = '')
    for c in range(i-1, 0, -1):
        print(c, end = '')
    print()