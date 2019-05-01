from tkinter import *
from tkinter import messagebox
#import popup

class Triple_Tgame:
  def __init__(self):
    self.__main_window = Tk()
   # self.__main_window.title(self.__player_name+"'s Game")
    self.__main_window.geometry("400x300")
    self.__bottom_frame = Frame(self.__main_window)
    self.__title = Label(self.__main_window, text="Tic-Tac-Toe Game",\
                         font=('Marker Felt', '25'))
    self.__title.grid(row=0, column=0)

    self.__button1 = Button(self.__main_window, \
                            text=" ", highlightbackground='light blue',\
                            fg = "dark red", \
                            width = 4, \
                            height = 2, \
                            font=('Market Felt', '20'),\
                            command=self.x_for_b1)
    self.__button1.grid(column=1, row=1)
    self.__button2 = Button(self.__main_window, \
                            text=" ", highlightbackground='light blue',\
                            fg = "dark red", \
                            width = 4, \
                            height = 2, \
                            font=('Market Felt', '20'),\
                             command=self.x_for_b2)
    self.__button2.grid(column=2, row=1)
    self.__button3 = Button(self.__main_window, \
                            text=" ", highlightbackground='light blue',\
                            fg = "dark red", \
                            width = 4, \
                            height = 2, \
                            font=('Market Felt', '20'),\
                             command=self.x_for_b3)
    self.__button3.grid(column=3, row=1)
    self.__button4 = Button(self.__main_window, \
                            text=" ", highlightbackground='light blue',\
                            fg = "dark red", \
                            width = 4, \
                            height = 2, \
                            font=('Market Felt', '20'),\
                             command=self.x_for_b4)
    self.__button4.grid(column=1, row=2)
    self.__button5 = Button(self.__main_window, \
                            text=" ", highlightbackground='light blue',\
                            fg = "dark red", \
                            width = 4, \
                            height = 2, \
                            font=('Market Felt', '20'),\
                             command=self.x_for_b5)
    self.__button5.grid(column=2, row=2)
    self.__button6 = Button(self.__main_window, \
                            text=" ", highlightbackground='light blue',\
                            fg = "dark red", \
                            width = 4, \
                            height = 2, \
                            font=('Market Felt', '20'),\
                             command=self.x_for_b6)
    self.__button6.grid(column=3, row=2)
    self.__button7 = Button(self.__main_window, \
                            text=" ", highlightbackground='light blue',\
                            fg = "dark red", \
                            width = 4, \
                            height = 2, \
                            font=('Market Felt', '20'),\
                             command=self.x_for_b7)
    self.__button7.grid(column=1, row=3)
    self.__button8 = Button(self.__main_window, \
                            text=" ", highlightbackground='light blue',\
                            fg = "dark red", \
                            width = 4, \
                            height = 2, \
                            font=('Market Felt', '20'),\
                             command=self.x_for_b8)
    self.__button8.grid(column=2, row=3)
    self.__button9 = Button(self.__main_window, \
                            text=" ", highlightbackground='light blue',\
                            fg = "dark red", \
                            width = 4, \
                            height = 2, \
                            font=('Market Felt', '20'),\
                             command=self.x_for_b9)
    self.__button9.grid(column=3, row=3)

    
    self.__main_window.mainloop()

  def x_for_b1(self):
    self.__button1.config(text="X")
  def x_for_b2(self):
    self.__button2.config(text="X")
  def x_for_b3(self):
    self.__button3.config(text="X")
  def x_for_b4(self):
    self.__button4.config(text="X")
  def x_for_b5(self):
    self.__button5.config(text="X")
  def x_for_b6(self):
    self.__button6.config(text="X")
  def x_for_b7(self):
    self.__button7.config(text="X")
  def x_for_b8(self):
    self.__button8.config(text="X")
  def x_for_b9(self):
    self.__button9.config(text="X")

Triple_Tgame()

class KeepScore:
  def __init__(self):
    #FIX self.__score_board = Button(self.__bottom_frame)
    self.__score = 0

  def get_score(self):
    return self.__score
  
  def increment(self):
    self.__score += 1

  def __str__(self):
    return "Player1 wins: %d" % (self.__score)

KeepScore()
