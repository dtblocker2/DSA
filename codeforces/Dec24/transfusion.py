#no oftest cases
t = int(input('no of tests'))

output = []
p = 1

while p <= t:
    n = int(input('no of int'))
    integers = input('enter integers')
    value = integers.split()
    values = []
    for x in value:
        values.append(int(x))
    if len(values) == n:
        y = 0
        for i in values:
            y += i

        if y%n != 0:
            output.append('NO')
        else:
            while (2*i-1) < len(le)
            output.append('YES')
        p += 1
    else:
        print('re-enter values')

print(output)