import random

number = random.randint(1, 5)

while True:
    try:
        guess = int(input("guess number: "))
    except ValueError:
        print('please type a number!!!\n')
        continue

    if guess == number:
        print('Very gooood.')
        break
    else:
        print('try again!\n')
sdfsdfsdfsdf
sdfsdfsdfsdf
sdfsdfsdfsdf
