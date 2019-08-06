from tkinter import *
from Turn import *
from tkinter import messagebox
from Win import *
class tictactoeGUI:
  OUTPUT_X = 'X'
  OUTPUT_O = 'O'
  def __init__(self):
    #window and class objects
    self.__w = Tk()
    self.__turn = Turn()
    self.__win = Win()
    #creation of buttons
    self.b1 = Button(text = 'Empty', command = lambda:self.win_check(self.b1),
                     font = "Arial 14 bold", fg = 'white', bg= 'black',
                     width = 5, height = 3)
    self.b2 = Button(text = 'Empty', command = lambda:self.win_check(self.b2),
                     font = "Arial 14 bold", fg = 'white', bg= 'black',
                     width = 5, height = 3)
    self.b3 = Button(text = 'Empty', command = lambda:self.win_check(self.b3),
                     font = "Arial 14 bold", fg = 'white', bg= 'black',
                     width = 5, height = 3)
    self.b4 = Button(text = 'Empty', command = lambda:self.win_check(self.b4),
                     font = "Arial 14 bold", fg = 'white', bg= 'black',
                     width = 5, height = 3)
    self.b5 = Button(text = 'Empty', command = lambda:self.win_check(self.b5),
                     font = "Arial 14 bold", fg = 'white', bg= 'black',
                     width = 5, height = 3)
    self.b6 = Button(text = 'Empty', command = lambda:self.win_check(self.b6),
                     font = "Arial 14 bold", fg = 'white', bg= 'black',
                     width = 5, height = 3)
    self.b7 = Button(text = 'Empty', command = lambda:self.win_check(self.b7),
                     font = "Arial 14 bold", fg = 'white', bg= 'black',
                     width = 5, height = 3)
    self.b8 = Button(text = 'Empty', command = lambda:self.win_check(self.b8),
                     font = "Arial 14 bold", fg = 'white', bg= 'black',
                     width = 5, height = 3)
    self.b9 = Button(text = 'Empty', command = lambda:self.win_check(self.b9),
                     font = "Arial 14 bold", fg = 'white', bg= 'black',
                     width = 5, height = 3)
    self.breset = Button(text = 'Reset', font = "Arial 14 bold", fg = 'black',
                         bg = 'red', width = 5, height = 3,
                         command = self.__reset)
    self.help = Button(text = 'Help', font = 'Arial 14 bold', fg = 'black',
                       bg = 'yellow', width = 5, height = 3,
                       command = self.__helper)
    self.exit = Button(text = 'Exit', font = 'Arial 14 bold', fg = 'black',
                       bg = 'white', width = 5, height = 3,
                       command = self.quit)
    self.__button_list = [self.b1, self.b2, self.b3, self.b4,
                          self.b5, self.b6, self.b7, self.b8, self.b9]
    #grid to organize buttons
    self.b1.grid(row= 0, column = 0)
    self.b2.grid(row= 0, column = 1)
    self.b3.grid(row= 0, column = 2)
    self.b4.grid(row= 1, column = 0)
    self.b5.grid(row= 1, column = 1)
    self.b6.grid(row= 1, column = 2)
    self.b7.grid(row= 2, column = 0)
    self.b8.grid(row= 2, column = 1)
    self.b9.grid(row= 2, column = 2)
    self.breset.grid(row= 3, column = 1)
    self.help.grid(row= 3, column = 0)
    self.exit.grid(row= 3, column = 2)
    mainloop()
#----Event Handlers-------------------------------------------------------
  #resets buttons, and instances from other classes
  def __reset(self):
    self.__reset_buttons()
    self.__turn.reset()
    self.__win.reset_counter()
    self.__win.reset_message()
    self.__win.reset_winner()

  #checks for win every turn
  def win_check(self, button):
    if button['text'] == 'Empty':
      self.__player1_player2(button)
      list_button_text = self.__list_converter()
      self.__win.decider_winner(list_button_text,button['text'])
      self.__win.decider_message()
      if self.__win.current_message():
        messagebox.showinfo(message = self.__win.current_message())
        self.__stop_buttons()

  #displays how to play    
  def __helper(self):
    messagebox.showinfo(message = "Tic-Tac-Toe\nThis is a game in which"
                        " two players face off and attempt to have three"
                        " X's or O's in a row before the other player. The"
                        " person who does so first wins the game. Should "
                        " there be no winner, then the game is a CAT"
                        " (AKA a draw).\n"
                        "--How to use Buttons--\n"
                        "Reset: Reset the board at anytime\n"
                        "Exit: Exit the window at any time\n")
  #exits window                               
  def quit(self):
    self.__w.destroy()
                        
#----Private Class helpers------------------------------------------------
  #resets buttons
  def __reset_buttons(self):
    for button in self.__button_list:
      button['text'] = 'Empty'
      button['bg'] = 'black'
    self.b1['command'] = lambda:self.win_check(self.b1)
    self.b2['command'] = lambda:self.win_check(self.b2)
    self.b3['command'] = lambda:self.win_check(self.b3)
    self.b4['command'] = lambda:self.win_check(self.b4)
    self.b5['command'] = lambda:self.win_check(self.b5)
    self.b6['command'] = lambda:self.win_check(self.b6)
    self.b7['command'] = lambda:self.win_check(self.b7)
    self.b8['command'] = lambda:self.win_check(self.b8)
    self.b9['command'] = lambda:self.win_check(self.b9)
  #decides player turn
  def __player1_player2(self, box1):
    
    if box1['text'] == 'Empty' and self.__turn.get_turn_decider() == True:
      self.__turn.turn()
      box1['text'] = self.OUTPUT_X
      box1['bg'] = 'light blue'
    elif box1['text'] == 'Empty' and self.__turn.get_turn_decider() == False:
      self.__turn.turn()
      box1['text'] = self.OUTPUT_O
      box1['bg'] = 'green'

  #converts buttons texts to list
  def __list_converter(self):
    li = []
    for button in self.__button_list:
      li = li + [button['text']]
    return li

  #stops buttons from being clicked once game is over
  def __stop_buttons(self):
    for button in self.__button_list:
      button['command'] = lambda : messagebox.showinfo(message = "Press"
                                                       " Reset to start new"
                                                       " game. Or Exit")
      
    
   
tictactoeGUI()
