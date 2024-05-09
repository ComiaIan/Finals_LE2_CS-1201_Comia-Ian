class Score:
    def __init__(self, score_file):
        self.score_file = score_file

    def load_score(self):
        try:
            with open(self.score_file, 'r') as file:
                return int(file.read())
        except FileNotFoundError:
            return None
        except ValueError:
            print("Error: Invalid data in score file.")
    
    def load_score_date(self):
        try:
            with open(self.score_file, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return None
