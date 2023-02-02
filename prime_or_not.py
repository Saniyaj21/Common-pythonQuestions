def Prime(number):
    if number<=1:
        return False
    if number == 2:
        return True
    for i in range(2, (number//2)+1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number : "))
if Prime(number):
    print("Number is prime : ")
else:
    print("Number is not prime : ")

    