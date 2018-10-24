# ReadFile Program

def print_text(file):
	for line in file:
		print(line)

text_file = open("new.txt", 'r') 
print_text(text_file)
