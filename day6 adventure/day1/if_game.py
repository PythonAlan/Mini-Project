__author__ = 'uesr'

mynumbers = 16
guess = -1 #先定义值,不然会报错
retry_count = 0
while retry_count <3:  #while True循环,条件为true则执行
    guess = int(input('Pls guess my number :'))

    if guess < mynumbers:
        print('Pls try to guess again.It may be bigger than...')
    elif guess > mynumbers :
        print ('Pls try to guess again.It may be less than...')
    else:
        print('Bingo')
        break  #猜对直接退出程序
    retry_count += 1
else:
    print('Try too many times')

