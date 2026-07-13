Profit=int(input('Enter the profit:'));
Time=int(input('Enter the time:'));
rate=int(input('enter the rate:'));

amount = Profit * (pow((1 + rate / 100), Time))


compound_interest = amount - Profit

print('The compound interest is',compound_interest);


