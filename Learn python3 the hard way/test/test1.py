def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	"""Sort the words"""
	#sorted是任何可迭代对象都可按照ASCII大小排序，并产生新的
	#可迭代对象
	#list.sort()只针对列表，并在原列表上进行排序修改
	return sorted(words)
	
def print_first_word(words):
	"""Prints the first word after popping it off"""
	word = words.pop(0)
	print(word)
	
def print_last_word(words):
	word = words.pop(-1)
	print(word)
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words"""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)