import random


class RPCGame:
    def __init__(self):
        self.rule_dict = {"rock": 0, "paper": 1, "scissors": 2}
        self.rule_list = list(self.rule_dict.keys())
        self.score = 0

    def build_rule_dict(self, rule_string=""):
        if rule_string != "":
            rule_list = rule_string.split(",")
            rule_dict = dict((rule_list[i], i) for i in range(len(rule_list)))
            self.rule_dict = rule_dict
            self.rule_list = rule_list

    def check_input(self, string):
        if string == "!rating":
            print(f"Your rating: {self.score}")
            return False
        elif self.rule_dict.get(string, -1) == -1:
            print("Invalid input")
            return False
        return True

    def find_winner(self, input_string):
        input_choice = self.rule_dict[input_string]
        computer_choice = random.randrange(0, len(self.rule_dict))
        n = len(self.rule_list)
        k = input_choice
        p = computer_choice
        beater_switch = k - (n + 1) / 2
        if input_choice == computer_choice:
            print(f"There is a draw ({self.rule_list[computer_choice]})")
            self.score += 50
        elif (beater_switch < 0 and k < p <= n + beater_switch) or \
                (beater_switch >= 0 and not beater_switch < p < k):
            print(f"Sorry, but computer chose {self.rule_list[computer_choice]}")
        else:
            print(f"Well done. Computer chose {self.rule_list[computer_choice]} and failed")
            self.score += 100

    def get_score(self, name):
        scoreboard = open("rating.txt", "r")
        for line in scoreboard:
            row = line.split(" ")
            if row[0] == name:
                self.score = int(row[1])
        scoreboard.close()

    def run(self):
        user_input = input("Enter your name: ")
        if user_input != "!exit":
            print(f"Hello, {user_input}")
            self.get_score(user_input)
            self.build_rule_dict(input())
            print("Okay, let's start")
            user_input = input()
            while user_input != "!exit":
                if self.check_input(user_input) is True:
                    self.find_winner(user_input)
                user_input = input()
        print("Bye!")


game = RPCGame()
game.run()
