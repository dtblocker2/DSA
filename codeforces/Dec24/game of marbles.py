#no of tests
output = []
t = int(input())
p = 1
while p < t:
    points = 0
    #no of marbles
    n = int(input())
    #color of marbles
    marbles = input()
    value = marbles.split()
    values = []
    for x in value:
        values.append(int(x))
    t = 0
    lst_2 = []
    while t <= (n-1):
        lst_2.append(values[t])
        t += 2
    set_1 = set(lst_2)
    points += len(set_1)

    lst = []
    k=1
    while (2*k-1) <= (n-1):
        lst.append(values[2*k-1])
        k+=1
    set_2 = set(values)
    set_3 = set(lst)
    points += len(set_2)-len(set_3)
    output.append(points)
    p += 1

for x in output:
    print(x)