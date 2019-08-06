class Win:

 # -------------------------------------------------------------------------
  # Constructor
  def __init__(self):
    self.__winner = ""
    self.__message = ""
    self.__counter = 0
  # --------------------------------------------------------------------------
  # Predicates
  def x_wins(self):
    return self.__winner == 'X'
  def o_wins(self):
    return self.__winner == 'O'
  def CAT(self):
    return self.__winner == 'No winner. CAT!'

  # --------------------------------------------------------------------------
  # Accessors
  def result(self):
    return self.winner
  def current_message(self):
    return self.__message

  # --------------------------------------------------------------------------
  # Mutators
  #decides if there is winner or not, incrememnts every time it is called
  def decider_winner(self, li, tester):
    if ((li[0] == tester and li[1] == tester and li[2] == tester) or
        (li[3] == tester and li[4] == tester and li[5] == tester) or 
        (li[6] == tester and li[7] == tester and li[8] == tester) or
        (li[0] == tester and li[3] == tester and li[6] == tester) or
        (li[1] == tester and li[4] == tester and li[7] == tester) or
        (li[2] == tester and li[5] == tester and li[8] == tester) or
        (li[0] == tester and li[4] == tester and li[8] == tester) or
        (li[6] == tester and li[4] == tester and li[2] == tester)):
      self.__winner = tester
    self.__counter_increment()
  # if game is over, message changes
  def decider_message(self):
    if self.__winner == 'X':
      self.__message = 'X has won the game!'
    elif self.__winner == 'O':
      self.__message = "O has won the game!"
    elif self.__counter == 9:
      self.__message = "No winner. CAT!"

  def __counter_increment(self):
    self.__counter += 1

  def reset_counter(self):
    self.__counter = 0

  def reset_message(self):
    self.__message = ""

  def reset_winner(self):
    self.__winner = ""

  # --------------------------------------------------------------------------
  # to_string()


  def __str__(self):

    return "%s" %(self.__winner) 
    
