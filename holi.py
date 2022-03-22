import os
import random
from time import sleep

message_1 = ["For best results, open the console in full screen","Bytes are the currency this game will be using, similar to dollars or rupees.","Each player will start with 3000 bytes and 20 bags of holi.","When it is your turn, you can take an action."]
message_2 = ["On your turn, you can ATTACK","If you choose to attack, you will be asked which player you want to throw your bags of holi on.","You can also choose how many bags of holi you want to throw.", "There is a chance you will miss, which is 40%", "You can buy an upgrade in teh shop that increases this."]
message_3 = ["On your turn, you can DEFEND", "Defending means that there is a high chance that if someone attacks you, they will not succeed", "When you defend, your chance of defending correctly is 70%.", "You can buy an upgrade in the shop that increases this."]
message_4 = ['Each turn, you will earn a salary of 50 bytes.', 'You can buy an upgrade in the shop that increases your salary.', 'In addition to this, each turn, instead of defending or attacking, you can work.', 'Working earns twice your salary and adds it to your account', "This option is good if you are low on money.", "When you work, your manager/boss is impresses, increasing your salary by 15%"]

def clear():
    if os.name == "nt":
        os.system('cls')
    else: 
        os.system('clear')

def starting_message():
    print("Welcome to the festival of colors, also known as HOLI!")
    wants_instructions = input("Would you like to learn how to play the game? \nAnswer with a 'yes' if you would, if you would not, answer anything else: ")
    wants_instructions = wants_instructions.lower()
    instruction_cards = [message_1, message_2, message_3]
    if wants_instructions == "true" or wants_instructions == "yes" or wants_instructions == "y" or wants_instructions == "yeah" or wants_instructions == "'yes'":
        for x in instruction_cards:
            clear()
            for y in x:
                sleep(1)
                print(y)
                
            move = input("\nWould you like to continue to the next page? Please enter a 'c' to continue.")
            print(move)
            while True:
                if move == "c":
                    break
                print(x)
                move = input("Your previous input was not a 'c' and was ignored. \nWould you like to continue to the next page? Please enter a 'c' to continue.")
    print("You are now ready to play!")
class Player:
    def __init__(self) -> None:
        self.name = input("Enter player name: ")
        self.money = 3000
        self.ammunition = 20
        self.color = []
        # Bags of holi successfully thrown on another player
        self.points = 0
        # Used defend on last turn or not
        self.defend = False
        self.turns = 0
        # Accuracy of attack
        self.accuracy=60
        # Defense accuracy
        self.defense_proficiency = 70
        self.gender = "none set at the moment"
        
        self.salary = 50
        
        self.upgrades = []
    def __str__(self) -> str:
        return """
              PLAYER {self.name} INFO
              _____________________________
              - Money: {self.money}
              - Bags of holi: {self.ammunition}
              - Points: {self.points}
              - Attack accuracy: {self.accuracy}
              - Defense accuracy: {self.defense_proficiency}
              """
        
class Game:
    def __init__(self) -> None:
        pass
    def input_num_players(self):
        players = input("Enter the number of players playing holi. 2-9 players allowed: ")
        valid_input = False
        
        if players.isdigit:
            try:
                int(players)
                valid_input = True
            except: 
                pass
        while not valid_input:
            try:
                int(players)
                valid_input = True
            except: 
                players = input("Please try again. Enter the number of players playing holi. 2-9 players allowed: ")
        self.num_players = int(players)
    
    def create_players(self):
        self.players = []
        self.names = []
        while len(self.players) < self.num_players:
            new_player = Player()
            while True:
                if new_player.name in self.names:
                    print("That name is already taken! Please try again!")
                    new_player = Player()
                else:
                    break
            self.players.append(new_player)
            self.names.append(new_player.name)
    
    def __str__(self) -> str:
        message = []
        os.system('cls' if os.name=='nt' else 'clear')
        message.append("CURRENT GAME STATUS")
        for player in self.players:
            message.append(f"Player {player.name}: has {player.bags_of_color} bags of color, has {player.points} points, .")
        return "\n".join(message)

def turn(current_game,player):
    clear()
    option = input(f"""
                    '{player.name}, it is your turn. 
                    What would you like to do?
                    Please respond with the letter or the word.
                    A: Attack ({player.bags_of_color} bags of color and {player.accuracy})
                    D: Defend ({player.defense_proficiency}%)'
                    W: Work (earn money)
                    S: Shop (buy upgrades and bags of holi)     
                    The following options do not require a turn.
                    You can still make a move after this.
                    I: Get info about how to play the game (you still have a turn after this)
                    P: Get info about a player (you still have a turn after this)
                    L: Get info about all players (you still have a turn after this.)
                   """)


if __name__ == "__main__":
    starting_message()
    new_game = Game()
    new_game.input_num_players()
    new_game.create_players()
    for x in new_game.players:
        print(x)