t = int(input())
output = []

for _ in range(t):
    x = input()

    minNumber = int(x[0])
    for i in x:
        if int(i) < minNumber:
            minNumber = int(i)
        
    output.append(minNumber)

for j in output:
    print(j)

