
cards_one = [10,6,8,9,7,12,7]

cards_two = [7,6,9,5,2,8,11]




def rounds():
    
    if cards_one== cards_two :    
        print('_The round has DRAW_')
    elif cards_two >= cards_one:
        print('_Player_2 WINS_')
    else:
        cards_one >= cards_two
        print('_ Player_1 WINS__')