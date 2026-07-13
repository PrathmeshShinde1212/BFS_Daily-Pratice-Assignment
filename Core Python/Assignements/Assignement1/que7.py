days=int(input('Enter the no of days: '));

years=days // 365;
print(years);

days=days % 365;
print(days);

weeks=days // 7;
print(weeks);

days=days % 7;
print(days);

print(f'Years:{years},weeks:{weeks},days:{days}');


