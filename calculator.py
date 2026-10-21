import math

while True:
    try:
        op = input('Enter operator (+, -, *, /, **, sqrt): ')

        if op == "sqrt":
            num = float(input("Enter a number: "))
            if num < 0:
                print("Cannot take square root of a negative number!\n")
                continue
            result = math.sqrt(num)
            print(f"sqrt ({num}) = {result}\n")

        else:
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))

            if op == '**':
                result = num1 ** num2
            elif op == '/':
                if num2 == 0:
                    print('can not divide by zero.')
                    continue
                result = num1 / num2
            elif op == '*':
                result = num1 * num2
            elif op == '-':
                result = num1 - num2
            elif op == '+':
                result = num1 + num2
            else:
                print('unknown operator!!!')
                continue

            print(f'{num1} {op} {num2} = {result}\n')

    except ValueError:
        print('please type a number!!!\n')
        continue

    moreover = input("Again? (y/n): ").lower()
    if moreover != 'y':
        break
