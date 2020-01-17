# num = input("please input a number you want >>>: ")
# d = {}
# for c in num:
    # if c not in d.keys():
        # d[c] = 0
    # d[c] += 1
# print(d)


# 二：
# import random
# lst = []
# for i in range(100):
	# lst.append(random.randint(-1000, 1000))

# directory = {}

# for i in lst:
	# if i not in directory:
		# directory[i] = 1
	# else:
		# directory[i] = directory[i] + 1
	
# print(sorted(directory))
# print(sorted(directory.values()))
# print(sorted(directory.items()))	k,v都可以打印

#三
import random
sample = "abcdefghijklmnopqrstuvwxyz"

numdic = {}
for i in range(100):
	k = random.choice(sample) + random.choice(sample)
	if k not in numdic.keys():
		numdic[k] = 0
	numdic[k] = 1
d1 = sorted(numdic.items(),reverse = True)
print(d1)


from datetime import datetime

d = datetime.now()
print(d)



