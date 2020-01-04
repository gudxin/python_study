# def print_two(*args):
	# arg1, arg2 = args
	# print(f"arg1: {arg1},arg2: {arg2}. ")
	
# def print_two_again(arg1,arg2):
	# print(f"arg1: {arg1},arg2: {arg2}. ")
	
# def print_one(arg1):
	# print(f"arg1:{arg1}.")
	
# def print_none():
	# print("I got nothin'.")
	
# print_two("Zed","Shaw")
# print_two_again("Zed","Shaw")
# print_one("Zed")
# print_none()


def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheese.")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("Or,we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do match inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and match:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 200)	