word = "This is just a test."


def reverse_word(input_str: str) -> str:
    if not input_str:
        return input_str
    else:
        return reverse_word(' '.join(input_str.split()[1:])) + \
            input_str.split()[0] + ' '


print(reverse_word(word))
