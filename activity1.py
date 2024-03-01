age=int(input ("Enter your age:"))
status=input ("Are you student:(yes or no)").lower()
if status =="yes":
    if (age <= 12) or (age <=18 and age >=13):
        print("You are eligible for discount.")

    else:
        print("You are not eligible for discount.")

else:
    print("You are not eligible for discount.")