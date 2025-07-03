def lol():
    n, m = map(int,input().split())
    words = [input() for _ in range(n)]
    x=0
    y=0

    for i in range(n):
        if x + len(words[i]) > m:
            break
        else:
            x += len(words[i])
            y += 1
    return y
output = []
t = int(input())
for _ in range(t):
    output.append(lol())

for x in output:
    print(x)