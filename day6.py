marks=int(input("Enter your marks?"))  #Grade checker 
if marks<0 or marks>100:
    print("invalid marks")
elif marks>=80:
    print("Grade: A")
elif marks>=70:
    print("Grade: B")
elif marks>=60:
    print("Grade: C")
elif marks>=50:
    print("Grade: D")
else:
    print("Grade: F")

#Login check 
username=input("Enter your username?")
password=input("Enter your password?")
correct_username="admin"
correct_password="admin11122"
if username==correct_username and password == correct_password:
    print("Access is Granted.")
else:
    print("Access is denied.")

 #valid exam day
exam_day=int(input("Enter your exam day?"))
if exam_day>=1 and exam_day<=7:
     print("Valid Exam day.")
else:
     print("invalid exam day.")
