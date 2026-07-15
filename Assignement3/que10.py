num = int(input("Enter a 3-digit number: "))

if 100 <= num <= 999:
    temp = num
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10

    if num == reverse:
        print("The number is a Palindrome.")
    else:
        print("The number is Not a Palindrome.")
else:
    print("Please enter a valid 3-digit number.")