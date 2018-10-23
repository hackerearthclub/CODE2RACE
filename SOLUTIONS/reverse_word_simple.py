def reverse_word(string):
    string = string.split()[::-1]
    string = " ".join(string)
    return string

string = str(input())

print(reverse_word(string))
