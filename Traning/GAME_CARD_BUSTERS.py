print('******* Card Busters *******')


player_1 = [10, 6, 8, 9, 7,12, 7]
#element =  0   1  2  3  4  5  6
player_2 = [7, 6, 9, 5, 2, 8, 11]


for i in range(len(player_1)):  
    if (player_1[i] > player_2[i]):
            print('Player_1 Wins the round',player_1[i],'with beating',player_2[i])

    elif (player_2[i] > player_1[i]):
            print('Player 2 wins the round',player_2[i],'with beating',player_1[i])
    
    else: (len(player_1) == len(player_2))
    #print('This round has ended in a draw',)

        ########### Result ###########
                        
print('Player_1 the game, by',i - 2,'wins to',i-4)


