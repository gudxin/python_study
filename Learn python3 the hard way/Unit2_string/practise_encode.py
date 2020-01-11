import sys
script, encoding, error = sys.argv


def main(language_file, encodings, errors):
	line = language_file.readline()

	if line:
		print_line(line, encodings,errors)
		return main(language_file, encodings, errors)

def print_line(line, encoding, errors):
	# 删除每行结尾的\n
	# next_lang = line.strip()
	raw_byte = line.encode(encoding, errors = errors)
	cooked_string = raw_byte.decode(encoding, errors = errors)
	
	print(raw_byte, "<===>", cooked_string,end = "")

languages = open("language.txt", encoding = "UTF-8")

main(languages, encoding, error)	