#[615]

def main():
    u_Inp = input('Please enter a string: ')
    words = u_Inp.split(' ')
    revwrd = '';
    for w in reversed(words):
    	revwrd += w + ' '
    print(revwrd)

if __name__ == '__main__':
    main()