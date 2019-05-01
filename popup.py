from tkinter import *
from tkinter import messagebox


class PlayerPopUP:
  def __init__(self):
    self.__main_window = Tk()
    self.__main_window.title("What is Player 1's Name?")
    self.__top = Frame(self.__main_window)
    self.__bottom = Frame(self.__main_window)
    
#frames created above
    
    self.__prompt_label = Label(self.__top,\
                                text="Please enter Player 1's name:")
    self.__player_name = Entry(self.__top, width=10)
    #self.__player_name.bind(
    self.__prompt_label.pack(side='left')
    self.__player_name.pack(side='left')

#labels + prompt created and packed

    self.__play_button = Button(self.__bottom, \
                                text="Begin Tic Tac Toe",\
                                command=self.play)
    self.__play_button.pack(side='left')

    self.__top.pack()
    self.__bottom.pack()
    self.__main_window.mainloop()

    

#play button, frames created and packed
    
    #self.__main_window.mainloop()
#PlayerPopUP()

#Event handler: command to start game
  def play(self):
    Player1 = self.__player_name.get()
    self.__main_window.destroy()
    import Triple_T_new
    Triple_T_new.Triple_Tgame(Player1)
   
    import Triple_T
    KeepScore(Player1+" ",value)
    
    
    
PlayerPopUP() 
