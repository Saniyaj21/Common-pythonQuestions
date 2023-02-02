num = int(input("Enter a decimal number : "))

# [2:] this string slicing is used to remove first to alphabet for every number system name
# just remove one [2:] and watch the change in output 


in_binary = bin(num)[2:]
print("Binary : ",in_binary)  


in_octal = oct(num)[2:]
print("Octal : ",in_octal)  


in_hexadecimal = hex(num)[2:]
print("Hexadecimal : ",in_hexadecimal)  
