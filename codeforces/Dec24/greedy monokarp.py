#no of tests
output = []
t = int(input())
p = 1
while p <= t:
    op = (input()).split()
    n = int(op[0])
    k = int(op[1])
    #coin in chest
    marbles = input()
    value = marbles.split()
    values = []
    for x in value:
        values.append(int(x))
    values.sort(reverse=True)
 
    x = 0
    for i in values:
        x += i
        if x > k:
            break
        else:
            y = k-x
    output.append(y)
    p += 1
 
for i in output:
    print(i)