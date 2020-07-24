import json
import random
import tkinter
import tkinter.messagebox

class Hangman():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Hangman")
        self.window.geometry("650x600")
        self.window.config(bg="Black")

        with open("words.json", "rb") as w:
            self.words = json.load(w)["data"]

        self.letters = {}

        self.MainMenu()

        self.window.mainloop()

    def letterPressed(self, letter):
        self.letters[letter].destroy()

        if letter in self.word:
            self.found_letters.append(letter)
            word = []

            for index in range(len(self.word)):
                if self.word[index] == letter or self.word[index] in self.found_letters:
                    word.append(self.word[index])
                else:
                    word.append("_")

            self.blanks.set(" ".join(word))

        else:
            self.stateLabel.destroy()
            self.hangman_state = [self.hangman_state[0] + 1, tkinter.PhotoImage(file=f"forms\\{str(self.hangman_state[0] + 1)}.png")]
            self.stateLabel = tkinter.Label(self.window, image=self.hangman_state[1], bg="Black")
            self.stateLabel.place(x=0, y=370)

        if self.hangman_state[0] == 6:
            tkinter.messagebox.showerror("Game Over", f"You Lost!\nThe Word Was: {self.word}")
            self.MainMenu()

        won = True
        for lett in self.word:
            if lett not in self.found_letters:
                won = False
                break

        if won:
            tkinter.messagebox.showinfo("Game Over", "You Won!")
            self.MainMenu()

    def resetWindow(self):
        for child in self.window.winfo_children():
            child.destroy()

    def startedGame(self):
        self.resetWindow()
        self.blanks = tkinter.StringVar()
        self.blanks.set("_ " * len(self.word))
        tkinter.Label(self.window, textvariable=self.blanks, font=("Heveltica", 30), bg="Black", fg="White").pack(side=tkinter.LEFT)
        self.stateLabel = tkinter.Label(self.window, image=self.hangman_state[1], bg="Black")
        self.stateLabel.place(x=0, y=370)

        for letter in range(ord("A"), ord("Z")+1):
            if ((letter - ord("A")) + 1) <= 13:
                self.letters[chr(letter)] = tkinter.Button(self.window, text=chr(letter), font=("Heveltica", 18), command=lambda letter=letter:self.letterPressed(chr(letter)), bg="White")
                self.letters[chr(letter)].place(x=(50 * (letter - ord("A"))), y=10)
            else:
                self.letters[chr(letter)] = tkinter.Button(self.window, text=chr(letter), font=("Heveltica", 18), command=lambda letter=letter:self.letterPressed(chr(letter)), bg="White")
                self.letters[chr(letter)].place(x=(50 * (letter - ord("N"))), y=70)

    def MainMenu(self):
        self.resetWindow()

        self.word = random.choice(self.words).upper()
        self.found_letters = []
        self.hangman_state = [0, tkinter.PhotoImage(file="forms\\0.png")]
        self.window.grid_columnconfigure((0,(len(self.word) - 1)), weight=1)

        tkinter.Label(self.window, text="Hang Man\nMain Menu", font=('Copperplate Gothic Bold', 60, 'bold', "underline"), bg="Black", fg="Gold").pack(fill=tkinter.X, side=tkinter.TOP)
        tkinter.Button(self.window, text="Start", font=('Copperplate Gothic Bold', 60, 'bold'), fg="Red", bg="Black", borderwidth=10, command=self.startedGame).pack(fill=tkinter.X, side=tkinter.BOTTOM)

Hangman()
