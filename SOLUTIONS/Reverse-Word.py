def reverse_word():
    s = input("Enter a sentence containing multiple words: ").strip()
    s = s.split()[::-1]
    print(s)
    s = " ".join(s)
    return s

print(reverse_word())
