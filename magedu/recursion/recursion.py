#求N的阶乘
#(1) 一般阶乘
# def Factorial(n):
	# return 1 if n<=2 else n * Factorial(n-1)
	
# Factorial(5)

#(2)
def Factorial(n):
	if n == 2:
		return 2
	return n * Factorial(n-1)
	
print(Factorial(5))

                                      

#将一个数逆序放入列表中，例如1234=>[4,3,2,1]
#(1)
# def func(n):
	# length = len(n)
	# number = int(n)
	# cal_number = (10**(length-1))
	# while length:
		# innum = number // cal_number
		# lst.append(innum)
		# number = number - innum * cal_number
		# length -= 1
	# reversed(lst)
	# print(lst)
# lst = []	
# func(input("input a number >>"))

#(2)：
# str = input("give a number")
# lst = list(reversed(str))
# print(lst)

#(3)： 递归方式
# def func(num, target=[]):
	# if num:
		# target.append(num[len(num)-1])
		# func(num[:len(num)-1])
	# return target
	
# print(func(str(1234)))


#三。猴子第一天摘下若干个桃子，当即吃了一半，又多吃了一个。第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到了第十天早上想吃的时候，只剩下了一个桃子了。求第一天一共摘了多少个桃子。

def Peach(day=1):
	if day == 10:
		return 1
	return 2*(Peach(day+1)+1)
	
print(Peach())
	






		
	

	