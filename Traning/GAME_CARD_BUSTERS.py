print('******* Card Busters *******')


player_1 = [10, 6, 8, 9, 7,12, 7]
#element =  0   1  2  3  4  5  6
player_2 = [7, 6, 9, 5, 2, 8, 11]


p1_wins = [0]
p2_wins = [0]

for i in range(len(player_1)):  
    if (player_1[i] > player_2[i]):
        print('Player_1 Wins the round',player_1[i],'with beating',player_2[i])

    elif (player_1[i]) == (player_2[i]):
        print('This round has ended in a draw')
        
        (player_2[i] > player_1[i])
        print('Player 2 wins the round',player_2[i],'with beating',player_1[i])
    
    
 
################## restult #####################

for x in p1_wins:
        if (p1_wins > p2_wins):
                print('Player 1 wins The game,by ',p1_wins,'wins to ',p2_wins)
        
        elif (p1_wins )== (p2_wins):
                #print('the game has ended un a draw')

                (p2_wins < p1_wins)
                print('Player 2 wins the game,by',p1_wins,'wins to',p2_wins)

