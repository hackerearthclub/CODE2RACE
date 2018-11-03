"""

https://en.wikipedia.org/wiki/Fizz_buzz

Fizz buzz is a group word game for children to teach them about division. Players take turns to
count incrementally, replacing any number divisible by 3 with the word "fizz", and any
number divisible by 5 with the word "buzz".

Players generally sit in a circle. The player designated to go first says the number "1", and
each player thenceforth counts one number in turn. However, any number divisible by 3 is
replaced by the word fizz and any divisible by 5 by the word buzz. Numbers divisible by both
become fizz buzz. A player who hesitates or makes a mistake is eliminated from the game.

For example, a typical round of fizz buzz would start as follows:

1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22,
23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ...

It has been used as an interview screening device for computer programmers. Writing a program to
output the first 100 FizzBuzz numbers is a trivial problem for any would-be computer programmer,
so interviewers can easily sort out those with insufficient programming ability.
"""

def FizzBuzz(limit):
    for i in range(1, limit+1):
        if(i%3 == 0 and i%5 == 0): print("FizzBuzz")
        elif(i%3 == 0): print("Fizz")
        elif(i%5 == 0): print("Buzz")
        else: print(i)
        
FizzBuzz(100)
        