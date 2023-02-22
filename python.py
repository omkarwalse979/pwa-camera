import random
prev_score = 0
player_turn = 1

while True:
    print("\nPlayer, player", player_turn ,"press ENTER to generate alphabet")
    input()
    
    curr_score = random.randint(65,90)
    alpha - str(curr_score)
    print("You Generate", alpha)
    if curr_core prev_score + 1: 
        print("Player", player_num, "wins..!!")
        break
    else:
        prev_score = curr_score

    if player_turn == 1:
        player_turn = 2
    elif player_turn == 2:
        player_turn = 1