ten_things = "Apples,Orange,Crows,Light,Sugar"

print("Wait there are not 10 things.Let's fix that.")
#字符串通过","划分为列表
stuff = ten_things.split(',')

print(type(stuff))
print(stuff)
print(stuff[1])

more_stuff = ["Day", "Night","Song","FriSbee","Corn","Banana","Girl","Boy"]

# print(more_stuff.pop())
# print(more_stuff)

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:",next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("Here we go:",stuff)
print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
#将stuff尾部
print(stuff.pop())
print(stuff)
#string"Apples Orange Crows Light Sugar Boy Girl Banana Corn"
print(' '.join(stuff))
#String"Light#Sugar"
print('#'.join(stuff[3:5]))

#a = ['7009.0', '童美琪', '1.0', '103.0', '118.0', '107.0',' 94.0', '95.0',' 517.0', '2.0', '57.0',' 81.0',' 655.0',' 4.0', '1.0']
a = [7009.0, '童美琪', 1.0, 103.0, 118.0, 107.0, 94.0, 95.0, 517.0, 2.0, 57.0, 81.0, 655.0, 4.0, 1.0]
b = [str(i) for i in a]
	
print(type(b))
print(b)



