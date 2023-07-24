import tkinter as tk
from PIL import ImageTk, Image
from GamePlay import GamePlay

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('JapanAlphabetsGame')
        self.geometry('800x700')
        self.configure(bg='#FFC7BA')
        self.resizable(False, False)
        """
        Configure columns
        """
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.main_title = tk.Label
        self.photo = None
        self.main_menu()

        self.game = GamePlay()
        self.expand_mode_show = tk.StringVar()
        self.expand_mode_show.set("-")
        self.difficulty_select_show = tk.StringVar()
        self.difficulty_select_show.set("-")
        self.score = tk.StringVar()
        self.score.set(f"Score : {self.game.score}")
        self.correct_percent = tk.StringVar()
        self.target = tk.StringVar()
        self.target.set(self.game.target)
        self.choice_1 = tk.StringVar()
        self.choice_2 = tk.StringVar()
        self.choice_3 = tk.StringVar()
        self.choice_4 = tk.StringVar()
        self.choice_5 = tk.StringVar()
        self.choice_6 = tk.StringVar()
        self.choice_7 = tk.StringVar()
        self.choice_8 = tk.StringVar()
        self.choice_9 = tk.StringVar()

    def main_menu(self):
        self.clear_page()
        self.main_title = tk.Label(self, text="Alphabettle!", font=("Helvetica", 48),
                              background="#FF92A5", foreground="white", borderwidth=5, highlightthickness=2)
        by_alphabet = tk.Button(self, text="Guess by alphabet", font=("Helvetica", 24),
                                relief="flat", width=20, height=2, command=self.stage_selection_by_alphanet)
        by_pronunciation = tk.Button(self, text="Guess by pronunciation", font=("Helvetica", 24),
                                     relief="flat", width=20, height=2, command=self.stage_selection_by_pronunciation)
        library = tk.Button(self, text="Library", font=("Helvetica", 24), relief="flat",
                            width=20, height=2, command=self.library_menu)
        quit_button = tk.Button(self, text="Quit", font=("Helvetica", 24), relief="flat",
                                width=10, height=2, command=self.quit)

        image = Image.open("pictures/anya-diary.png")
        height = 450
        width = int(height * (9/16))
        image = image.resize((height, width))
        self.photo = ImageTk.PhotoImage(image)
        welcome_anya = tk.Label(self, image=self.photo)

        self.main_title.grid(row=0, columnspan=5, sticky="EW")
        welcome_anya.grid(row=2, column=1, columnspan=3, pady=(40, 0))
        by_alphabet.grid(row=3, column=1, pady=(40, 0), sticky="EW")
        by_pronunciation.grid(row=3, column=3, pady=(40, 0), sticky="EW")
        library.grid(row=4, column=1, columnspan=3, pady=(20, 0), sticky="EW")
        quit_button.grid(row=5, column=1, pady=(40, 0), sticky="W")

    def library_menu(self):
        self.clear_page()
        title = tk.Label(self, text="Library", font=("Helvetica", 20), borderwidth=5,
                         background="#FF92A5", foreground="white",highlightthickness=2)

        image = Image.open("pictures/spy_anya.jpg")
        height = 450
        width = int(height * (9 / 16))
        image = image.resize((height, width))
        self.photo = ImageTk.PhotoImage(image)
        library_anya = tk.Label(self, image=self.photo)

        hiragana_table = tk.Button(self, text="Hiragana", font=("Helvetica", 24), relief="flat",
                            width=20, height=2, command=self.hiragana_library)
        katakana_table = tk.Button(self, text="Katakana", font=("Helvetica", 24), relief="flat",
                            width=20, height=2, command=self.katakana_library)
        back_button = tk.Button(self, text="Back", font=("Helvetica", 24), relief="flat",
                                width=10, height=2, command=self.main_menu)

        title.grid(row=1, column=1, columnspan=3, pady=(20, 0))
        library_anya.grid(row=2, column=1, columnspan=3, pady=(20, 0))
        hiragana_table.grid(row=3, column=1, pady=(40, 0), sticky="EW")
        katakana_table.grid(row=3, column=3, pady=(40, 0), sticky="EW")
        back_button.grid(row=5, column=1, pady=(40, 0), sticky="W")

    def hiragana_library(self):
        self.clear_page()
        title = tk.Label(self, text="Hiragana Table", font=("Helvetica", 24),
                              background="#FF92A5", foreground="white", borderwidth=5, highlightthickness=2)
        back_button = tk.Button(self, text="Back", font=("Helvetica", 24), relief="flat",
                                width=5, height=2, command=self.library_menu)
        image = Image.open("pictures/hiragana-base.jpg")
        height = 350
        width = int(height * (1204 / 816))
        image = image.resize((height, width))
        self.photo = ImageTk.PhotoImage(image)
        hiragana_chart = tk.Label(self, image=self.photo)

        title.grid(row=2, column=1, pady=(40, 0), sticky="NW")
        hiragana_chart.grid(row=2, column=1, columnspan=3, rowspan=3, pady=(40, 0), sticky="E")
        back_button.grid(row=4, column=1, pady=(40, 0), sticky="SW")

    def katakana_library(self):
        self.clear_page()
        title = tk.Label(self, text="Katakana Table", font=("Helvetica", 24),
                         background="#FF92A5", foreground="white", borderwidth=5, highlightthickness=2)
        back_button = tk.Button(self, text="Back", font=("Helvetica", 24), relief="flat",
                                width=5, height=2, command=self.library_menu)
        image = Image.open("pictures/katakana-base.jpg")
        height = 350
        width = int(height * (1198 / 814))
        image = image.resize((height, width))
        self.photo = ImageTk.PhotoImage(image)
        katakana_chart = tk.Label(self, image=self.photo)

        title.grid(row=2, column=1, pady=(40, 0), sticky="NW")
        katakana_chart.grid(row=2, column=1, columnspan=3, rowspan=3, pady=(40, 0), sticky="E")
        back_button.grid(row=4, column=1, pady=(40, 0), sticky="SW")

    def clear_page(self):
        for widget in self.winfo_children():
            if widget != self.main_title:
                widget.destroy()

    def stage_selection_by_alphanet(self):
        self.clear_page()
        self.game.guess_by_alphabet()
        title = tk.Label(self, text="Guess by alphabet", font=("Helvetica", 20), borderwidth=5,
                         background="#FF92A5", foreground="white", highlightthickness=2)

        image = Image.open("pictures/spy_anya.jpg")
        height = 450
        width = int(height * (9 / 16))
        image = image.resize((height, width))
        self.photo = ImageTk.PhotoImage(image)
        library_anya = tk.Label(self, image=self.photo)

        hiragana_table = tk.Button(self, text="Hiragana", font=("Helvetica", 24), relief="flat",
                                   width=20, height=2, command=self.type_selection_hiragana)
        katakana_table = tk.Button(self, text="Katakana", font=("Helvetica", 24), relief="flat",
                                   width=20, height=2, command=self.type_selection_katakana)
        back_button = tk.Button(self, text="Back", font=("Helvetica", 24), relief="flat",
                                width=10, height=2, command=self.main_menu)

        title.grid(row=1, column=1, columnspan=3, pady=(20, 0))
        library_anya.grid(row=2, column=1, columnspan=3, pady=(20, 0))
        hiragana_table.grid(row=3, column=1, pady=(40, 0), sticky="EW")
        katakana_table.grid(row=3, column=3, pady=(40, 0), sticky="EW")
        back_button.grid(row=5, column=1, pady=(40, 0), sticky="W")

    def stage_selection_by_pronunciation(self):
        self.clear_page()
        self.game.guess_by_pronunciation()
        title = tk.Label(self, text="Guess by pronunciation", font=("Helvetica", 20), borderwidth=5,
                         background="#FF92A5", foreground="white", highlightthickness=2)

        image = Image.open("pictures/spy_anya.jpg")
        height = 450
        width = int(height * (9 / 16))
        image = image.resize((height, width))
        self.photo = ImageTk.PhotoImage(image)
        library_anya = tk.Label(self, image=self.photo)

        hiragana_table = tk.Button(self, text="Hiragana", font=("Helvetica", 24), relief="flat",
                                   width=20, height=2, command=self.type_selection_hiragana)
        katakana_table = tk.Button(self, text="Katakana", font=("Helvetica", 24), relief="flat",
                                   width=20, height=2, command=self.type_selection_katakana)
        back_button = tk.Button(self, text="Back", font=("Helvetica", 24), relief="flat",
                                width=10, height=2, command=self.main_menu)

        title.grid(row=1, column=1, columnspan=3, pady=(20, 0))
        library_anya.grid(row=2, column=1, columnspan=3, pady=(20, 0))
        hiragana_table.grid(row=3, column=1, pady=(40, 0), sticky="EW")
        katakana_table.grid(row=3, column=3, pady=(40, 0), sticky="EW")
        back_button.grid(row=5, column=1, pady=(40, 0), sticky="W")

    def type_selection_hiragana(self):
        self.clear_page()
        self.game.type_hiragana()
        self.mode_selection_page()

    def type_selection_katakana(self):
        self.clear_page()
        self.game.type_katakana()
        self.mode_selection_page()

    def expand_true(self):
        self.game.expand_true()
        self.expand_mode_show.set("Yes")

    def expand_false(self):
        self.game.expand_false()
        self.expand_mode_show.set("No")

    def mode_easy(self):
        self.game.mode_easy()
        self.difficulty_select_show.set("Easy")

    def mode_medium(self):
        self.game.mode_medium()
        self.difficulty_select_show.set("Medium")

    def mode_hard(self):
        self.game.mode_hard()
        self.difficulty_select_show.set("Hard")

    def mode_selection_page(self):
        title = tk.Label(self, text="Mode selection", font=("Helvetica", 20), borderwidth=5,
                         background="#FF92A5", foreground="white", highlightthickness=2)

        expand_mode_title = tk.Label(self, text="Expand mode", font=("Helvetica", 20), borderwidth=5,
                         background="white", foreground="black", highlightthickness=2)
        expand_mode_confirm = tk.Label(self, textvariable=self.expand_mode_show, font=("Helvetica", 20), borderwidth=5, width=10,
                         background="white", foreground="black", highlightthickness=2)
        expand_mode_true = tk.Button(self, text="Yes", font=("Helvetica", 20), relief="flat",
                                   width=10, height=2, command=self.expand_true)
        expand_mode_false = tk.Button(self, text="No", font=("Helvetica", 20), relief="flat",
                                   width=10, height=2, command=self.expand_false)


        difficult_mode_title = tk.Label(self, text="Select difficulty", font=("Helvetica", 20), borderwidth=5,
                                     background="white", foreground="black", highlightthickness=2)
        difficult_mode_confirm = tk.Label(self, textvariable=self.difficulty_select_show, font=("Helvetica", 20), borderwidth=5, width=10,
                                       background="white", foreground="black", highlightthickness=2)
        difficult_mode_easy = tk.Button(self, text="Easy", font=("Helvetica", 20), relief="flat",
                                     width=10, height=2, command=self.mode_easy)
        difficult_mode_medium = tk.Button(self, text="Medium", font=("Helvetica", 20), relief="flat",
                                      width=10, height=2, command=self.mode_medium)
        difficult_mode_hard = tk.Button(self, text="Hard", font=("Helvetica", 20), relief="flat",
                                          width=10, height=2, command=self.mode_hard)

        start_game = tk.Button(self, text="START!", font=("Helvetica", 20), relief="flat",
                                          width=10, height=2, command=self.start_game)

        back_button = tk.Button(self, text="Back", font=("Helvetica", 20), relief="flat",
                                          width=10, height=2, command=self.main_menu)

        title.grid(row=1, column=0, columnspan=5, pady=(20, 0))
        expand_mode_title.grid(row=2, column=1, columnspan=3, pady=(40, 0))
        expand_mode_confirm.grid(row=2, column=3, pady=(40, 0))
        expand_mode_true.grid(row=3, column=1, columnspan=2, pady=(20, 0))
        expand_mode_false.grid(row=3, column=2, columnspan=2, pady=(20, 0))

        difficult_mode_title.grid(row=4, column=1, columnspan=3, pady=(40, 0))
        difficult_mode_confirm.grid(row=4, column=3, pady=(40, 0))
        difficult_mode_easy.grid(row=5, column=1, pady=(20, 0))
        difficult_mode_medium.grid(row=5, column=2, pady=(20, 0))
        difficult_mode_hard.grid(row=5, column=3, pady=(20, 0))

        start_game.grid(row=6, column=3, pady=(80, 0))
        back_button.grid(row=6, column=1, pady=(80, 0))

    def start_game(self):
        if self.game.mode == "Easy":
            self.start_game_easy()
        elif self.game.mode == "Medium":
            self.start_game_medium()
        elif self.game.mode == "Hard":
            self.start_game_hard()

    def start_game_easy(self):
        self.clear_page()
        self.game.score = 0
        self.game.round = 0
        self.game.correct = 0
        self.game.wrong = 0
        self.easy_mode_setup()

    def on_click_easy(self, selected_choice):
        self.game.on_click(selected_choice)

        self.clear_page()
        self.easy_mode_setup()
        self.finish_button()

    def easy_mode_setup(self):
        self.game.target_frame()
        self.game.mode_check()
        self.game.target_randomizer()
        self.game.choice_cleaner()
        self.game.choice_randomizer()

        self.target.set(self.game.target)
        self.score.set(f"Score : {self.game.score}")
        self.choice_1.set(self.game.choice[0])
        self.choice_2.set(self.game.choice[1])
        self.choice_3.set(self.game.choice[2])
        self.choice_4.set(self.game.choice[3])

        target = tk.Label(self, textvariable=self.target, font=("Helvetica", 48), borderwidth=5,
                          background="white", foreground="black", highlightthickness=2)
        score = tk.Label(self, textvariable=self.score, font=("Helvetica", 20), borderwidth=3,
                         background="white", foreground="black", highlightthickness=2)
        choice_1 = tk.Button(self, textvariable=self.choice_1, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_easy(self.game.choice[0]))
        choice_2 = tk.Button(self, textvariable=self.choice_2, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_easy(self.game.choice[1]))
        choice_3 = tk.Button(self, textvariable=self.choice_3, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_easy(self.game.choice[2]))
        choice_4 = tk.Button(self, textvariable=self.choice_4, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_easy(self.game.choice[3]))

        target.grid(row=1, column=0, columnspan=5, pady=(40, 0))
        score.grid(row=1, column=3, pady=(40, 0), padx=(60, 0))
        choice_1.grid(row=2, column=1, pady=(60, 0))
        choice_2.grid(row=2, column=3, pady=(60, 0))
        choice_3.grid(row=3, column=1, pady=(40, 0))
        choice_4.grid(row=3, column=3, pady=(40, 0))

    def start_game_medium(self):
        self.clear_page()
        self.game.score = 0
        self.game.round = 0
        self.game.correct = 0
        self.game.wrong = 0
        self.medium_mode_setup()

    def on_click_medium(self, selected_choice):
        self.game.on_click(selected_choice)

        self.clear_page()
        self.medium_mode_setup()
        self.finish_button()

    def medium_mode_setup(self):
        self.game.target_frame()
        self.game.mode_check()
        self.game.target_randomizer()
        self.game.choice_cleaner()
        self.game.choice_randomizer()

        self.target.set(self.game.target)
        self.score.set(f"Score : {self.game.score}")
        self.choice_1.set(self.game.choice[0])
        self.choice_2.set(self.game.choice[1])
        self.choice_3.set(self.game.choice[2])
        self.choice_4.set(self.game.choice[3])
        self.choice_5.set(self.game.choice[4])
        self.choice_6.set(self.game.choice[5])

        target = tk.Label(self, textvariable=self.target, font=("Helvetica", 48), borderwidth=5,
                          background="white", foreground="black", highlightthickness=2)
        score = tk.Label(self, textvariable=self.score, font=("Helvetica", 20), borderwidth=3,
                         background="white", foreground="black", highlightthickness=2)
        choice_1 = tk.Button(self, textvariable=self.choice_1, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_medium(self.game.choice[0]))
        choice_2 = tk.Button(self, textvariable=self.choice_2, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_medium(self.game.choice[1]))
        choice_3 = tk.Button(self, textvariable=self.choice_3, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_medium(self.game.choice[2]))
        choice_4 = tk.Button(self, textvariable=self.choice_4, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_medium(self.game.choice[3]))
        choice_5 = tk.Button(self, textvariable=self.choice_5, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_medium(self.game.choice[4]))
        choice_6 = tk.Button(self, textvariable=self.choice_6, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_medium(self.game.choice[5]))

        target.grid(row=1, column=0, columnspan=5, pady=(40, 0))
        score.grid(row=1, column=3, pady=(40, 0), padx=(60, 0))
        choice_1.grid(row=2, column=1, pady=(60, 0))
        choice_2.grid(row=2, column=2, pady=(60, 0))
        choice_3.grid(row=2, column=3, pady=(60, 0))
        choice_4.grid(row=3, column=1, pady=(40, 0))
        choice_5.grid(row=3, column=2, pady=(40, 0))
        choice_6.grid(row=3, column=3, pady=(40, 0))

    def start_game_hard(self):
        self.clear_page()
        self.game.score = 0
        self.game.round = 0
        self.game.correct = 0
        self.game.wrong = 0
        self.hard_mode_setup()

    def on_click_hard(self, selected_choice):
        self.game.on_click(selected_choice)

        self.clear_page()
        self.hard_mode_setup()
        self.finish_button()

    def hard_mode_setup(self):
        self.game.target_frame()
        self.game.mode_check()
        self.game.target_randomizer()
        self.game.choice_cleaner()
        self.game.choice_randomizer()

        self.target.set(self.game.target)
        self.score.set(f"Score : {self.game.score}")
        self.choice_1.set(self.game.choice[0])
        self.choice_2.set(self.game.choice[1])
        self.choice_3.set(self.game.choice[2])
        self.choice_4.set(self.game.choice[3])
        self.choice_5.set(self.game.choice[4])
        self.choice_6.set(self.game.choice[5])
        self.choice_7.set(self.game.choice[6])
        self.choice_8.set(self.game.choice[7])
        self.choice_9.set(self.game.choice[8])

        target = tk.Label(self, textvariable=self.target, font=("Helvetica", 48), borderwidth=5,
                          background="white", foreground="black", highlightthickness=2)
        score = tk.Label(self, textvariable=self.score, font=("Helvetica", 20), borderwidth=3,
                         background="white", foreground="black", highlightthickness=2)
        choice_1 = tk.Button(self, textvariable=self.choice_1, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_hard(self.game.choice[0]))
        choice_2 = tk.Button(self, textvariable=self.choice_2, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_hard(self.game.choice[1]))
        choice_3 = tk.Button(self, textvariable=self.choice_3, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_hard(self.game.choice[2]))
        choice_4 = tk.Button(self, textvariable=self.choice_4, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_hard(self.game.choice[3]))
        choice_5 = tk.Button(self, textvariable=self.choice_5, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_hard(self.game.choice[4]))
        choice_6 = tk.Button(self, textvariable=self.choice_6, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_hard(self.game.choice[5]))
        choice_7 = tk.Button(self, textvariable=self.choice_7, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_hard(self.game.choice[6]))
        choice_8 = tk.Button(self, textvariable=self.choice_8, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_hard(self.game.choice[7]))
        choice_9 = tk.Button(self, textvariable=self.choice_9, font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=lambda: self.on_click_hard(self.game.choice[8]))


        target.grid(row=1, column=0, columnspan=5, pady=(40, 0))
        score.grid(row=1, column=3, pady=(40, 0), padx=(60, 0))
        choice_1.grid(row=2, column=1, pady=(60, 0))
        choice_2.grid(row=2, column=2, pady=(60, 0))
        choice_3.grid(row=2, column=3, pady=(60, 0))
        choice_4.grid(row=3, column=1, pady=(40, 0))
        choice_5.grid(row=3, column=2, pady=(40, 0))
        choice_6.grid(row=3, column=3, pady=(40, 0))
        choice_7.grid(row=4, column=1, pady=(40, 0))
        choice_8.grid(row=4, column=2, pady=(40, 0))
        choice_9.grid(row=4, column=3, pady=(40, 0))

    def finish_button(self):
        finish_button = tk.Button(self, text="Finish", font=("Helvetica", 20), relief="flat",
                                  width=10, height=2, command=self.finish_game)
        finish_button.grid(row=5, column=3, pady=(120, 0))

    def finish_game(self):
        self.clear_page()
        congratulation = tk.Label(self, text="CONGRATULATION!", font=("Helvetica", 30), borderwidth=5,
                         background="white", foreground="black", highlightthickness=2)
        you_got = tk.Label(self, text="You got", font=("Helvetica", 20), borderwidth=5,
                                  background="white", foreground="black", highlightthickness=2)
        self.score.set(f"Score : {self.game.score}")
        score = tk.Label(self, textvariable=self.score, font=("Helvetica", 20), borderwidth=3,
                         background="white", foreground="black", highlightthickness=2)
        next_button = tk.Button(self, text="Next", font=("Helvetica", 20), relief="flat",
                             width=10, height=2, command=self.main_menu)

        self.correct_percent.set(f"You play : {self.game.round} rounds\n"
                                 f"Correct : {self.game.correct}\n"
                                 f"Wrong : {self.game.wrong}\n"
                                 f"Correct percentage : {((self.game.correct/self.game.round)*100):.2f}%")

        correct_percentage = tk.Label(self, textvariable=self.correct_percent, font=("Helvetica", 20), borderwidth=3,
                         background="white", foreground="black", highlightthickness=2)

        image = Image.open("pictures/finish_anya.png")
        height = 450
        width = int(height * (9 / 16))
        image = image.resize((height, width))
        self.photo = ImageTk.PhotoImage(image)
        finish_anya = tk.Label(self, image=self.photo)

        congratulation.grid(row=1, column=0, columnspan=5, pady=(10, 0))
        finish_anya.grid(row=2, column=0, columnspan=5, pady=(10, 0))
        you_got.grid(row=3, column=0, columnspan=5, pady=(10, 0))
        score.grid(row=4, column=0, columnspan=5, pady=(10, 0))
        correct_percentage.grid(row=5, column=0, columnspan=5, pady=(10, 0))
        next_button.grid(row=6, column=4, pady=(0, 0))


if __name__ == "__main__":
    app = Application()
    app.mainloop()