
class Display:

  def __init__(self):
    #Turn into list 
    self.box0 = [" "]
    self.box1 = [" "]
    self.box2 = [" "]
    self.box3 = [" "]
    self.box4 = [" "]
    self.box5 = [" "]
    self.box6 = [" "]
    self.box7 = [" "]
    self.box8 = [" "]
    self.list_box = self.box0 + self.box1 + self.box2 + self.box3 + self.box4 + \
                  self.box5 + self.box5 + self.box7 + self.box8
  #Shows a display of the game board 
  def game_board(self,list_players):
    print("%s | %s | %s" % (list_players[0], list_players[1], list_players[2]))
    print("-----------")
    print("%s | %s | %s" % (list_players[3], list_players[4], list_players[5]))
    print("-----------")
    print("%s | %s | %s" % (list_players[6], list_players[7], list_players[8]))

    
  #Updates the display of where the x or o goes 

  def place_x_o(self,list_letter,box_number,letter):
    if box_number == 1:
      list_letter[0] = letter
    elif box_number == 2:
      list_letter[1] = letter
    elif box_number == 3:
      list_letter[2] = letter
    elif box_number == 4:
      list_letter[3] = letter
    elif box_number == 5:
      list_letter[4] = letter
    elif box_number == 6:
      list_letter[5] = letter
    elif box_number == 7:
      list_letter[6] = letter
    elif box_number == 8:
      list_letter[7] = letter
    elif box_number == 9:
      list_letter[8] = letter
