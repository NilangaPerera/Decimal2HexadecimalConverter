# Decimal to Hexadecimal Converter by 0x7gen
print("""
\033[1;31m  0x7gen  
 \033[1;32m  0000      x        7777777   ggggggg    eeeeeee    n     n
\033[1;33m  0    0    x x          7      g           e          nn    n
\033[1;34m  0    0    x x          7      g  gg       eeee       n n   n
\033[1;35m  0    0    x x          7      g   g       e          n  n  n
\033[1;36m   0000    x   x      77777     ggggggg    eeeeeee    n   nn

 	  === Decimal to Hexadecimal Converter ===
\033[0m""")

# Prompt the user to enter a decimal address
decimal_address = input("Enter the decimal address to convert to hexadecimal: ")

try:
    # Convert the input to an integer
    decimal_address = int(decimal_address)
    
    # Convert the decimal address to hexadecimal
    hexadecimal_address = hex(decimal_address)
    
    # Print the result
    print(f"The hexadecimal representation is: {hexadecimal_address}")
except ValueError:
    print("Invalid input! Please enter a valid decimal number.")
