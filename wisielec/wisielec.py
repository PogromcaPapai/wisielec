import random
import os

def wybor(zbior):
    a = 'ghh'
    while not a in slownik.keys():
       a = input('Wybierz kategorię: ')
    return random.choice(slownik[a])

def tester(slowo, litera, druk):
    czy = False
    for i in range(len(slowo)):
        if litera==slowo[i]:
            czy = True
            druk[i] = slowo[i]
    return " ".join(druk), czy

def wisi(a):
    if a==0:
        return (' +---+',' |   |',' |    ',' |    ',' |    ',' |    ',' |    ','-------')
    if a==1:
        return (' +---+',' |   |',' |   O',' |    ',' |    ',' |    ',' |    ','-------')
    if a==2:
        return (' +---+',' |   |',' |   O',' |   |',' |   |',' |    ',' |    ','-------')
    if a==3:
        return (' +---+',' |   |',' |   O',' |  /|',' |   |',' |    ',' |    ','-------')
    if a==4:
        return (' +---+',' |   |',' |   O',' |  /|\\',' |   |',' |    ',' |    ','-------')
    if a==5:
        return (' +---+',' |   |',' |   O',' |  /|\\',' |   |',' |  / ',' |    ','-------')
    if a==6:
        return (' +---+',' |   |',' |   O',' |  /|\\',' |   |',' |  / \\',' |    ','-------')

slownik = {'zwierzęta':['pies','kot','ryba']}

while True:
    kat = 'ghh'
    while not kat in slownik.keys():
       kat = input('Wybierz kategorię: ') 
    wybrane = random.choice(slownik[kat])
    os.system('cls')
    lblad = -1
    lit = '4'
    druk = ["_" for x in wybrane]
    while True:
        runda = tester(wybrane, lit, druk)
        if not runda[1]:
            lblad +=1
        print('Kategoria: ', kat, '\n\n========================\n')
        print("\n".join(wisi(lblad)))
        print('\n========================\nSłowo: \n')
        print(runda[0],'\n')
        if lblad==6:
            print('========================\nPrzegrałeś :c')
            input()
            break
        elif not '_' in runda[0]:
            print('========================\nWygrałeś c:')
            input()
            break
        else:
            lit = input('Podaj kolejną literę:\n')
        os.system('cls')
    os.system('cls')
    if input("Czy chcesz kontynuować?\n") in ['Nie','nie','n','N']:
        break
