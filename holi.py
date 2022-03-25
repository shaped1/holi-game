import os
import random
import time
from time import sleep
import sys


def is_int(num):
    try:
        int(num)
        return True
    except:
        return False


def susprint(numtime:float, text:str):
    for l in text:
        print(l, end='')
        sys.stdout.flush()
        sleep(numtime)
    print('\n')


message_1 = ["For best results, open the console in full screen\n", "Bytes are the currency this game will be using, similar to dollars or rupees.\n",
             "Each player will start with 3000 bytes and 20 bags of holi.\n", "When it is your turn, you can take an action.\n"]
message_2 = ["On your turn, you can ATTACK\n", "If you choose to attack, you will be asked which player you want to throw your bags of holi on.\n",
             "You can also choose how many bags of holi you want to throw.\n", "There is a chance you will miss, which is 40%\n", "You can buy an upgrade in the shop that increases this.\n"]
message_3 = ["On your turn, you can DEFEND\n", "Defending means that there is a high chance that if someone attacks you, they will not succeed\n",
             "When you defend, your chance of defending correctly is 70%.\n", "You can buy an upgrade in the shop that increases this.\n"]
message_4 = ['Each turn, you will earn a salary of 50 bytes.', 'You can buy an upgrade in the shop that increases your salary.', 'In addition to this, each turn, instead of defending or attacking, you can work.',
             'Working earns twice your salary and adds it to your account', "This option is good if you are low on money.\n", "When you work, your manager/boss is impresses, increasing your salary by 15%"]


def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def starting_message():
    clear()
    susprint(0.02, "Welcome to the festival of colors, also known as HOLI!\n")
    wants_instructions = input(
        "Would you like to learn how to play the game? \nAnswer with a 'yes' if you would, if you would not, answer anything else: ")
    wants_instructions = wants_instructions.lower()
    instruction_cards = [message_1, message_2, message_3]
    if wants_instructions == "true" or wants_instructions == "yes" or wants_instructions == "y" or wants_instructions == "yeah" or wants_instructions == "'yes'":
        for x in instruction_cards:
            clear()
            for y in x:
                sleep(1)
                susprint(0.02, y)

            move = input(
                "\nWould you like to continue to the next page? Please enter a 'c' to continue.")
            susprint(0.02, move)
            while True:
                if move == "c":
                    break
                susprint(0.02, x)
                move = input(
                    "Your previous input was not a 'c' and was ignored. \nWould you like to continue to the next page? Please enter a 'c' to continue.")
    susprint(0.02, "You are now ready to play!")
    sleep(1)
    clear()


