class Turn:
  # -------------------------------------------------------------------------
  # Constructor
  def __init__(self):
    self.__turn_decider = True

  # --------------------------------------------------------------------------
  # Predicates
 
  # --------------------------------------------------------------------------
  # Accessors
  def get_turn_decider(self):
    return self.__turn_decider
  

  # --------------------------------------------------------------------------
  # Mutators
  #every turn, true becomes false or false becomes true
  #switching player turns 
  def turn(self):
  
    if self.__turn_decider == True:
      self.__turn_decider = False
    elif self.__turn_decider == False:
      self.__turn_decider = True

  def reset(self):
    self.__turn_decider = True



  # --------------------------------------------------------------------------
  # to_string()

  #returns string of instances 
  def __str__(self):
    if self.__turn_deicder == True:
      boolean_string = "True"
    else:
      boolean_string = "False"

    return "%s" %(boolean_string)
