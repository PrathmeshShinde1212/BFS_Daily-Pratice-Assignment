unit=int(input("Enter a number of units:"));

if(unit >= 50):
    print(f'The {unit} Price is {unit * 0.50} ');
elif(unit>=100):
    print(f'The {unit} Price is {unit * 0.75}');
elif(unit>=200):
    print(f'The {unit} Price is {unit * 1.20}');
elif(unit>=250):
    print(f'The {unit} Price is {unit * 1.50}');
else:
    print("Please eneter correct unit ...!!");

