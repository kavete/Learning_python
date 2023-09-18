weight = int(input("Enter weight\n"))

unit = input("L(bs) or K(g)")

if unit.upper() == 'K':
    converted = weight / 0.45
    print(f'You are {converted} Pounds')
else:
    converted = weight * 0.45
    print(f'You are {converted} Kilograms')

