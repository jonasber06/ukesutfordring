n = 1000

def f(x):
    return x**2

a = 0
b = 5

dx = (b-a)/n
s = 0

for i in range(n):
    xi = a+dx*i
    s+=(f(xi)*dx)

print(s)