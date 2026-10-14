largest_number=0
first_number=int(input("Enter the first number:"))
second_number=int(input("Enter the second number:"))
third_number=int(input("Enter the third number:"))
if first_number>second_number and first_number>third_number:
    print("largest number is=",first_number)
elif second_number>third_number and second_number>first_number:
    print("largest number is",second_number)
else:
    print("largest number is=",third_number)