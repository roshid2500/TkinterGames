
from Turn import *
from Win import *
from Display import Display
INDEX = 1
MIN_INDEX = 0
MAX_INDEX = 9



class tictactoeCommand:

  
  

  def __init__(self):
    
    #Model
    #Display class
    self.__board = Display()
    #Turn class
    self.__turn = Turn()
    #Win class
    self.__win = Win()
    #list of boxes on board
    self.list_frames = [" "," "," "," "," "," "," "," "," "]
    #Describes basic rules of tic tac toe game 
    rules = print("This is tictactoe! Get three X's or O's in a row,"
                       " column, or diaganol to win! Enter in a number 1-9"
                       " to place your X or O. Enter 1 for row one, column"
                       " 1, Enter 2 for row one, column 2, and so on!")

    #Ask user whether they want to play or not 
    decision = decision = input("Enter 'play' to start. Or anything else to exit: ")
    while decision == 'play':
      #Displays board that players play on 
      self.display_screen(self.list_frames)

      #Ask player 1 to input where they want to place their x 
      x_placement = int(input("What box would you like your X in? "))

      #Validates that player entered valid value 
      while not self.__is_valid_placement(x_placement):
        print("Invalid Value Pick something in range 1-9 inclusive")
        self.display_screen(self.list_frames)
        x_placement = int(input("What box would you like your X in? "))

      #Places X based on value given 
      self.place_player(self.list_frames,x_placement,'X')
      #Checks to see if X has won the game 
      self.player_win(self.list_frames,'X')

      
      #Updates screen display 
      self.display_screen(self.list_frames)

      #If X has not won then ask player two(o) for their placement 
      if self.__win.current_message() != 'X has won the game!':
        o_placement = int(input("What box would you like your O in? "))
      #Validates range 
      while not self.__is_valid_placement(o_placement):
        print("Invalid Value pick something in range 1-9 inclusive")
        self.display_screen(self.list_frames)
        o_placement = int(input("What box would you like your O in"))

      #Places O where user inputted          
      self.place_player(self.list_frames,o_placement,'O') 
    
        
                        
        
  
      #Checks to see if player O won 
      self.player_win(self.list_frames,'O')

      #Updates current winner 
      self.__win.current_message()


      #If there is no winner continue the loop
      if self.__win.current_message() == '':
        continue
      
      else:
        decision = input("Would you like to play again? Type Y to continue or \
                            #Enter to quit: ").upper()
        if decision == 'Y':
          self.reset_board()
          self.__win.reset_message()
          tictactoeCommand()
  


    
                     
      


  #Events
      
  
  #If the box is empty then the player can put an X or O
  #If the box is not empty user will get an error message which will
  #allow them to play again
  def place_player(self, list_frames, player_placement,player):
    if list_frames[player_placement-INDEX] == " ":
      self.__board.place_x_o(list_frames,player_placement,player)
    else:
      if self.__win.current_message() == '':
        placement = int(input("Box taken! Try another value: "))
        self.place_player(self.list_frames,placement,player)
        
  
  def reset_board(self):
    self.list_frames = [" "," "," "," "," "," "," "," "," "]
    self.__win.reset_winner()
    self.__win.reset_counter()
    
  #Checks to see if X or O won
  def player_win(self,list_buttons,letter):
    self.__win.decider_winner(list_buttons,letter)
    self.__win.decider_message()
    if self.__win.current_message():
      print(self.__win.current_message())
      #self.display_screen(self.list_frames)
 


 
  #Displays board using display class   
  def display_screen(self,list_box):
    self.__board.game_board(list_box)
    
  #Private helper
  #Makes sure number given is 1-9 inclusive 
  def __is_valid_placement(self,num):
    return (int(num) > MIN_INDEX and int(num) <= MAX_INDEX) 
  #Describes game
  def game_description():
    print("This is a command line version of the game tic-tac-toe")
  





      
    


    
#Ask user which version of tic tac toe they want to play 
which_version = input("Which version of tic \
tac toe do you want to play? Enter GUI or command: ")
if which_version == 'GUI':
  from GUIclass import tictactoeGUI
elif which_version == 'command':
  tictactoeCommand.game_description()
  tictactoeCommand()

