str = sorted({'c':1,'b':2,'a':3})
print(str)


for x in enumerate([2,4,6,8]):
	print(x)
	
a = range(10)
print(a)
print(type(a))

g = (i for i in range(10))

print(next(g))
print(g)
