import os


class Client:
    def __init__(self, id, name, lastname, accnumber, accbalance):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.accnumber = accnumber
        self.accbalance = accbalance


client1 = Client("1", "Jan", "Nowak", "001", 1457.23)
client2 = Client("2", "Agnieszka", "Kowalska", "002", 3600.18)
client3 = Client("3", "Robert", "Lewandowski", "003", 2745.03)
client4 = Client("4", "Zofia", "Płucińska", "004", 	7344.00)
client5 = Client("5", "Grzegorz", "Braun", "005", 	455.38)

clientsList = [client1, client2, client3, client4, client5]


def moneyAmountToTransfer(n):
    moneyAmount = input('PODAJ KWOTĘ PRZELEWU: ')


def checkNumberToTransfer(n):
    n = int(n)
    transferAccountNumber = input(
        'WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAĆ PRZELEW: ')
    for x in clientsList:
        if x.accnumber == transferAccountNumber:
            idAccountNumber = int(x.id)
            break
        else:
            idAccountNumber = None

    if idAccountNumber == None:
        print('NIEPRAWIDŁOWY NUMER KONTA')
    elif idAccountNumber == n:
        print('NIE MOŻESZ ZROBIĆ PRZELEWU NA WŁASNE KONTO.')
    else:
        moneyAmountToTransfer(idAccountNumber)
        # print(clientsList[idAccountNumber-1].accbalance)


def showClientsList():
    print('ID | IMIĘ I NAZWISKO | NR KONTA | SALDO')
    for x in clientsList:
        print(x.id, "|", x.name, "|", x.lastname,
              "|", x.accnumber, "|", x.accbalance, "zł")
    showMenu()


def loginSuccessful(n):
    print('ZALOGOWANY KLIENT')
    print('ID:', clientsList[n-1].id)
    print('IMIĘ I NAZWISKO:', clientsList[n-1].name, clientsList[n-1].lastname)
    print('NR KONTA:', clientsList[n-1].accnumber)
    print('SALDO:', clientsList[n-1].accbalance)
    checkNumberToTransfer(clientsList[n-1].id)


def login():
    clientIdLogin = input('ZALOGUJ SIĘ WYBIERAJĄC ID KLIENTA: ')
    os.system('cls')
    if clientIdLogin.isdigit():
        clientIdLogin = int(clientIdLogin)
        if (clientIdLogin < 1 or clientIdLogin > len(clientsList)):
            print('Logowanie nieudane!')
            input()
        else:
            loginSuccessful(clientIdLogin)
    else:
        print('Logowanie nieudane!')
        input()


def showMenu():
    print('WYBIERZ OPCJĘ:')
    print('1 => LISTA WSZYSTKICH KLIENTÓW BANKU')
    print('2 => LOGOWANIE')
    print('3 => ZAKOŃCZ PROGRAM')
    print('WYBIERZ 1, 2 LUB 3:')
    userChoice = input()
    userChoice = str(userChoice)
    os.system('cls')
    if (userChoice == '1'):
        showClientsList()
    elif (userChoice == '2'):
        login()
    else:
        exit()


showMenu()
