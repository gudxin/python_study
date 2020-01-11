sum = 0 
for i in range(1,10):
    for j in range(1,i+1):
        sum = i*j
        print(j,'*',i,'=',sum,sep = '',end='\t')
        j += 1
    else:
        print()
    i += 1;
	
	
for i in range(-3,4,1):
    if i < 0:
        i = -i
    else:
        i = i
    print(' '*i+'*'*(7-2*i))
	

def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
for i in range(1,101):
    if Fibonacci(i)>100:
        break
    print(Fibonacci(i))
	
	
def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
sum = Fibonacci(100)
print(sum)




a = 1
b = 1
print(a)
print(b)
for count in range(99):
    a,b=b,a+b
    if b>100:
        break
    print(b)
	
	
	
	
sum = 0
for i in range(2,100000):
    for j in range(2,int(i**0.5)+1):
        if  i % j == 0:
            break
    else:
        sum += 1

print(sum)




for i in range(1,10):
    print(i*'\t',end='')
    for j in range(i,10):
        print("{}*{}={}\t".format(i,j,i*j),end='')
    print()
	
	
	
	
for i in range(1,10):     
    s=(i-1)*'\t' 
    for j in range(i,10):         
        s += str(j) + '*' + str(i) + '=' + str(i*j) + '\t'   
    print(s)
	
	
	

for i in range(1,10):     
    s=''
    for j in range(i,10):         
        s += "{}*{}={:<{}}".format(i,j,i*j,2 if j<4 else 3)  
    print('{:>85}'.format(s))
	
	
	
for i in range(-3,4,1):
    print(' '*i+'*'*(7-2*i)) if i>0 else print(' '*(-i)+'*'*(7-2*(-i)))
	
	
	
	
	import datetime
start = datetime.datetime.now()
sum = 0
for i in range(2,100000):
    for j in range(2,i):
        if  i % j == 0:
            break
    else:
        sum += 1
start = datetime.datetime.now() - start
print(start.total_seconds())

print(sum)






import datetime
start = datetime.datetime.now()
sum = 0
for i in range(2,100000):
    for j in range(2,int(i**0.5)+1):
        if  i % j == 0:
            break
    else:
       sum += 1
start = datetime.datetime.now() - start

print(start.total_seconds())
print(sum)




import datetime
start = datetime.datetime.now()
sum = 1
for i in range(3,100001,2):
    for j in range(2,int(i**0.5)+1):
        if  i % j == 0:
            break
    else:
       sum += 1
start = datetime.datetime.now() - start

print(start.total_seconds())
print(sum)



#还有一种算法
import datetime
start = datetime.datetime.now()
sum = 1
for i in range(3,100001,2):
    for j in range(2,int(i**0.5)+1):
        if  i % j == 0:
            break
    else:
       sum += 1
start = (datetime.datetime.now() - start).total_seconds()

print(start)
print(sum)