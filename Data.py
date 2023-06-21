import pandas as pd
import random
import time

class Data:
    def __init__(self):
        self.path_hiragana = 'library/hiragana.csv'
        self.path_hiragana_expanded = 'library/hiraganaExpanded.csv'
        self.path_katakana = 'library/katakana.csv'
        self.path_katakana_expanded = 'library/katakanaExpanded.csv'

    def hiragana(self):
        hiragana = pd.read_csv(self.path_hiragana)
        return hiragana

    def hiragana_expanded(self):
        hiragana_expanded = pd.read_csv(self.path_hiragana_expanded)
        return hiragana_expanded

    def katakana(self):
        katakana = pd.read_csv(self.path_katakana)
        return katakana

    def katakana_expanded(self):
        katakana_expanded = pd.read_csv(self.path_katakana_expanded)
        return katakana_expanded

