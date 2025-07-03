def h(x):
    print(x)
    return x

def g(y):
    print(y)
    return y

def f(x,y):
    print("----------------")
    h(x+1)
    g(y)

f(h(10),g(20))
print("\n")
f(g(20),h(10))3