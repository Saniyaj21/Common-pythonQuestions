# multiplication table

num = int(input("Enter a number : "))
print(f"Multiplication table of {num} is : ")
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")