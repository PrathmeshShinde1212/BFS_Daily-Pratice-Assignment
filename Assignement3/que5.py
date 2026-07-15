side1=int(input("Enter first side: "));
side2=int(input("Enter second side: "));
side3=int(input("Enter third side: "));

if(side1 == side2 == side3):
    print("This is a Equilateral tringle");
elif (side1 == side2 or side2 == side3 or side3 == side1):
    print("This is a isosceles tringle");
else:
    print("This is a scalene tringle");

