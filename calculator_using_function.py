n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))

choice = int(input("Enter 1,2,3,4 respectively for sum,sub,mul,div : "))


    
def do_sum(n1,n2):
    return (n1+n2)

def do_sub(n1,n2):
    return (n1-n2)

def do_mul(n1,n2):
    return (n1*n2)

def do_div(n1,n2):
    return (n1//n2)

if choice == 1:
    result = do_sum(n1, n2)
    print(f"Addition of {n1} and {n2} is = {result}")

elif choice == 2:
    result = do_sub(n1, n2)
    print(f"Subtraction of {n1} and {n2} is = {result}")

elif choice == 3:
    result = do_mul(n1, n2)
    print(f"Multiplication of {n1} and {n2} is = {result}")

elif choice == 4:
    result = do_div(n1, n2)
    print(f"Division of {n1} and {n2} is = {result}")