

def reverse_string(string):
    return " ".join(string.split(" ")[::-1])


string = raw_input('Enter a string containing multiple words:')
print reverse_string(string)
