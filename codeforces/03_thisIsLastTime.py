t = int(input())

output=[]
for _ in range(t):
    n,k = map(int, list(input().split()))
    casinos=[]
    stack = []
    visitedCells = []
    maxValue = k
    z = []
    for i in range(n):
        casinos.append(input().split())
    # print(casinos)

    for j in casinos:
        if (k <= int(j[1])) and (k >= int(j[0])):
            if int(j[2]) > k:
                k = int(j[2])
            stack.append(int(j[2]))
            visitedCells.append(j)

    while stack:
        kTemporary = stack.pop()
        if kTemporary>k:
            k = kTemporary
        for j in casinos:
            if (kTemporary <= int(j[1])) and (kTemporary >= int(j[0])):
                if int(j[2]) > k:
                    k = int(j[2])
                if j not in visitedCells:
                    stack.append(int(j[2]))
                    visitedCells.append(j)
    output.append(k)

for i in output:
    print(i)

""" This answer has big time complexity learn to simplify it even though it might be correct """