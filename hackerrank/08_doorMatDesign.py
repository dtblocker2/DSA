n, m = map(int, input().split())

# Top part
for i in range(n // 2):
    pattern = '.|.' * (2 * i + 1)
    print(pattern.center(m, '-'))

# Center line
print('WELCOME'.center(m, '-'))

# Bottom part
for i in range(n // 2 - 1, -1, -1):
    pattern = '.|.' * (2 * i + 1)
    print(pattern.center(m, '-'))
