#Program to check leap year


year = 2024
if (year%4 == 0):
   (year % 100 != 0)
   (year % 400 == 0)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("not leap year")


