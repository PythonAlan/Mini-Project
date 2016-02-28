class ATM():

    def __init__(self, accountInfo):
        '''passed in a list of lines from a file, records user data in a dictionary.'''
        self.userData = {}
        for line in accountInfo:
            data = line.strip('\n').split()
            self.userData[data[0]] = list(data[1:])
        


    def verifyPin(self, pin):
        '''verify if a user/pin combination is valid.  Raises InvalidPinError if the pin isn't stored in the ATM'''
        if pin in self.userData:
            data = self.userData[pin]
            actualPinOwner = data[0] + " " + data[1]
            print("Hello {}, welcome back!\n".format(actualPinOwner))

        else:
            raise InvalidPinError("The pin [{}] is not contained in this ATM.".format(pin))
        

    def getBalance(self, pin):
        if pin in self.userData:
            data = self.userData[pin]
            return eval(data[2])
        
        

    def withdraw(self, pin, amount):

        try:
            amount = eval(amount)
        except:
            raise InvalidDataError("Withdraw can only be performed with numerical inputs.")
        
        if pin in self.userData:
            data = self.userData[pin]
            newAmount = eval(data[2]) - amount
            if newAmount < 0:
                raise InsufficientFundsError("Withdraw attempted with insufficient funds.")
            else:
                data[2] = str(newAmount)
                print("Successfully withdrew ${}!".format(amount))
                

    def deposit(self, pin, amount):

        try:
            amount = eval(amount)
        except:
            raise InvalidDataError("Deposit can only be performed with numerical inputs.")
                                   
        if pin in self.userData:
            data = self.userData[pin]
            newAmount = eval(data[2]) + amount
            data[2] = str(newAmount)
            print("Successfully deposited ${}!".format(amount))

    def outPutData(self):
        lineList = []

        for pin in self.userData:
            data = [pin]
            data.extend(self.userData[pin])
            constructed = " ".join(data)
            lineList.append(constructed)

        return lineList
'''可以再扩展一个转账功能'''

class InvalidDataError(Exception):

    def __init__(self, message):
        super().__init__(message)    


class InvalidPinError(Exception):

    def __init__(self, message):
        super().__init__(message)

class InsufficientFundsError(Exception):

    def __init__(self, message):
        super().__init__(message)


def printMenu():

    print("\t\tWelcome to the ATM\n")
    print("Please select from one of the following choices to proceed.")
    print("1.\tGet Balance")
    print("2.\tWithdraw Funds")
    print("3.\tDeposit Funds")
    print("4.\tQuit")
