if __name__ == '__main__':

    from atm import *

    while True:
        try:
            answer = input("Enter a file with account info: ")
            inFile = open(answer)
            lines = inFile.readlines()
            inFile.close()
            break
        except:
            print("The program can not locate {}, pleaser re-enter the filepath.".format(answer))

    
    atm = ATM(lines)

    while True:
        try:
            pin = input("Please enter your secret PIN: ")
            atm.verifyPin(pin)
            break
        except InvalidPinError:
            print("You have entered a PIN that is not in the system, please try another number.")
            continue


    printMenu()
    selection = eval(input("Please choose a selection. "))
    while selection != 4:

        if selection == 1:
            print("Your current balance is ${}\n".format(atm.getBalance(pin)))
            printMenu()
            selection = eval(input("Please choose a selection. "))

        elif selection == 2:
            while True:
                try:
                    funds = input("Please enter an amount of funds to withdraw: ")
                    atm.withdraw(pin, funds)
                    printMenu()
                    selection = eval(input("Please choose a selection. "))
                    break
                
                except InvalidDataError:
                    print("Please enter a numerical value for a withdraw.")
                    continue
                
                except InsufficientFundsError:
                    print("You attemted to overdraw funds! Please enter a different amount.")
                    continue

        elif selection == 3:
            while True:
                try:
                    funds = input("Please enter an amount of funds to deposit: ")
                    atm.deposit(pin, funds)
                    printMenu()
                    selection = eval(input("Please choose a selection. "))
                    break
                
                except InvalidDataError:
                    print("Please enter a numerical value for a deposit.")
                    continue

    print("Thank you for using the ATM, have a nice day!")
    updatedData = atm.outPutData()
    outFile = open('accountsUpdated.txt', 'w')
    for line in updatedData:
        outFile.write(line + '\n')
    outFile.close()
