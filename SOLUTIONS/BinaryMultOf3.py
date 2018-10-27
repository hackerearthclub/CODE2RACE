# Determine if binary number is a multiple of 3

num_tcases = int(input("Number of Test Cases: "))

for i in range(num_tcases):
    binary_string = input("Binary Number: ")

    # Add 0s to begining of binary to get complete bytes(4 bits)
    while len(binary_string) % 4 != 0:
        binary_string = f"0{binary_string}"
    
    num_bytes = int(len(binary_string) / 4)
    decimal = 0
    byte_decimal = 0
    place_value = 1
    for byte in range(num_bytes):
        # Calculate decimal value of a byte 
        for bit in range(4):
            binary = int(binary_string[place_value -1])
            byte_decimal += binary * 2 ** (len(binary_string) - place_value)
            place_value += 1

        # Add decimal value of byte to decimal and reset byte_decimal
        decimal += byte_decimal
        byte_decimal = 0
    
    # Print outcome
    if(decimal % 3 == 0):
        print(1)
    else:
        print(0)
