def main():
    userInput = input('Enter a string with multiple words: ')
    wordsArr = userInput.split(' ')
    reversedWord = '';
    for word in reversed(wordsArr):
    	reversedWord += word + ' '
    print(reversedWord)

if __name__ == '__main__':
    main()