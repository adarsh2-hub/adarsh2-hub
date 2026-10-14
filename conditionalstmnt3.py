studmarks=int(input("Enter the student marks:"))
if studmarks>=90:
    print("Grade A..")
elif studmarks>=75:
    if studmarks<90:
        print("Grade B..")
elif studmarks>=50:
    if studmarks<75:
        print("Grade C..")
else:
    print("Fail..")