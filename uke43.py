print("")
n = 1000

def f(x):
    return x**2

a = 0
b = 5

dx = (b-a)/n
s = 0

for i in range(n):
    xi = a+dx*i
    s+=(f(xi))
print(s)

s1 = 0
for n in range(n+1):
    xi = a+dx*n
    s1+=f(xi)*dx

integral = (dx/2)*(f(a)+f(b)+2*s1)
print(integral)