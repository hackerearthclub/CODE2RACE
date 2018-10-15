get = lambda mas, key: [ind for ind, value in enumerate(result) if value == key]
if __name__ == '__main__':
    count = 2  # configurable number of players
    names = []
    # rock - 0
    # paper - 1
    # scissors - 2
    for i in range(count):
        names.append(input("Enter name of {} player: ".format(i + 1)))
    print('Rock - 0, Paper - 1,Scissors -2')
    result = []
    while True:
        print('========================')
        for i in range(count):
            result.append(int(input('Enter result of {} player: '.format(i + 1))))
        rocks = get(result, 0)
        papers = get(result, 1)
        scissors = get(result, 2)
        if len(rocks) > 0 and len(papers) > 0 and len(scissors) > 0 \
                or len(rocks) == count or len(scissors) == count or len(papers) == count:
            print('Draw')
        else:

            if len(rocks) > 0 and len(scissors) > 0:
                print('Winners are players: ', [names[i] for i in rocks])
            if len(rocks) > 0 and len(papers) > 0:
                print('Winners are players: ', [names[i] for i in papers])
            if len(papers) > 0 and len(scissors) > 0:
                print('Winners are players: ', [names[i] for i in scissors])
        play_again = int(input('Play again? (1 yes, 0 no):'))
        if not play_again:
            break
