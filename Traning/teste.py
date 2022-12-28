########## ROUND 1 ##########

print('ROUND NUMBER 1:')

player_1 = int(input('Player_1 - Put your Card :'))
player_2 = int(input('Player_2 - Put your Card :'))


round1 = [player_1,player_2]

for round in range (1):
    round +1
    print('--------Result----------') 
    print('Player_1 -',round1,'- Player_2')  

if player_1== player_2 :    
    print('______The round 1 has DRAW______')
elif player_2 >= player_1:
    print('______ PLayer_2 WINS______')
else:
    player_1 >= player_2
    print('______Player_1 WINS_______')

   

print('********************************************************')
print('********************************************************')


########### ROUND 2 ##########

print('ROUND NUMBER 2:')

player_1 = int(input('Player_1 - Put your Card :'))
player_2 = int(input('Player_2 - Put your Card :'))


round2 = [player_1,player_2]

for round in range (1):
    round +1
    print('--------Result----------') 
    print('Player_1 -',round2,'- Player_2')  
    
if player_1== player_2 :    
    print('______The round 2 has DRAW______')
elif player_2 >= player_1:
    print('______ PLayer_2 WINS______')
else:
    player_1 >= player_2
    print('______Player_1 WINS_______')

print('********************************************************')
print('********************************************************')

total = round1, round2


print(total)



