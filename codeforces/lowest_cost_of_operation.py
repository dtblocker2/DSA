# Congrats bro you completed 1 question keep it up next time I want you to complete 2
def XOR(a):
    if a%2 == 0:
        return a+1
    return a-1

def min_cost_transform(m, n, x, y):
    queue = [(m, 0)]
    visited = set()

    while queue:
        min_index = 0
        for i in range(1, len(queue)):
            if queue[i][1] < queue[min_index][1]:
                min_index = i

        current, cost = queue[min_index]
        queue.pop(min_index)

        if current == n:
            return cost

        if current in visited or current > 2 * n:
            continue
        visited.add(current)

        queue.append((XOR(current), cost + y))

        queue.append((current + 1, cost + x))

    return -1

t = int(input())

output = []
for _ in range(t):
    a,b,x,y = map(int, input().split())
    outputs = min_cost_transform(a,b,x,y)
    output.append(outputs)

for i in output:
    print(i)