sub1=int(input("Enter marks of subject 1: "));
sub2=int(input("Enter marks of subject 2: "));
sub3=int(input("Enter marks of subject 3: "));  
sub4=int(input("Enter marks of subject 4: "));
sub5=int(input("Enter marks of subject 5: "));

total=(sub1+sub2+sub3+sub4+sub5);
percent=total/5;

if(percent >=75):
    print("Distinction");
elif(percent >=60):
    print("First Class");
elif(percent >= 50):
    print("Second Class");
else:
    print("Fail");


