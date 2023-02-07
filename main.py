import os

redFont = '\x1b[38;2;255;0;0m'
greenFont = '\x1b[38;2;124;252;0m'


class Client:
    def __init__(self, id, name, lastname, accnumber, accbalance):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.accnumber = accnumber
        self.accbalance = accbalance


client1 = Client("1", "Jan", "Nowak", "001", 1457.24)
client2 = Client("2", "Agnieszka", "Kowalska", "002", 3600.18)
client3 = Client("3", "Robert", "Lewandowski", "003", 2745.03)
client4 = Client("4", "Zofia", "Płucińska", "004", 	7344.00)
client5 = Client("5", "Grzegorz", "Braun", "005", 	455.38)

clientsList = [client1, client2, client3, client4, client5]


def moneyAmountToTransfer(transferIdAcc, userIdAcc):
    moneyAmount = input('\n PODAJ KWOTĘ PRZELEWU: ')
    os.system('cls')
    x = clientsList[userIdAcc-1]
    y = clientsList[transferIdAcc-1]

    moneyAmountType = True

    try:
        float(moneyAmount)
    except ValueError:
        moneyAmountType = False

    if moneyAmountType:
        moneyAmount = float(moneyAmount)
        if (x.accbalance < moneyAmount):
            print(
                redFont + '\n NIEWYSTARCZAJĄCE ŚRODKI NA RACHUNKU' + '\x1b[0m')
        else:
            x.accbalance = x.accbalance - moneyAmount
            y.accbalance = y.accbalance + moneyAmount
            x.accbalance = round(x.accbalance, 2)
            y.accbalance = round(y.accbalance, 2)
            print(greenFont + '\n PRZELEW ZOSTAŁ WYKONANY' + '\x1b[0m')
            showClientsList()
        input()
    else:
        print(redFont + '\n NIEPRAWIDŁOWA KWOTA' + '\x1b[0m')
        input()


def checkNumberToTransfer(loggedIdAccountNumber):
    loggedIdAccountNumber = int(loggedIdAccountNumber)
    transferAccountNumber = input(
        '\n WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAĆ PRZELEW: ')
    os.system('cls')
    for x in clientsList:
        if x.accnumber == transferAccountNumber:
            idAccountNumber = int(x.id)
            break
        else:
            idAccountNumber = None
    if idAccountNumber == None:
        print(redFont + '\n NIEPRAWIDŁOWY NUMER KONTA' + '\x1b[0m')
        input()
    elif idAccountNumber == loggedIdAccountNumber:
        print(
            redFont + '\n NIE MOŻESZ ZROBIĆ PRZELEWU NA WŁASNE KONTO.' + '\x1b[0m')
        input()
    else:
        moneyAmountToTransfer(idAccountNumber, loggedIdAccountNumber)


def showClientsList():
    print('\n ID | IMIĘ I NAZWISKO | NR KONTA | SALDO\n')
    for x in clientsList:
        print(' ', x.id, "|", x.name, x.lastname,
              "|", x.accnumber, "|", x.accbalance, "zł\n")


def loginSuccessful(n):
    print('\n ZALOGOWANY KLIENT')
    print('\n ID:', clientsList[n-1].id)
    print('\n IMIĘ I NAZWISKO:',
          clientsList[n-1].name, clientsList[n-1].lastname)
    print('\n NR KONTA:', clientsList[n-1].accnumber)
    print('\n SALDO:', clientsList[n-1].accbalance, 'zł')
    checkNumberToTransfer(clientsList[n-1].id)


def login():
    clientIdLogin = input('\n ZALOGUJ SIĘ WYBIERAJĄC ID KLIENTA: ')
    os.system('cls')
    if clientIdLogin.isdigit():
        clientIdLogin = int(clientIdLogin)
        if (clientIdLogin > 0 and clientIdLogin <= len(clientsList)):
            loginSuccessful(clientIdLogin)
        else:
            print(redFont + '\n Logowanie nieudane!' + '\x1b[0m')
            input()
    else:
        print(redFont + '\n Logowanie nieudane!' + '\x1b[0m')
        input()


def showMenu():
    print('\n WYBIERZ OPCJĘ:\n')
    print(' 1 => LISTA WSZYSTKICH KLIENTÓW BANKU\n')
    print(' 2 => LOGOWANIE\n')
    print(' 3 => ZAKOŃCZ PROGRAM\n')
    userChoice = input(' WYBIERZ 1, 2 LUB 3: ')
    userChoice = str(userChoice)
    os.system('cls')
    if (userChoice == '1'):
        showClientsList()
        showMenu()
    elif (userChoice == '2'):
        login()
    else:
        exit()


showMenu()
