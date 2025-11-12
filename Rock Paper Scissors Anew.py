import random
player_dic = {
    }
PlayAgain="yes"
while PlayAgain==("yes"):


        pscore=bscore=rounds=0
        current_player = input("Who is the current player?")
        if current_player not in player_dic:
            CPS = 0
            CBS = 0
            player_dic[current_player] = (str(CPS) + ":" + str(CBS))
        else:
            CPS = player_dic[current_player].split(":")[0]
            BPS = player_dic[current_player].split(":")[1]

        while True:
            try:
             rounds = int(input("How many rounds would you like? "))
             if rounds <= 0:
                print("Please enter a positive number of rounds.")
                continue
             break
            except ValueError:
                print("Invalid input. Please enter a valid integer for the number of rounds.")
        
        while int(pscore) < int(rounds) and int(bscore) < int(rounds):
            Bot=random.randint(1, 3)
            Player = None
            while Player == None:
                Player=input("Rock, Paper, Scissors:")
                if Player=='rock':
                    Player=1
                    print("Player chooses rock", end=', ')
                elif Player=='paper':
                    Player=2
                    print("Player chooses paper", end=', ')
                elif Player=='scissors':
                    Player=3
                    print("Player chooses scissors", end=', ')
                else:
                    print("Invalid input.  Please choose 'rock', 'paper', or 'scissors'.")
                    Player = None
                if Bot == 1:
                    print("Bot chooses rock")
                elif Bot == 2:
                    print("Bot chooses paper")
                elif Bot == 3:
                    print("Bot chooses scissors")
            Score=int(Player)-int(Bot)  
            print()
            if Score==-1 or Score==2:
                print("Loss!")
                bscore += 1
            elif Score==0:
                print("Tie!")
            else:
                print("Win!")
                pscore += 1

                
        if int(pscore) == int(rounds) and int(bscore) == int(rounds):
            print("Tie??")
        elif int(bscore) == int(rounds):
            print("you have lost the game")
        else:
            print("you have won the game!!")
        CPS = int(CPS) + pscore
        CBS = int(CBS) + bscore
        player_dic[current_player] = (str(CPS) + ":" + str(CBS))
        print("\n")
        while True:
            PlayAgain = input("Would you like to play again? (yes/no): ").lower().strip()
            if PlayAgain in ["yes", "no"]:
                break
        else:
            print("Please enter 'yes' or 'no'.")        


