#modify size of plan
size = 10
#modify win condition
num_to_win = 4
plan = [["-" for i in range(size)] for j in range(size)]
current_symbol = "o"

def print_plan():
    for i in range(len(plan)):
        if i == 0:
            print("   ", end = "")
            for k in range(len(plan[i])):
                print(chr(65+k), end = "  ")
            print()
        for j in range(len(plan[i])):
            if j == 0:
                if i < 9:
                    print(i+1, end = "  ")
                else:
                    print(i+1, end = " ")
            if plan[i][j] == "-":
                print("-", end = "  ")
            elif plan[i][j] == "x":
                print("x", end = "  ")
            else:
                print("o", end = "  ")
        print()

def check_for_win(x,y,current_symbol):
    # check row
    count = 0
    for i in range(size):
        if plan[x][i] == current_symbol:
            count += 1
            if count == num_to_win:
                return True
        else:
            count = 0
    # check column
    count = 0
    for i in range(size):
        if plan[i][y] == current_symbol:
            count += 1
            if count == num_to_win:
                return True
        else:
            count = 0
    # check diagonal one
    count = 0
    m = x
    n = y
    while m > 0 and n > 0:
        m -= 1
        n -= 1
    while m <= size-1 and n <= size-1:
        if plan[m][n] == current_symbol:
            count += 1
            if count == num_to_win:
                return True
        m += 1
        n += 1
    # check diagonal two
    count = 0
    m = x
    n = y
    while m > 0 and n < size-1:
        m -= 1
        n += 1
    while m <= size-1 and n >= 0:
        if plan[m][n] == current_symbol:
            count += 1
            if count == num_to_win:
                return True
        m += 1
        n -= 1    
    return False
print("Enter coordinates. Sample input \"c4\" (without the quotes).")
while True:
    print("Player {}'s turn.".format(current_symbol))
    print_plan()
    inp = input()
    y = ord(inp[0].upper())-65
    x = int(inp[1:])-1
    if plan[x][y] == "-":
        plan[x][y] = current_symbol
        if check_for_win(x,y,current_symbol):
            print(x,y)
            print_plan()
            break
        if current_symbol == "o":
            current_symbol = "x"
        else:
            current_symbol = "o"
    else:
        print("Invalid position, play again.")

print("Player {} wins!!!".format(current_symbol))
input()
