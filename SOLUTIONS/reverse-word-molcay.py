def reverse_word():
  sentence = input("Enter a sentence to reverse words order: ")
  words = sentence.split(" ")
  return " ".join(words[::-1])

print(reverse_word())
