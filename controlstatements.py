num=int(input("Enter a number: "))

if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

    # create a program to grade student a to fail

    marks=int(input("Enter marks: "))
    if marks<=100 and marks>=80:
        print("You have an A")
    elif marks<=79 and marks>=60:
        print("You have a B")
    elif marks<=40 and marks>=59:
        print("You have a C")
    elif marks==0 and marks==39:
        print("You have failed")
    else:
        print("invalid marks entered")