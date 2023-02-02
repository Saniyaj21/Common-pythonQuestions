
def sumNatural(n):
    if n<=1:
        return n
    else:
        return n+sumNatural(n-1)

num = int(input("Enter how many numbers to sum : "))
print("Sum of first {num} natural number is : ",sumNatural(num))

