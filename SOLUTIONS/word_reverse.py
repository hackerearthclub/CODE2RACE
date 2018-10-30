def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])


print(reverse_sentence("Go away"))
