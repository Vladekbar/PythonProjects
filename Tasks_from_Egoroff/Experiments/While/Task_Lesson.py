guess = input('Enter your password: ')
password = 'qwerty'
n = 2
count = 0`
while guess != password and n > 0:
    count += 1
    print(f'Wrong password! You have only {n} guesses left! Try again: ')
    guess = input('Enter your password: ')
    n -= 1
if n == 0 and guess != password:
    print('You have run out of guesses!')
    exit()
else:
    print('Congratulation! You have guessed the correct password!')
    print(f'You have guessed the password {count} times!')