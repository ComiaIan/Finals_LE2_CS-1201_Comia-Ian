import os
from utils.score import Score
from datetime import datetime
import random

class DiceGame(Score):
    def __init__(self, score_file):
        super().__init__(score_file)
        self.user_folder = 'user'
        self.score_file = os.path.join(self.user_folder, 'score.txt')
        self.create_data_folder()

    def create_data_folder(self):
        if not os.path.exists(self.user_folder):
            os.makedirs(self.user_folder)

    def load_scores(self):
        if os.path.exists(self.score_file):
            with open(self.score_file, 'r') as file:
                scores = []
                for line in file:
                    score, username, date = line.strip().split(', ')
                    try:
                        score = int(score)
                    except ValueError:
                        print(f"\tInvalid score value for user {username} on date {date}. Skipping this entry.")
                        continue
                    scores.append((username, int(score), date))
                return scores
        return []

    def save_scores(self, username, score):
        if not isinstance(score, int):
            print(f"\tInvalid score value: {score}")
        try:
            with open(self.score_file, 'a') as file:
                now = datetime.now()
                score_date = now.strftime("%Y-%m-%d %H:%M:%S")
                file.write(f'{score}, {username}, Achieved on: {score_date}\n')
        except IOError:
            return print("\tAn error occurred while trying to save the score.")

    def play_game(self, username):
        stage = 1
        total_score = 0
        game = True

        while game:
            user_score = 0
            cpu_score = 0

            while user_score < 2 and cpu_score < 2:
                user_num = random.randint(1,6)
                cpu_num = random.randint(1,6)

                if user_num > cpu_num:
                    print(f"\t{username} rolled: {user_num}\n\tCPU: {cpu_num}\n\n\t{username} Won!\n")
                    user_score += 1
                elif user_num < cpu_num:
                    print(f"\t{username} rolled: {user_num}\n\tCPU: {cpu_num}\n\n\tCPU Won!\n")
                    cpu_score += 1
                else:
                    print(f"\t{username} rolled: {user_num}\n\tCPU: {cpu_num}\n\n\tDRAW!\n")
                    continue

            if user_score > cpu_score:
                total_score += 3 + user_score                
                print(f"\tCongratulations! You won stage {stage}!\n\t{username}'s current score: {total_score}")
                stage += 1
                continue_game = str(input("\tContinue to the next stage? (y/n): "))

                if continue_game.lower() == "n":
                    print("\tThanks for playing!")
                    game = False
                elif continue_game.lower() != "y":
                    print("\tInvalid input. Please enter 'y' or 'n'.")                    
            else:
                total_score += user_score
                print("\tGame over.\n")  
                game = False
        return total_score                            
        
    def start_game(self, username):
        total_score = self.play_game(username)
        self.save_scores(username, total_score)

    def show_top_scores(self):
        scores = self.load_scores()
        scores.sort(key=lambda x: x[1], reverse=True)

        print("\n\t---TOP PLAYERS---")

        print(f'{"\n\tRanking":<10}{"Username":<10}{"Score":<10}{"Date":<10}')

        for i in range(10):
            if i < len(scores):
                username, score, date = scores[i]
                print(f'\t{i+1:<10}{username:<10}{score:<10}{date:<10}')
            else:
                print(f"{i+1:<10}---")

    def menu(self, username):
        print(f"\n\tWelcome to Dice Game!")
        while True:
            print("\n\t\t1. Play Game")
            print("\t\t2. Show Top Scores")
            print("\t\t3. Log out")
            choice = input("\n\tEnter Choice: ")

            if choice == '1':
                self.play_game(username)
            elif choice == '2':
                self.show_top_scores()
            elif choice == '3':
                print("\tLogging out. Thanks for playing...\n")
                return False
            else:
                print("")
