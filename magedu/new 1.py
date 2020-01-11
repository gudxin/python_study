#一个合数一定可以分解成几个素数的乘积，也就
#是说，一个数如果可以被一个素数整除就是合数
import datetime

start = datetime.datetime.now()
lst = []
count = 1	#2也是素数
flag = False
for i in range(3,10,2):
	up = int(i**0.5)+1
	for j in lst:
		if j >= up:
			flag = False
			break
		if i % j == 0:		#合数
			flag = True
			break
	if not flag:
		# print(i)	#找到了一个质数
		lst.append(i)
		count += 1
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)




