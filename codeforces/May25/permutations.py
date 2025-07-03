t=int(input())

lst = []
for i in range(t):
    n = int(input())
    if n%2 == 0:
        lst.append(int((n/2)**2+1))
    else:
        lst.append(int((n+1)*(n-1)/4 + 1))

for i in lst:
    print(i)