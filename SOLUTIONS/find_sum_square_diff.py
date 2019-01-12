# Sum square difference

def sum_square_dif(number):
    out = ((number*(number+1)*(2*number+1))/6) - ((number*(number+1)/2)**2)
    return abs( int(out) )

t = int(input())
for i in range(t):
    number = int(input())
    print(sum_square_dif(number))
