t = int(input(""))
lst = []
for _ in range(t):
    n = int(input(""))
    k = input()
    if '0 0' in k:
        lst.append("YES")
    elif k.count("1") > n-1:
        lst.append("YES")
    else:
        lst.append("NO")

for i in lst:
    print(i)