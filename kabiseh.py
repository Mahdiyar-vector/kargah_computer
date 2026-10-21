while True:
    try:
        year = int(input("Please enter a Gregorian year: "))
    except ValueError:
        print('please type a number!!!\n')
        continue

    if year == 0:
        print("Year 0 is not valid!\n")
        continue

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f'{year} is a leap year.\n')
        break
    else:
        print(f'{year} is not a leap year.\n')
        break
