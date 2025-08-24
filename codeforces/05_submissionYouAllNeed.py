""" def mex(lst):
    i = 0

    while True:
        if i in lst:
            i+= 1
            continue
        break
    
    return i

def sum(lst):
    sum1 = 0
    for i in lst:
        sum1 += i

    return sum1
 """
t = int(input())

output = []
for _ in range(t):
    n = int(input())
    lst = input().split()

    sum2 = 0
    for i in lst:
        sum2 += int(i)

    sum2 += lst.count('0')

    output.append(sum2)

for i in output:
    print(i)

