import interval as itv

# copy
x = itv.interval(1., 2.)
y = itv.interval(3., 4.)
z = itv.interval(1.)
print(x)
print(y)
print(z)

# basic four operations
print("basic four operations")
print(x+y)
print(x-y)
print(x*y)
print(x/y)

# compound assignment operator
print("compound assignment operator")
x = itv.interval(1., 2.)
x += y
print(x)
x = itv.interval(1., 2.)
x -= y
print(x)
x = itv.interval(1., 2.)
x *= y
print(x)
x = itv.interval(1., 2.)
x /= y
print(x)

# access to endpoints
z = itv.interval(1.0, 3.0)
print("access to endpoints")
print(z.lower)
print(z.upper)
z.lower = 3.5
z.upper = 4.5
print(z)

#sqrt
print("sqrt")
z = itv.interval(2.)
print(itv.interval.sqrt(z))

print("calculation(x^2+2x-8=0)")
a = itv.interval(1.)
b = itv.interval(2.)
c = itv.interval(-8.)
print(itv.interval(2.)*c / ((itv.interval(0.)-b) - itv.interval.sqrt(b*b-itv.interval(4.)*a*c)))