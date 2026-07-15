import random;

userID=input("Enter a user id:");
password=input("Enter a password:");

if(userID == "admin") and (password =="Prathmesh@1214"):
    captch=random.randint(1000,9999);
    print(f"Your captch={captch}");
    chuser=int(input("Enter a captcha=>"));
    if(chuser == captch):
        print("User login sucessfully");
    else:
        print("Invalid captcha");
else:
    print("Invalid user");

