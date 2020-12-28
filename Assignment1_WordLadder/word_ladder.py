from string import punctuation

#============================================================
#                           CLASS
#============================================================
# Class list:
# UserInput
# UserRequire

#-------------------------UserInput--------------------------
# Description: it has multiple methods to check if user input is valid and return the valid values.
# Constructor: Takes a list of string from the file as input, and returns a value depending on which function called.
# Methods:
# valid_str, start_word, target_word, list_words, unwant
#------------------------------------------------------------
class UserInput():

  def __init__(self, lines : [str]):
    self.lines = lines

  #-------------------------valid_str()--------------------------
  # Description:
  # valid_str, to check if the string user provides is valid or not.
  # **** Sample input output ****
  # input -> output
  # h12 -> ValueError
  # hello -> if in dic, return hello, else return ValueError
  #-------------------------------------------------------------
  def valid_str(self, word:str) -> str:
    """
      Check if the string user provides is valid or not.
      - the word should only contain alphabetic characters
      - the word should be in the dictionary file user-provided
      if the word is valid, returns True
      if the word is invalid, raise a ValueError message
    """
    # check if the word only contain alphabetic characters
    if word.isalpha():
      # check if the word is in self.lines which is a list of words from the dictionary file
      if word in self.lines:
        return True
      else:
        raise ValueError("Sorry, this word is not in the dictonary file.")
    else:
      raise ValueError("Invalid word. The word must only conatin alphabetic letters.")
  #-------------------------END valid_str()-----------------------

  # ------      -------       --------        --------

  #-------------------------start_word()--------------------------
  # Description:
  # Ask the user to enter a word, and use valid_str() to check if that word is valid, then returns the word
  # **** Sample input output ****
  # input : 'hide'
  # output: 'hide'
  #--------------------------------------------------------------
  def start_word(self) -> str:
    """
    Takes user input, and check if it is valid.
    Returns user input value if it is valid, else return ValueError
    """
    user_input: str = input("Please enter a Start word: ").lower()
    output = self.valid_str(user_input) # Check if the word is valid
    if output == True:
      return user_input
    else:
      return output
  #-------------------------END start_word()-----------------------

  # ------      -------       --------        --------

  #-------------------------target_word()--------------------------
  # Description:
  # Ask the user to enter a word, and use valid_str() to check if that word is valid, then returns the word
  # **** Sample input output ****
  # input : 'seek'
  # output: 'seek'
  #----------------------------------------------------------------
  def target_word(self, start:str) -> str:
    """
    Take start word as an argument to check if the input word has the same length as start word.
    Returns user input value if it is valid, else raise ValueError.
    """
    user_input: str = input("Please enter a Target word: ").lower()
    output = self.valid_str(user_input) # Check if the word is valid
    if output != True:
      return output
    if len(start) == len(user_input):
      return user_input
    else:
      raise ValueError("Please enter a word that has the same length as the first word")
  #-------------------------END target_word()--------------------------

  # ------      -------       --------        --------

  #-------------------------list_words()-------------------------------
  # Description:
  # Check if the words in the dictionary have the same length as start word.
  # If True, returns a list of words that have the same length.
  ## **** Sample input output ****
  # input: 'aa'
  # ouput: ['aa', 'ab']
  #---------------------------------------------------------------------
  def list_words(self, start : str) -> [str]:
    """
      Check if the words in the dictionary have the same length as start word.
      If True, returns a list of words that have the same length.
    """
    words: [str] = [word for word in self.lines if len(word) == len(start)]
    return words

  #-------------------------END list_words()----------------------------

  # ------      -------       --------        --------

  #-------------------------unwant()------------------------------------
  # Description:
  # Asks the user if they want to provide a list of words that are not to be included in the steps.
  # input: 'hw,hlk'
  # output: ['hw', 'hlk'] 
  #----------------------------------------------------------------
  def unwant(self): # unwant word or not allowed word
    """
      Asks the user if they want to provide a list of words that are not to be included in the steps.
      If the user chose yes, then ask to input words separated by space, and return a list of words.
      else return an empty list
    """
    # Put other requirement line in the input is for display purpose, so when doing unit test will not appear -----other requirement--- line, but when running the main program will show the line.
    optional: str = input("--------------------------Other requirement----------------------------\nWould you like to have words that are not included? Y/n: ") 
    if optional in 'Yy':
      user_input: str = input("Please enter word/s separeted by space: ")
      table = str.maketrans("","",punctuation)
      if user_input == "": # if the user chose y and input nothing, then return []
        return []
      else:
        result = user_input.translate(table).split(' ') # remove punctuation, split by space
        return result
    else:
      return []
  #-------------------------END unwant()--------------------------

#==========================END UserInput class===========================

#-------------------------UserRequire--------------------------
# Constructor : Take start, target, words, unwant, path_req
# Create a class object of user requirement, for other function to access the instance variables
#-------------------------------------------------------------
class UserRequire:
  def __init__(self, start, target, words, unwant, ):
    self.start = start
    self.target = target
    self.words = words
    self.unwant = unwant
#==========================END UserRequire class===========================

# ========      ==========       ===========        ==========

#==========================================================================
#                               FUNCTIONS
#==========================================================================
# Function Lists:
# open_file()
# word_path()
# shortest_path()
# display_result()

#--------------------------open_file()-------------------------
# Function that opens the input file and returns a list of words
# **** Sample input output ****
# input: sample.txt
# output: ['aa', 'ab', 'abc', 'what']
#----------------------------------------------------------------
def open_file(fileName : str) -> [str]:
  """
  Check if the user input file ends with .txt, if not raise ValueError
  Open a txt file, and process the file into a list of words.
  """
  if fileName.endswith('.txt'):
    with open(fileName) as f:
      list_words = f.readlines()
    return [word.strip() for word in list_words]
  else:
    raise ValueError("File type not valid, please provide a txt file.")
