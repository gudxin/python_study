def gold_room():
	flag = True
	while flag == True:
		choice = input(">")
		#只要有零或者1就进入
		if "0" in choice or "1" in choice:
			print("1Good jOb!")
		elif "2" in choice:
			print("2well done")
		elif "3" in choice:
			print("3nice")
		else:
			print("4bad boy")
			flag = False

gold_room()