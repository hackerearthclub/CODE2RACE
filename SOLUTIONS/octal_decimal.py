def octal_to_decimal(octal):
    octal_str = list(reversed(str(octal))) 
    decimal = 0
    for i in range(0, len(octal_str)):
        decimal += int(octal_str[i]) * 8**i
    return  decimal
 
def decimal_to_octal(decimal):
    decimal = int(decimal)
    finished = False
    rests = ""
    dividend = decimal
    while(finished == False):
        float_result = dividend / 8
        int_result = int(float_result)
        rest = dividend % 8       
        dividend = int_result
        if(float_result < 1):
            finished = True
        rests += str(rest)
    octal = rests[::-1]
    return octal
    
def simple_test():
    print("#--Converter made by Matteo Veraldi--#")
    octal = input("[oct2dec] Insert your octal number: ")
    print("[+] decimal result: " + str(octal_to_decimal(octal)))
    decimal = input("[dec2oct] Insert your decimal number: ")
    print("[+] octal result: " + str(decimal_to_octal(decimal)))