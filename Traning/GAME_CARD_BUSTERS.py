
####### HOW TO PLAY ##########

#There are seven rounds in the game. Each round, the value of the players’
#cards for that particular round are compared to see who has the highest 
#valued card. The player with the highest value card wins the round


player_1 = 10,6,8,9,12,7

player_2 = 7,6,8,9,5,2,8,11


#name fo game

print('*********** CARD BUSTERS **************')

#MENU


########### ROUND 1 ##########

print('-----------/ ROUND NUMBER 1/ ----------')

player_1 = int(input('Player_1 - Put your Card :'))
player_2 = int(input('Player_2 - Put your Card :'))


round1 = [player_1,player_2]

for round in range (1):
    round +1
    print('-----------Result-------------') 
    print('Player_1 -',round1,'- Player_2')  
    
if player_1== player_2 :    
    print('_______The round 1 has DRAW______')
elif player_2 >= player_1:
    print('_________  Player_2 WINS_______')
    
else:
    player_1 >= player_2
    print('_________  Player_1 WINS_______')


print('*******************************************')
print('*******************************************')


########### ROUND 2 ##########

print('-----------/ ROUND NUMBER 2/ -------------')

player_1 = int(input('Player_1 - Put your Card :'))
player_2 = int(input('Player_2 - Put your Card :'))


round2 = [player_1,player_2]

for round in range (1):
    round +1
    print('-----------Result-------------') 
    print('Player_1 -',round2,'- Player_2')  
    
if player_1== player_2 :    
    print('_______The round 2 has DRAW______')
elif player_2 >= player_1:
    print('_________  Player_2 WINS_______')
    
else:
    player_1 >= player_2
    print('_________  Player_1 WINS_______')


print('*******************************************')
print('*******************************************')


########### ROUND 3 ##########

print('************* ROUND NUMBER 3 *************')

player_1 = int(input('Player_1 - Put your Card :'))
player_2 = int(input('Player_2 - Put your Card :'))


round3 = [player_1,player_2]

for round in range (1):
    round +1
    print('-----------Result-------------') 
    print('Player_1 -',round3,'- Player_2')  
    
if player_1== player_2 :    
    print('_______The round 3 has DRAW______')
elif player_2 >= player_1:
    print('_________  Player_2 WINS_______')
    
else:
    player_1 >= player_2
    print('_________  Player_1 WINS_______')


print('*******************************************')
print('*******************************************')

########### ROUND 4 ##########

print('************* ROUND NUMBER 4 *************')

player_1 = int(input('Player_1 - Put your Card :'))
player_2 = int(input('Player_2 - Put your Card :'))


round4 = [player_1,player_2]

for round in range (1):
    round +1
    print('-----------Result-------------') 
    print('Player_1 -',round4,'- Player_2')  
    
if player_1== player_2 :    
    print('_______The round 4 has DRAW______')
elif player_2 >= player_1:
    print('_________  Player_2 WINS_______')
    
else:
    player_1 >= player_2
    print('_________  Player_1 WINS_______')

print('*******************************************')
print('*******************************************')

########### ROUND 5 ##########
print('************* ROUND NUMBER 5 *************')

player_1 = int(input('Player_1 - Put your Card :'))
player_2 = int(input('Player_2 - Put your Card :'))


round5 = [player_1,player_2]

for round in range (1):
    round +1
    print('-----------Result-------------')  
    print('Player_1 -',round5,'- Player_2')  
    
if player_1== player_2 :    
    print('_______The round 5 has DRAW______')
elif player_2 >= player_1:
    print('_________  Player_2 WINS_______')
    
else:
    player_1 >= player_2
    print('_________  Player_1 WINS_______')

print('*******************************************')
print('*******************************************')
########### ROUND 6 ##########

print('************* ROUND NUMBER 6 *************')

player_1 = int(input('Player_1 - Put your Card :'))
player_2 = int(input('Player_2 - Put your Card :'))


round6 = [player_1,player_2]

for round in range (1):
    round +1
    print('-----------Result-------------') 
    print('Player_1 -',round6,'- Player_2')  
    
if player_1== player_2 :    
    print('_______The round 6 has DRAW______')
elif player_2 >= player_1:
    print('_________  Player_2 WINS_______')
    
else:
    player_1 >= player_2
    print('_________  Player_1 WINS_______')

print('*******************************************')
print('*******************************************')

########### ROUND 7 ##########

print('************* ROUND NUMBER 7 *************')

player_1 = int(input('Player_1 - Put your Card :'))
player_2 = int(input('Player_2 - Put your Card :'))


round7 = [player_1,player_2]

for round in range (1):
    round +1
    print('-----------Result-------------') 
    print('Player_1 -',round7,'- Player_2')  
    
if player_1== player_2 :    
    print('_______The round 7 has DRAW______')
elif player_2 >= player_1:
    print('_________  Player_2 WINS_______')
    
else:
    player_1 >= player_2
    print('_________  Player_1 WINS_______')

print('*******************************************')
print('*******************************************')

########### Result ###########

if round1== round2 and round3 and round4 and round5 and round6 and round7:    
    print('_________ The round has DRAW ______')

elif round2 >= round1 and round3 and round4 and round5 and round6 and round7:
    print('__________ PLayer_2 ______')
    print('__________ WINS OVERALL ____')

else:
    round1 >= round2 and round3 and round4 and round5 and round6 and round7  
    print('______Player_1_______')
    print('_____WINS OVERALL____')

    print('********GAMEOVER*********')
