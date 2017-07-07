from tkinter import Tk, Label, Button, Entry, IntVar, StringVar, DISABLED, NORMAL, END, W, E, font, messagebox


class Game:
    def __init__(self, master):
        self.Board = Board(master)


class Board:
    def __init__(self, master):
        self.master = master
        master.title("Kółko i krzyżyk")

        self.player_o = "o"
        self.player_x = "x"
        self.current_player = ""
        self.testbut = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        self.przyciski = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.przyciski[i][j] = Button(master, height=6, width=12, text="",
                                              command=lambda i=i, j=j: self.xo(self.przyciski[i][j],
                                                                               self.current_player))
                self.przyciski[i][j].grid(row=i, column=j)

        self.reset_button = Button(master, text="RESET", width=24, height=2, command=lambda: self.reset())
        self.quit_button = Button(master, text="Wyjście", width=24, height=2, command=lambda: self.quit())

        self.reset_button.grid(row=3, column=0, columnspan=3)
        self.quit_button.grid(row=4, column=0, columnspan=3)

    def quit(self):
        self.master.quit()

    def reset(self):
        self.current_player = ""
        self.testbut = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for i in range(3):
            for j in range(3):
                self.przyciski[i][j].configure(text="")

    def xo(self, przycisk, *argv):
        print(przycisk)
        if przycisk["text"] == "":
            if self.current_player == self.player_o:
                self.current_player = self.player_x
            else:
                self.current_player = self.player_o
            przycisk.configure(text=self.current_player)
        test = str(przycisk)
        if test == ".!button":
            self.testbut[0] = self.current_player
        elif test == ".!button2":
            self.testbut[1] = self.current_player
        elif test == ".!button3":
            self.testbut[2] = self.current_player
        elif test == ".!button4":
            self.testbut[3] = self.current_player
        elif test == ".!button5":
            self.testbut[4] = self.current_player
        elif test == ".!button6":
            self.testbut[5] = self.current_player
        elif test == ".!button7":
            self.testbut[6] = self.current_player
        elif test == ".!button8":
            self.testbut[7] = self.current_player
        elif test == ".!button9":
            self.testbut[8] = self.current_player
        #print(self.testbut)
        self.check_victory()

    def check_victory(self):
        # print(self.testbut)
        if self.testbut[0] == self.testbut[1] == self.testbut[2]:
            print("vin")
            messagebox.showinfo("Wygrana", "Gratulacje!!! \nWygrał znak\n" + self.testbut[0])
        elif self.testbut[3] == self.testbut[4] == self.testbut[5]:
            print("vin")
            messagebox.showinfo("Wygrana", "Gratulacje!!! \nWygrał znak\n" + self.testbut[3])
        elif self.testbut[6] == self.testbut[7] == self.testbut[8]:
            print("vin")
            messagebox.showinfo("Wygrana", "Gratulacje!!! \nWygrał znak\n" + self.testbut[6])
        elif self.testbut[0] == self.testbut[3] == self.testbut[6]:
            print("vin")
            messagebox.showinfo("Wygrana", "Gratulacje!!! \nWygrał znak\n" + self.testbut[0])
        elif self.testbut[1] == self.testbut[4] == self.testbut[7]:
            print("vin")
            messagebox.showinfo("Wygrana", "Gratulacje!!! \nWygrał znak\n" + self.testbut[1])
        elif self.testbut[2] == self.testbut[5] == self.testbut[8]:
            print("vin")
            messagebox.showinfo("Wygrana", "Gratulacje!!! \nWygrał znak\n" + self.testbut[2])
        elif self.testbut[0] == self.testbut[4] == self.testbut[8]:
            print("vin")
            messagebox.showinfo("Wygrana", "Gratulacje!!! \nWygrał znak\n" + self.testbut[0])
        elif self.testbut[2] == self.testbut[4] == self.testbut[6]:
            print("vin")
            messagebox.showinfo("Wygrana", "Gratulacje!!! \nWygrał znak\n" + self.testbut[2])
        else:
            return False
