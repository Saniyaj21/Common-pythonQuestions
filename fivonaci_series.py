num = int(input("Enter how many numbers you want : "))

a = 0
b = 1

for i in range(num):
    print(a)
    temp = a+b
    b = a 
    a = temp