year = int(input("Enter a year to check : "))

if(year %400 == 0 and year%100 ==0):
    print("year is leap year")
elif year%4==0 and year%100!=0:
    print("year is leap year")
else:
    print("year is not leapyear")