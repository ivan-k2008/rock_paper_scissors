
from random import choice
from time import sleep

class Combat:
    def __init__(Self):
        while True:
            try:
                RoundsConfirmation = "None" # initializes RoundsConfirmation, which is used if someone enters a high number of rounds
                
                Self.Rounds = int(input("How many rounds would you like to play?: ").strip()) # asks for number of rounds
                if Self.Rounds <= 0: # checks if its positive
                    print("Please enter a positive number of rounds.")
                    continue # if its not positive it just repeats
                elif Self.Rounds >= 30: # if Self.Rounds is a high number...
                    while True:
                        RoundsConfirmation = input("This is a high number of rounds. " + \
                                                   "Are you sure you want to continue? (Yes/No): ").capitalize().strip()
                        # ^ ...the lines above double check with the user if they want to continue
                        if RoundsConfirmation == "Yes": # if they say yes
                            break # ends the loop
                        elif RoundsConfirmation == "No": # if they say no
                            break # ends the loop
                        else: # if they enter something that isn't yes or no...
                            print("Please enter 'Yes' or 'No'.") # displays a message and repeats the confirmation input
                            
                if RoundsConfirmation != "No": # if the user didn't enter no after entering a number of rounds above or equal to 30
                    print("\n- - - - - - - - - - - - - -\n") # cool border
                    break # ends the loop
                # ^ the if statement above is for when a if puts a number of rounds above or equal to 30 and inputs 'No'
                # into the RoundsConfirmation input, it asks them how many rounds they'd like to play again
                
            except ValueError: # incase the user inputs something other than a number
                print("Invalid input. Please enter a valid integer for the number of rounds.")
        Self.PlayerChoice = "None" # initialized these incase someone using the __str__ outside of the game() method
        Self.BotChoice = "None" # also made them store strings to avoid errors with same scenario mentioned above ^
        Self.Weapons = {"Rock":1, "Paper":2, "Scissors":3} # initializes weapons
        
    def __str__(Self):
        return "\nPlayer chooses: " + Self.PlayerChoice + "\n\nBot chooses: " + Self.BotChoice # returns a string displaying both choices
        
    def game(Self): 
        PlayerScore = 0 # initializes both score variables
        BotScore = 0
        while (PlayerScore <= Self.Rounds / 2 and BotScore <= Self.Rounds / 2) and PlayerScore + BotScore != Self.Rounds:
        # ^ while both scores are not above half of the amount of rounds / while nobody's won and while its not a tie
            while True:
                Self.PlayerChoice = input("Rock, Paper, or Scissors?: ").capitalize().strip() # asks player for their choice
                if Self.PlayerChoice in Self.Weapons: # if Self.PlayerChoice is a valid weapon
                    break # end the loop
                print("Invalid input. Please choose 'Rock', 'Paper', or 'Scissors'.") # prints if user input isn't a weapon
                
            Self.BotChoice = choice(["Rock", "Paper", "Scissors"]) # bot randomly picks between the three
            
            print(Self) # displays choices
            print()

            RoundScore = Self.Weapons[Self.PlayerChoice] - Self.Weapons[Self.BotChoice] # calculates the result of the round...
            if RoundScore == -1 or RoundScore == 2:
                print("Loss!") # ...then displays it
                BotScore += 1
            elif RoundScore == 0:
                print("Tie!")
            else:
                print("Win!")
                PlayerScore += 1

            sleep(1) # waits one second before starting the next round so it doesnt go too fast
            print("\n- - - - - - - - - - - - - -") # cool border

            if (PlayerScore > Self.Rounds / 2 or BotScore > Self.Rounds / 2) or PlayerScore + BotScore == Self.Rounds: # if someone won or they tied...
                print("\nFinal Score: (You)", PlayerScore, "-", BotScore, "(Bot)\n") # ...display 'final score' instead of 'current score'
            else:
                print("\nCurrent Score: (You)", PlayerScore, "-", BotScore, "(Bot)\n") # displays the current score

        if PlayerScore > BotScore: # if you won
            print("You have won the game!!")
        elif BotScore > PlayerScore: # if you lost
            print("You have lost the game.")
        else: 
            print("It's a tie!")

        print("\n- - - - - - - - - - - - - -\n") # cool border
            
        return [PlayerScore, BotScore] # returns the final scores to update player_dic
    
# - - - - - - - - - - - - - - - - - - - - - - - - end of initialization - - - - - - - - - - - - - - - - - - - - - - - - #
class HighScore:
    def __init__(self):
        self.name = None
        self.score = 0

    def update(self, player_name, player_score):
        if player_score > self.score:
            self.name = player_name
            self.score = player_score

    def __str__(self):
        if self.name is None:
            return "No high score yet."
        return f"High Score -> {self.name.capitalize()} with {self.score} total wins"
high_score = HighScore()
player_dic = {}
PlayAgain="yes"
while PlayAgain==("yes"):

    while True:
        current_player = input("Who is the current player?: ").lower()
        while True:
            NameConfirmation = input("Your name is " + current_player.capitalize() + ", is this correct? (Yes/No): ").lower() # gives the user a chance to double check their input
            if NameConfirmation == "yes": # if they write yes...
                break # ...end the loop
            elif NameConfirmation == "no": # if they write no...
                break # ...continue the confirmation loop
            else: # if they write something other than 'yes' or 'no'...
                print("Please enter 'Yes' or 'No'.")
        if NameConfirmation == "no":
            continue
        else:
            break
        
    if current_player not in player_dic:
        CPS = 0
        CBS = 0
        player_dic[current_player] = (str(CPS) + ":" + str(CBS))
    else:
        CPS = int(player_dic[current_player].split(":")[0])
        CBS = int(player_dic[current_player].split(":")[1])
    
    print("\n- - - - - - - - - - - - - -\n") # cool border
    Results = Combat().game() # runs the game and returns both player and bot final scores
    CPS = CPS + Results[0]
    CBS = CBS + Results[1]
    player_dic[current_player] = str(CPS) + ":" + str(CBS)
    high_score.update(current_player, CPS)
    print(high_score)

    while True:
        PlayAgain = input("Would you like to play again? (Yes/No): ").lower().strip()
        if PlayAgain in ["yes", "no"]:
            break
        else:
            print("Please enter 'Yes' or 'No'.")

print()
print("Thank you, come again.")