#-----------------------End open_file()------------------------

#             -----        ------          ------

#-----------------------word_path()----------------------------
# Function description:
# take a word and list of words as the argument, return a list of words that only have one letter difference to the word.
# If none, return an empty list
# **** Sample input output ****
# input: 'hide', ['side', 'site', 'sits', 'sies', 'sees', 'hell', 'look', 'load', 'goad', 'mine', 'lime', 'lide']
# output: ['side', lide']
#----------------------------------------------------------------
def word_path(word : str, list_words : [str] , checked : [str] = []) -> [str]:
  """
  Take a word and list of words as the argument, find and return a list of words that only have one letter difference to the word.
  If none, return an empty list
  """
  childrens: [str] = []
  count: int = 0
  for crt_wd in list_words: # crt_wd >>> current word
    if crt_wd not in checked:
      for (lt_fw, lt_sw) in zip(word, crt_wd): # lt_fw, lt_sw >>> letter of first word, letter of second word
        if lt_fw != lt_sw:
          count += 1
      if count == 1:
        childrens.append(crt_wd)
        count = 0
      else:
        count = 0
  return childrens

#-----------------------END word_path()----------------------------

#             -----        ------          ------

#-----------------------shortest_path()----------------------------
# Function description:
# take one class object, and return the length of the possible path and path to reach target word from start. 
# **** Sample input output ****
# output: [6, ['hide', 'bide', 'bids', 'beds', 'bees', 'sees', 'seek']]
#-------------------------------------------------------------------
def shortest_path(usr_req) -> [int, [str]]:
  """
  shortestpath() takes 1 class obj as the argument and return a list contains the length of the possible path and path to reach target word from the start word.
  """
  # Initialise
  start: str = usr_req.start
  target: str = usr_req.target
  list_words: [str] = usr_req.words
  not_allow: [str] = usr_req.unwant

  # Remove the unwantted word from list_words
  if not_allow != []:
    for word in not_allow:
      if word in list_words:
        list_words.remove(word)

  # Set up default value / starting value
  # to store the all the children of the word with its level
  # int -> level of str
  queue: [[str, int]] = [[start, 1]] 
  
  # to store the parent and children
  # int -> level of children
  # str -> parent word
  # [str] -> children of parent
  parent: [[int, str, [str]]] = [[1, [start]]] 
  
  while queue:
    crt_word, level = queue.pop(0) # current word and the level of the current word out of the queue
    children: [str] = word_path(crt_word, list_words) # find children of current word

    #---------------------------------
    # if the target in children of the current word, find out the path and return [path_len:int, path: [str]]
    if target in children:

      # find a path by going through parent list backwards to find a path arrive to start word.
      path: [str] = [target, crt_word]
      while crt_word != start:
        # structure of parent list [children's level, parent, children]
        for item in parent[1:]: # parent[1:] not include [1, [start]], start with [[2, start, [....], ..]
          if item[0] == level: # if the children's level is equal to the current level
            if crt_word in item[2]: # if the current word is in any word's children in that level
              path.append(item[1]) # True, then append parent
              crt_word = item[1] # update current word to parent, now to search parent's parent
              level -= 1 # update level, go backward so -= 1
      path.reverse()

      # update length of the path, since begins with start word(lv1), and
      # included target word(e.g.lv7), need to -= 1
      return [len(path) - 1, path]
    #---------------------------------

    # Update the queue and parent, also remove all the children from list_words prevent repeating
    if children != []:
      queue += [[word, level + 1] for word in children]
      parent.append([level + 1, crt_word, children])
      for item in children:
        list_words.remove(item)

  # ----End while loop---

  # The queue is empty, and there is no path
  return None

#-----------------------End shortestpath()----------------------------

#             -----        ------          ------

#-----------------------display_result()----------------------------
# Function description:
# take one class object, call shortest_path() with the class object and return a formatted result depend on user requirement
# **** Sample output ****
# Output:
# -->if result found:
# It takes 6 steps to arrive from hide to seek. Path as follows:
# hide -> bide -> bids -> beds -> bees -> sees -> seek
# -->if no result found:
# No path from take to talk
#-------------------------------------------------------------------

def display_result(user_rq) -> str:
  """
  Take one class object, call shortest_path() with the class object and return a formatted result depend on user requirement.
  """
  result = shortest_path(user_rq) # find out the path

  start: str = user_rq.start
  target: str = user_rq.target

  # format result
  if result != None:
    result: str = "It takes {} steps to arrive from {} to {}. Path as follows:\n{}" .format(result[0], start, target, ' -> '.join(result[1]))
    print("\n==========================Result==============================\n")
    return result
  else:
    result: str = "Sorry, no path from from {} to {}" .format(start, target)
    print("\n==========================Result==============================\n")
    return result
#-----------------------End display_result()----------------------------

#***************************************************************
#                       Calling functions
#                         Start program
#---------------------------------------------------------------

def main():
  print("\n")
  user_in = UserInput(open_file(input("Dictionary file: ")))
  start: str = user_in.start_word()
  user_rq = UserRequire(start, user_in.target_word(start), user_in.list_words(start), user_in.unwant())
  print(display_result(user_rq))

if __name__ == '__main__': # if __name__ of curent file is __main__ then run main()
  main()

##################################################################
#                       End Program
##################################################################