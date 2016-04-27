__author__ = 'uesr'

mynumbers = 16


for i in range(3):
    guess = int(input('Pls guess my number :'))

    if guess < mynumbers:
        print('Pls try to guess again.It may be bigger than...')
    elif guess > mynumbers :
        print ('Pls try to guess again.It may be less than...')
    else:
        print('Bingo')
        break  #猜对直接退出程序

else:
    print('Try too many times')