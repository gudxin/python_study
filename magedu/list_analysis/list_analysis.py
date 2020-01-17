#要求生成新列表元素是Lst相邻两项的和

lst = [1, 4, 9, 16, 2, 5, 10, 15]

a = [lst[i]+lst[i+1]  for i in range(len(lst)-1) ]

print(a)

#打印九九乘法表

[print("{}*{}={:<3}{}".format(i, j, i * j,'\n'if i==j else ' '),end='') for i in range(1,10) for j in range(1,i+1)]

#“0001.absjchguys”是ID格式，要求ID格式是以点号分割，左边是4位从1开始的整数，右边是10位
#随机小写英文字母。请依次生成前100个ID的列表。

import random
import string
str = 'abcdefghijklmnopqrstuvwxyz'

[print("{:04}.{}".format(i,"".join(random.sample(str,10))),end='\n') for i in range(1,101)]
# [print("{:0>4d}.{}".format(i,"".join(random.sample(string.ascii_lowercase,10))),end='\n') for i in range(1,101)]s

# print("".join(random.sample(str,10)))



a = {x:y for x in range(3) for y in range(4)}

print(a)

