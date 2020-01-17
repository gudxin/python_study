a = {"name":"Gu Dongxin","age":"24","sex":"male"}
print(type(a))
print(a['name'])
for i,j in a.items():
	print(i,j)
for i in a.keys():
	print(i)
for i in a.values():
	print(i)
	
from collections import OrderedDict

od = OrderedDict()
od[100] = 100
print(od)