import random

choices = ['rock', 'paper', 'scissors']
user_score = 0
cpu_score = 0


print('=' * 80)
print('\n                     (((Rock , Paper , Scissors game )))\n')
print('=' * 80)

while True:
    print('')
    print('1)Rock 🪨')
    print('2)Paper 📃')
    print('3)Scissors ✂️')
    print('0)Exit')

    user_input = input('\nchoose one of these options: ')

    if user_input == '0':
        print('\nfinish')
        print(f'your score: {user_score}')
        print(f'CPU score: {cpu_score}')
        break

    if user_input not in ('1', '2', '3'):
        print('Invalid input!')
        break

    user_choise = choices[int(user_input) - 1]
    cpu_choise = random.choice(choices)

    print(f'\nYou chose : {user_choise}')
    print(f'CPU chose: {cpu_choise}')

    if user_choise == cpu_choise:
        print('equivalent.')
    elif (
        (user_choise == 'rock' and cpu_choise == 'scissors') or
        (user_choise == 'scissors' and cpu_choise == 'paper') or
        (user_choise == 'paper' and cpu_choise == 'rock')
    ):
        print('you win.🎉')
        user_score += 1
    else:
        print('CPU wins')
        cpu_score += 1

    if user_score == 3 or cpu_score == 3:
        break

print(f"\nScore: You {user_score} - {cpu_score} Computer")
