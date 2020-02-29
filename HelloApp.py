# Author Lucas Maliszewski
# Date Feb 29 2020
# See course Python GUI Development with Tkinter
from random import randrange
from tkinter import *
from tkinter import ttk


class RollTheDice:

    def __init__(self, master):
        self.label = ttk.Label(master, text="Roll your die")
        self.label.grid(row=0, column=0, columnspan=2)

        ttk.Button(master, text="Roll 1D20",
                   command=self.roll_one_d_twenty).grid(row=1, column=0)
        ttk.Button(master, text="Roll 2D10",
                   command=self.roll_two_d_ten).grid(row=1, column=1)

    def roll_two_d_ten(self):
        _num_of_dice = 2
        _size = 10
        self.roll(_num_of_dice, _size)

    def roll_one_d_twenty(self):
        _num_of_dice = 1
        _size = 20
        self.roll(_num_of_dice, _size)

    def roll(self, num, size):
        _sum = 0
        while num > 0:
            _sum += randrange(1, size)
            num -= 1
        self.label.config(text="You've rolled {}".format(_sum))


def main():
    root = Tk()
    app = RollTheDice(root)
    root.mainloop()


if __name__ == "__main__": main()