class Player:
    def __init__(self) -> None:
        self.name = input("Enter player name: ")
        self.money = 3000
        self.ammunition = 20
        # Bags of holi successfully thrown on another player
        self.points = 0
        self.color = []
        # Used defend on last turn or not
        self.defend = False
        self.turns = 0
        # Accuracy of attack
        self.accuracy = 60
        # Defense accuracy
        self.defense_proficiency = 70
        # self.defendedlast is used in maintaining 2 turn defense.
        self.defendedlast = False
        # justdefend is to make sure consecutive defenses are not set up. 
        self.justdefend = False
        self.gender = "none set at the moment"
        self.bags_of_color = 20
        self.salary = 50
        self.raisevalue = 1.15
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
        players = input(
            "Enter the number of players playing holi. 2-9 players allowed: ")
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
                players = input(
                    "Please try again. Enter the number of players playing holi. 2-9 players allowed: ")
        self.num_players = int(players)

    def create_players(self):
        self.players = []
        self.names = []
        while len(self.players) < self.num_players:
            new_player = Player()
            while True:
                if new_player.name in self.names:
                    susprint(
                        0.02, "That name is already taken! Please try again!")
                    new_player = Player()
                else:
                    break
            self.players.append(new_player)
            self.names.append(new_player.name)

    def __str__(self) -> str:
        message = []
        os.system('cls' if os.name == 'nt' else 'clear')
        message.append("CURRENT GAME STATUS")
        for player in self.players:
            message.append(
                f"Player {player.name}: has {player.bags_of_color} bags of color, has {player.points} points, .")
        return "\n".join(message)

    def attack(self, player: Player):
        clear()
        sleep(0.5)
        if random.random() > player.accuracy:
            print("By a stroke of fate, a meteor lands and knocks the bags of holi out of your hand.\nYou cannot attack this turn.\nIncrease the accuracy in the shop.")
            return;
        susprint(0.02, f'{player.name}, you have chosen to attack.')
        victim = input(
            f"Who would you like to attack? Current players are {self.names}: ")
        while True:
            if victim in self.names:
                break
            victim = input(
                f"That's not a player! Current players are {self.names}: ")
            print(victim)
            sleep(5)
        clear()
        bags = input(
            f'{player.name}, you have chosen to attack {victim}.\nYou have {player.ammunition} bags. How many bags of color would you like to throw at them? ')
        while True:
            if is_int(bags):
                break
            bags = input('Not a valid amount of bags! Try again: ')
        vicplayer = Player()
        for p in self.players():
            if p.name == victim:
                vicplayer = p
                break
        if int(bags) > player.ammunition:
            susprint(0.02, '\nYou have attempted to throw more bags than you have.\nFor this action, you will not be allowed to throw any bags this turn.\nNext time, be careful!')
        elif vicplayer.defend:
            clear()
            susprint(
                0.02, 'That player has successfully put up a defense!\nYou throw your bags of holi against them but it is of no use.')
        else:
            clear()
            susprint(
                0.01, f"You are aiming your bags of color at {vicplayer.name}. \n")
            color = input("What color powder are the bags?")
            while True:
                if len(color) < 11:
                    break
                color = input(
                    "That color is too long. What color are the bags?")
            vicplayer.color.append(f"{bags} of {color}")
            clear()
            susprint(0.02, f"{bags} of {color} have been thrown.")
            sleep(0.5)

    def work(self, player: Player):
        clear()
        susprint(
            0.02, f"{player.name}, you have chosen to take an extra shift at your workplace. \nWorking..\nWorking..")
        x = int(random.random()*100)
        y = int(random.random()*100)
        time.sleep(3)
        susprint(0.02, f"You have to do a math problem to collect your paycheck!")
        z = 8
        problem_missed = False
        answer = -1
        while True:
            if problem_missed:
                break
            time.sleep(1.5)

            for i in range(z):
                clear()
                susprint(
                    0.000005, f"What is {x} + {y}?\n{z-i} seconds remaining!")
                time.sleep(1)
            for i in range(3):
                clear()
                susprint(
                    0.000005, f"You have {3-i} seconds to type the answer!")
                answer = input('Enter the answer here: ')
                time.sleep(1)
            if answer == x+y:
                clear()
                susprint(0.05, f"HOORAY! {x+y} was correct!")
                player.money += player.salary
                susprint(0.02, f"You earnt {player.salary} bytes")
                player.salary *= self.raisevalue
                time.sleep(1.2)
                susprint(
                    0.01, f"Huh? Your boss wants to give you a {self.raisevalue*100-100}% raise for being so good at math! \nYour current salary is {self.salary}")
            else:
                clear()
                susprint(
                    0.05, f"That was not correct.\nThe correct answer is {x+y}.\nBetter luck next time!")
                problem_missed = True
            answer = -1

    def defend(self, player: Player) -> None:
        clear()
        sleep(0.3)
        if player.defend:
            susprint(0.015, f"{player.name}, you already have a defense up!")
            sleep(3)
            return;
        elif player.justdefend:
            susprint(0.015,f"{player.name}, you just defended!")
            sleep(3)
            return;
        
        susprint(0.02, f"{player.name}, you have chosen to defend.")
        susprint(0.02, f"The probability of defending successfully for 2 turns is {player.defense_proficiency}%.")
        # The following section of code is insignificant.
        # I could've just made a random guess for the user, but what fun is that??
        numguess = input(f"To decide your fate, enter a number from 1-100: ")
        while True:
            while True:
                if is_int(numguess):
                    break
                numguess = input("Please enter an integer: ")
            if int(numguess) in range(1,101):
                break
            numguess = input("Please enter an integer from 1-100: ")
        clear()
        susprint(0.02,f"Your guess is {numguess}.")
        for i in range(1,6):
            susprint(0.003,f"Rolling the dice{'.'*i}")
        temp = range(1,101)
        random.shuffle(temp)
        temp1 = []
        for i in range(player.defense_proficiency):
            temp1.append(temp[i])
        if numguess in temp1:
            susprint(0.02,"You set up a defense!")
            sleep(0.5)
            player.defend = True
            return
        else:
            susprint(0.02, "Your guess did not work. Your defense was not set up.")
            sleep(2)
            return
        
    def shop(self, player: Player):
        clear()
        susprint(0.005,f"""
    {player.name}, welcome to the shop!
    {player.money} bytes available.
    750 - D: Increase defense proficiency by 5%. Currently at {player.defense_proficiency}%
    750 - A: Increase attack accuracy by 5%. Currently at {player.accuracy}%
    25 - H: Buy bags of holi.
                 """)
        o = input("What would you like to buy?: ")
        o = o.upper
        options = ['D','A','H']
        while not o in options:
            o = input("That is not an option.\nWhat would you like to buy?")
        if o == 'D':
            clear()
            if player.defense_proficiency == 100:
                print("Your defense proficiency is already 100%.")
                sleep(1)
                return
            player.defense_proficiency +=5
            print("Defense proficiency increased.")
            
        elif o == 'A':
            pass
        elif o == 'H':
            pass
    def turn(self, player: Player):
        # Defense lasts 2 turns long. 
        no_defense = False
        if player.justdefend:
            no_defense = True
            player.justdefend = False
        if player.defend and player.defendedlast:
            player.defend = False
            player.defendedlast = False
            player.justdefend = True
        elif player.defend and not player.defendedlast:
            player.defendedlast = True
        player.money += player.salary
        clear()
        susprint(0.005,f"""
        {player.name}, it is your turn. 
        What would you like to do?
        Please respond with the letter or the word.
        A: Attack ({player.bags_of_color} bags of color and {player.accuracy})
        D: Defend ({player.defense_proficiency}%)
        W: Work (earn money)
        S: Shop (buy upgrades and bags of holi)     
                    """)
        if player.defend:
            susprint(0.005,"\nYou have a defense set up from last turn.\nTrying to defend will result with the loss of your turn.")
        elif not player.defend:
            susprint(0.005, "\nYou do not have a defense set up.")
        elif no_defense:
            susprint(0.005, "\nYou cannot defend this turn because you had a defense for the last two turns.")
        option = input("Please respond with the letter or the word: \n")
        clear()
        sleep(2)
        if option.lower() == 'a':
            self.attack(player)
        if option.lower() == 'w':
            self.work(player)
        if option.lower() == 'd':
            self.defend(player)
        print(option)


if __name__ == "__main__":
    starting_message()
    new_game = Game()
    new_game.input_num_players()
    new_game.create_players()
    for y in range(5):
        for x in new_game.players:
            print(x)
            print("")
            new_game.turn(x)
