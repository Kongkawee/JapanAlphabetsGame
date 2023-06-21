import random
from Data import Data

class GamePlay:
    def __init__(self):
        self.data = Data()
        self.hiragana = self.data.hiragana()
        self.hiragana_ex = self.data.hiragana_expanded()
        self.katakana = self.data.katakana()
        self.katakana_ex = self.data.katakana_expanded()

        self.selected_frame = self.hiragana
        self.guess_by = ""
        self.type = ""
        self.expand = True
        self.mode = ""
        self.amount = 4

        self.target = ""
        self.choice_type = ""
        self.choice = []

        self.score = 0
        self.round = 0
        self.correct = 0
        self.wrong = 0

    def guess_by_alphabet(self):
        self.guess_by = "alphabet"
        self.choice_type = "pronunciation"

    def guess_by_pronunciation(self):
        self.guess_by = "pronunciation"
        self.choice_type = "alphabet"

    def type_hiragana(self):
        self.type = "hiragana"

    def type_katakana(self):
        self.type = "katakana"

    def expand_true(self):
        self.expand = True

    def expand_false(self):
        self.expand = False

    def mode_easy(self):
        self.mode = "Easy"

    def mode_medium(self):
        self.mode = "Medium"

    def mode_hard(self):
        self.mode = "Hard"

    def mode_check(self):
        if self.mode == "Easy":
            self.amount = 4
        elif self.mode == "Medium":
            self.amount = 6
        elif self.mode == "Hard":
            self.amount = 9

    def target_frame(self):
        if self.type == "hiragana" and self.expand == False:
            self.selected_frame = self.hiragana
        elif self.type == "hiragana" and self.expand == True:
            self.selected_frame = self.hiragana_ex
        elif self.type == "katakana" and self.expand == False:
            self.selected_frame = self.katakana
        elif self.type == "katakana" and self.expand == True:
            self.selected_frame = self.katakana_ex

    def target_randomizer(self):
        digit = random.randint(0, len(self.selected_frame) - 1)
        self.target = self.selected_frame[self.guess_by][digit]

    def choice_randomizer(self):
        self.choice_cleaner()
        for digit in range(len(self.selected_frame)):
            if self.target == self.selected_frame[self.guess_by][digit]:
                self.choice.append(self.selected_frame[self.choice_type][digit])
        while len(self.choice) < self.amount:
            digit = random.randint(0, len(self.selected_frame) - 1)
            choice = self.selected_frame[self.choice_type][digit]
            if choice not in self.choice:
                self.choice.append(choice)
        random.shuffle(self.choice)

    def choice_cleaner(self):
        self.choice = []

    def score_cleaner(self):
        self.score = 0

    def on_click(self, answer):
        target_digit = 0
        for digit in range(len(self.selected_frame)):
            if self.target == self.selected_frame[self.guess_by][digit]:
                target_digit = digit

        if self.selected_frame[self.choice_type][target_digit] == answer:
            self.score += 10
            self.correct += 1
            self.round += 1
        else:
            self.score += 0
            self.wrong += 1
            self.round += 1

        self.target_randomizer()
        self.choice_cleaner()
        self.choice_randomizer()