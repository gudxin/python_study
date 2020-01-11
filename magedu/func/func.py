# def fn(x, y, *arg, **kwargs):
	# print(x)
	# print(y)
	# print(arg)
	# print(kwargs)
	# print('***********************')
	
# fn(3,5)
# fn(3,5,7,9,a='1',b = 'python')
# fn(3,5,7)


# def fn1(*arg,x,y,**kwargs):
	# print(x)
	# print(y)
	# print(arg)
	# print(kwargs)
	# print('***********************')
	
# fn1(3,5,7)
# fn1(3,5,a=1,b='python')
# 上面的都是错误的,缺少x,y的赋值
# fn1(3,5,x=7,y=9,a=1,b='python')


# def add(x,y):
	# print(x+y)

# add((1,2)[0],[3,1][1])


def fn(x,y,*args):
	print("max = {}".format(max(args)))
	print("min = {}".format(min(args)))
	return max(args),min(args)
	
fn(1,3,4,5,6,7)


def drawnums(x,i=1,j=1):
	while i <= x:
		j = 1
		print('\t'*(x-i),end='\t')
		while j <= i:
			print("{}".format(i-j+1),end='\t')
			j += 1 
		print()
		
		i += 1
		
drawnums(5)


#进阶打印出合适的宽度
def show(n):
	tail = " ".join([str(i) for i in range(n,0,-1)])
	width = len(tail)
	for i in range(1,n):
		print("{:>{}}".format(" ".join([str(j) for j in range(i,0,-1)]),width))
	print(tail)

show(20)


def show1(n):
	head = " ".join([str(i) for i in range(n,0,-1)])
	print(head)
	width = len(head)
	for j in range(width):
		if head[j] == ' ':
			print(' '*j,head[j+1:])
	
	
show1(20)


def fn(x):
	for i in range(x):
		if(x>3):
			break
	else:
		print("hello")
		
fn(3 )


x = 5
def counter():
	y = x + 1   #会报错，因为在局部重新定义了x，不管前后，都会报错未定义就使用
	x += 1
	return x

counter()
	
	

	



































