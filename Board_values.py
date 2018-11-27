import random

player1_name = input('Enter Name for player 1:')
player2_name = input('Enter Name for player 2:')




board_values={0:'Go',1:'Chennai',2:'Mumbai',3:'Delhi',4:'Kolkata',5:'Agra',6:'Bhubaneshwar',7:'Lucknow'}


die_no1=0            # to determine where the player is
die_no2=0            # to determine where the player is

player_var=1



def player1():

    global player_var           #this is to switch between the two players
    player_var += 1


    print(player1_name, ' it\'s your turn \nPress r to roll the dice')

    #dice rolling

    player1_inp= input()
    if player1_inp=='r':
        k = random.randint(1,6)
        print('You rolled a',k)
    else:
        k=76

    if k==76:
        player_var = 0
        return

    global die_no1
    die_no1 = k+ die_no1

    if die_no1>7:
        die_no1 = die_no1-8
        if die_no1>0:
            print('You have passed go')



    #chec for dice no.
    #print('dieno is', die_no1)

    for val,ky in board_values.items():
        if  die_no1==val:
            print('You are at ',ky)
            break

def player2():

    global player_var           #this is to switch between the two players
    player_var -= 1

    print((player2_name, ' it\'s your turn :'))

    #dice rolling

    player_2_inp= input()
    if player_2_inp=='r':
        k = random.randint(1,6)
        print('You rolled a',k)
    else:
        k=76

    if k==76:
        player_var = 0
        return

    global die_no2
    die_no2 = k+ die_no2

    if die_no2>7:
        die_no2 = die_no2-8
        if die_no2>0:
            print('You have passed go')



    #chec for dice no.
    #print('dieno is', die_no1)

    for val,ky in board_values.items():
        if  die_no2==val:
            print('You are at ',ky)
            break





while player_var!=0:
    if player_var==1:
        player1()
    elif player_var==2:
        player2()
    else:
        print('shit')


