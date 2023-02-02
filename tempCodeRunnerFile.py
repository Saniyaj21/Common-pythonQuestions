

def Prime(number):
    if number<=1:
        return False
    if number == 2:
        return True
    for i in range(2, (number//2)+1):
        if number % i == 0:
            return False
    return True

if Prime(10):
    print("Number is prime : ")
else:
    print("Number is not prime : ")

    