user1 = input('Elije piedra, papel o tijera: ')
user2 = input('Elije jugador dos, piedra - papel o tijera: ')
re = ['piedra', 'papel', 'tijera']

def result():
    if user1 in re:
        player1()
        if user2 in re:
            player2()
        else:
            print('Error')
    else:
        print('Error')
def player1 ():
    if(user1 == 'piedra' and user2 == 'papel'):
        print('Jugador 2 gana')
    elif(user1 == 'papel' and user2 == 'tijera'):
        print('Jugador 2 gana')
    elif(user1 == 'tijera' and user2 == 'piedra'):
        print('Jugador 2 gana')
def player2 ():
    if(user2 == 'piedra' and user1 == 'papel'):
        print('Jugador 1 gana')
    elif(user2 == 'papel' and user1 == 'tijera'):
        print('Jugador 1 gana')
    elif(user2 == 'tijera' and user1 == 'piedra'):
        print('Jugador 1 gana')

result()

##GrJuan