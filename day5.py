marks=int(input("Enter your marks?"))  # Grade calculator
if marks>=80:
    print("Grade: A")
elif marks>=70:
    print("Grade: B")
elif marks>=60:
    print("Grade: C")
elif marks>=50:
    print("Grade: D")
else:
    print("Grade: F")

# age group 

age=int(input("Enter your age?"))
if age<13:
    print("You are a child.")
elif age<20:
    print("You are a teenager.")
elif age<65:
    print("You are adult.")
else:
    print("You are a senior.")