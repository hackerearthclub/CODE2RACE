#The solution to the mistery is that each output is the number of perfect 
#divisors of the correspondent input.

message = "Please choose a number:"

a = input(message)
a = int(a)

# setting the limit to the input number
if a > 10**8:
    print("Number must be less than 10^8")

#finding the numbers that are perfect divisors of the input    
if a <= 10**8:
    divisors = []
    for i in range(1,a+1):
        if a%i == 0:
            divisors.append(i)
#printing the number of divisors
    print(len(divisors))
        
    