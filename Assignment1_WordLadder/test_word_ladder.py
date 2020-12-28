import word_ladder
from word_ladder import UserInput
from word_ladder import UserRequire

import unittest 
from unittest import mock

class Test_Valid(unittest.TestCase):

############# Test valid_str ##################
  def test_InDict(self): # Test user inputs that are in the dictionary
    # Initialise
    list_words = ['aa', 'ab', 'nb', 'nhs', 'abc', 'aahed', 'aahing', 'aahs', 'aal', 'aalii', 'aaliis', 'aals', 'what', 'side', 'site', 'sits', 'sies', 'sees', 'seas', 'hell', 'look', 'load', 'goad', 'mine', 'lime', 'hide', 'hike', 'seek', 'lead', 'gold', 'bead', 'brad', 'bred', 'bree', 'dree', 'dreg', 'drag', 'drab', 'head', 'leaf', 'loaf', 'loof', 'woof', 'wood', 'wold', 'hide', 'aide', 'aids', 'yids', 'rids', 'rods', 'sods', 'suds', 'sudd', 'rudd', 'rued', 'ruer', 'suer', 'seer', 'soda', 'sods']
    user_input = UserInput(list_words)
    # ---------- test case -------------
    self.assertEqual(user_input.valid_str('gold'), True)
    self.assertEqual(user_input.valid_str('lead'), True)
    self.assertEqual(user_input.valid_str('side'), True)
    self.assertEqual(user_input.valid_str('aa'), True)
    self.assertEqual(user_input.valid_str('bead'), True)
    self.assertEqual(user_input.valid_str('ruer'), True)
    self.assertEqual(user_input.valid_str('aahing'), True)
    self.assertEqual(user_input.valid_str('aal'), True)
    self.assertEqual(user_input.valid_str('aaliis'), True)
    self.assertEqual(user_input.valid_str('what'), True)

  def test_NotInDict(self): # Test user inputs that are not in the dictionary
    # Initialise
    list_words = ['aa', 'ab', 'nb', 'nhs', 'abc', 'aahed', 'aahing', 'aahs', 'aal', 'aalii', 'aaliis', 'aals', 'what', 'side', 'site', 'sits', 'sies', 'sees', 'seas', 'hell', 'look', 'load', 'goad', 'mine', 'lime', 'hide', 'hike', 'seek', 'lead', 'gold', 'bead', 'brad', 'bred', 'bree', 'dree', 'dreg', 'drag', 'drab', 'head', 'leaf', 'loaf', 'loof', 'woof', 'wood', 'wold', 'hide', 'aide', 'aids', 'yids', 'rids', 'rods', 'sods', 'suds', 'sudd', 'rudd', 'rued', 'ruer', 'suer', 'seer', 'soda', 'sods']
    user_input = UserInput(list_words)
    # ---------- test case -------------
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('llakwdsaw')
    er = ve.exception
    self.assertEqual(str(er), "Sorry, this word is not in the dictonary file.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('HARi')
    er = ve.exception
    self.assertEqual(str(er), "Sorry, this word is not in the dictonary file.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('Makan')
    er = ve.exception
    self.assertEqual(str(er), "Sorry, this word is not in the dictonary file.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('MINUM')
    er = ve.exception
    self.assertEqual(str(er), "Sorry, this word is not in the dictonary file.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('balik')
    er = ve.exception
    self.assertEqual(str(er), "Sorry, this word is not in the dictonary file.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('tandas')
    er = ve.exception
    self.assertEqual(str(er), "Sorry, this word is not in the dictonary file.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('matahari')
    er = ve.exception
    self.assertEqual(str(er), "Sorry, this word is not in the dictonary file.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('bulan')
    er = ve.exception
    self.assertEqual(str(er), "Sorry, this word is not in the dictonary file.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('berak')
    er = ve.exception
    self.assertEqual(str(er), "Sorry, this word is not in the dictonary file.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('bunga')
    er = ve.exception
    self.assertEqual(str(er), "Sorry, this word is not in the dictonary file.")

  def test_type(self): # Test user input that are invalid.
    # Initialise
    list_words = ['aa', 'ab', 'nb', 'nhs', 'abc', 'aahed', 'aahing', 'aahs', 'aal', 'aalii', 'aaliis', 'aals', 'what', 'side', 'site', 'sits', 'sies', 'sees', 'seas', 'hell', 'look', 'load', 'goad', 'mine', 'lime', 'hide', 'hike', 'seek', 'lead', 'gold', 'bead', 'brad', 'bred', 'bree', 'dree', 'dreg', 'drag', 'drab', 'head', 'leaf', 'loaf', 'loof', 'woof', 'wood', 'wold', 'hide', 'aide', 'aids', 'yids', 'rids', 'rods', 'sods', 'suds', 'sudd', 'rudd', 'rued', 'ruer', 'suer', 'seer', 'soda', 'sods']
    user_input = UserInput(list_words)
    # ---------- test case -------------
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('651')
    er = ve.exception
    self.assertEqual(str(er), "Invalid word. The word must only conatin alphabetic letters.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('154.453')
    er = ve.exception
    self.assertEqual(str(er), "Invalid word. The word must only conatin alphabetic letters.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('lead123')
    er = ve.exception
    self.assertEqual(str(er), "Invalid word. The word must only conatin alphabetic letters.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('tandas, BULAN')
    er = ve.exception
    self.assertEqual(str(er), "Invalid word. The word must only conatin alphabetic letters.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('hide, seek')
    er = ve.exception
    self.assertEqual(str(er), "Invalid word. The word must only conatin alphabetic letters.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('G0@d')
    er = ve.exception
    self.assertEqual(str(er), "Invalid word. The word must only conatin alphabetic letters.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('!@#$%$^&*')
    er = ve.exception
    self.assertEqual(str(er), "Invalid word. The word must only conatin alphabetic letters.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('Goad: Lead')
    er = ve.exception
    self.assertEqual(str(er), "Invalid word. The word must only conatin alphabetic letters.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('what aahs')
    er = ve.exception
    self.assertEqual(str(er), "Invalid word. The word must only conatin alphabetic letters.")
    with self.assertRaises(ValueError) as ve:
      user_input.valid_str('li3d')
    er = ve.exception
    self.assertEqual(str(er), "Invalid word. The word must only conatin alphabetic letters.")

############# END Test valid_str ##################

# ------    ------    ------    ------    ------

############# Test start_word ##################
  # Test valid user input for start word, convert uppercase to lowercase
  def test_start_word(self):
    # Initialise
    list_words = ['aa', 'ab', 'nb', 'nhs', 'abc', 'aahed', 'aahing', 'aahs', 'aal', 'aalii', 'aaliis', 'aals', 'what', 'side', 'site', 'sits', 'sies', 'sees', 'seas', 'hell', 'look', 'load', 'goad', 'mine', 'lime', 'hide', 'hike', 'seek', 'lead', 'gold', 'bead', 'brad', 'bred', 'bree', 'dree', 'dreg', 'drag', 'drab', 'head', 'leaf', 'loaf', 'loof', 'woof', 'wood', 'wold', 'hide', 'aide', 'aids', 'yids', 'rids', 'rods', 'sods', 'suds', 'sudd', 'rudd', 'rued', 'ruer', 'suer', 'seer', 'soda', 'sods']
    user_input = UserInput(list_words)
    # ---------- test case -------------
    with mock.patch('builtins.input', lambda x: 'gold'):
      assert user_input.start_word() == 'gold'
    
    with mock.patch('builtins.input', lambda x: 'GOLD'):
      assert user_input.start_word() == 'gold'
    
    with mock.patch('builtins.input', lambda x: 'riDs'):
      assert user_input.start_word() == 'rids'

    with mock.patch('builtins.input', lambda x: 'lOad'):
      assert user_input.start_word() == 'load'

    with mock.patch('builtins.input', lambda x: 'aA'):
      assert user_input.start_word() == 'aa'

    with mock.patch('builtins.input', lambda x: 'aBC'):
      assert user_input.start_word() == 'abc'

    with mock.patch('builtins.input', lambda x: 'SitS'):
      assert user_input.start_word() == 'sits'

    with mock.patch('builtins.input', lambda x: 'sITe'):
      assert user_input.start_word() == 'site'

    with mock.patch('builtins.input', lambda x: 'Aal'):
      assert user_input.start_word() == 'aal'

    with mock.patch('builtins.input', lambda x: 'breD'):
      assert user_input.start_word() == 'bred'

  # Test not valid user input for start word
  def test_invalid_start_word(self):
    # Initialise
    list_words = ['aa', 'ab', 'nb', 'nhs', 'abc', 'aahed', 'aahing', 'aahs', 'aal', 'aalii', 'aaliis', 'aals', 'what', 'side', 'site', 'sits', 'sies', 'sees', 'seas', 'hell', 'look', 'load', 'goad', 'mine', 'lime', 'hide', 'hike', 'seek', 'lead', 'gold', 'bead', 'brad', 'bred', 'bree', 'dree', 'dreg', 'drag', 'drab', 'head', 'leaf', 'loaf', 'loof', 'woof', 'wood', 'wold', 'hide', 'aide', 'aids', 'yids', 'rids', 'rods', 'sods', 'suds', 'sudd', 'rudd', 'rued', 'ruer', 'suer', 'seer', 'soda', 'sods']
    user_input = UserInput(list_words)
    # ---------- test case -------------
    with mock.patch('builtins.input', lambda x: 'Hari'):
      with self.assertRaises(ValueError) as ve:
        user_input.start_word()
        er = ve.exception
        self.assertEqual(er, "Sorry, this word is not in the dictonary file.")

    with mock.patch('builtins.input', lambda x: 'BULAN'):
      with self.assertRaises(ValueError) as ve:
        user_input.start_word()
        er = ve.exception
        self.assertEqual(er, "Sorry, this word is not in the dictonary file.")

    with mock.patch('builtins.input', lambda x: 'baLik'):
      with self.assertRaises(ValueError) as ve:
        user_input.start_word()
        er = ve.exception
        self.assertEqual(er, "Sorry, this word is not in the dictonary file.")
        
    with mock.patch('builtins.input', lambda x: 'BeraK'):
      with self.assertRaises(ValueError) as ve:
        user_input.start_word()
        er = ve.exception
        self.assertEqual(er, "Sorry, this word is not in the dictonary file.")

    with mock.patch('builtins.input', lambda x: 'bUNGa'):
      with self.assertRaises(ValueError) as ve:
        user_input.start_word()
        er = ve.exception
        self.assertEqual(er, "Invalid word. The word must only conatin alphabetic letters.")

    with mock.patch('builtins.input', lambda x: '!@#$%$^&*'):
      with self.assertRaises(ValueError) as ve:
        user_input.start_word()
        er = ve.exception
        self.assertEqual(er, "Invalid word. The word must only conatin alphabetic letters.")

    with mock.patch('builtins.input', lambda x: 'G0@d'):
      with self.assertRaises(ValueError) as ve:
        user_input.start_word()
        er = ve.exception
        self.assertEqual(er, "Invalid word. The word must only conatin alphabetic letters.")

    with mock.patch('builtins.input', lambda x: 'Lead Gold'):
      with self.assertRaises(ValueError) as ve:
        user_input.start_word()
        er = ve.exception
        self.assertEqual(er, "Invalid word. The word must only conatin alphabetic letters.")

    with mock.patch('builtins.input', lambda x: 'What: GOLD'):
      with self.assertRaises(ValueError) as ve:
        user_input.start_word()
        er = ve.exception
        self.assertEqual(er, "Invalid word. The word must only conatin alphabetic letters.")

    with mock.patch('builtins.input', lambda x: 'hide, seek'):
      with self.assertRaises(ValueError) as ve:
        user_input.start_word()
        er = ve.exception
        self.assertEqual(er, "Invalid word. The word must only conatin alphabetic letters.")

############# END Test start_word ##################

# ------    ------    ------    ------    ------

############# Test target_word ##################
  def test_target_word(self):
    # Initialise
    list_words = ['aa', 'ab', 'nb', 'nhs', 'abc', 'aahed', 'aahing', 'aahs', 'aal', 'aalii', 'aaliis', 'aals', 'what', 'side', 'site', 'sits', 'sies', 'sees', 'seas', 'hell', 'look', 'load', 'goad', 'mine', 'lime', 'hide', 'hike', 'seek', 'lead', 'gold', 'bead', 'brad', 'bred', 'bree', 'dree', 'dreg', 'drag', 'drab', 'head', 'leaf', 'loaf', 'loof', 'woof', 'wood', 'wold', 'hide', 'aide', 'aids', 'yids', 'rids', 'rods', 'sods', 'suds', 'sudd', 'rudd', 'rued', 'ruer', 'suer', 'seer', 'soda', 'sods']
    user_input = UserInput(list_words)
    # test the length is equal
    # length equal, return the value
    with mock.patch('builtins.input', lambda x: 'gold'):
      assert user_input.target_word('lead') == 'gold'
    with mock.patch('builtins.input', lambda x: 'hide'):
      assert user_input.target_word('seek') == 'hide'
    with mock.patch('builtins.input', lambda x: 'abc'):
      assert user_input.target_word('AAL') == 'abc'
    with mock.patch('builtins.input', lambda x: 'what'):
      assert user_input.target_word('SidE') == 'what'
    with mock.patch('builtins.input', lambda x: 'site'):
      assert user_input.target_word('sIEs') == 'site'

  def test_len_target_word(self):
    # Initialise
    list_words = ['aa', 'ab', 'nb', 'nhs', 'abc', 'aahed', 'aahing', 'aahs', 'aal', 'aalii', 'aaliis', 'aals', 'what', 'side', 'site', 'sits', 'sies', 'sees', 'seas', 'hell', 'look', 'load', 'goad', 'mine', 'lime', 'hide', 'hike', 'seek', 'lead', 'gold', 'bead', 'brad', 'bred', 'bree', 'dree', 'dreg', 'drag', 'drab', 'head', 'leaf', 'loaf', 'loof', 'woof', 'wood', 'wold', 'hide', 'aide', 'aids', 'yids', 'rids', 'rods', 'sods', 'suds', 'sudd', 'rudd', 'rued', 'ruer', 'suer', 'seer', 'soda', 'sods']
    user_input = UserInput(list_words)
    # not equal, raise error
    with mock.patch('builtins.input', lambda x: 'lead'):
      with self.assertRaises(ValueError) as ve:
        user_input.target_word('aa')
      er = ve.exception
      self.assertEqual(str(er), "Please enter a word that has the same length as the first word")
    with mock.patch('builtins.input', lambda x: 'what'):
      with self.assertRaises(ValueError) as ve:
        user_input.target_word('aaL')
      er = ve.exception
      self.assertEqual(str(er), "Please enter a word that has the same length as the first word")
    with mock.patch('builtins.input', lambda x: 'sies'):
      with self.assertRaises(ValueError) as ve:
        user_input.target_word('AAHLIIS')
      er = ve.exception
      self.assertEqual(str(er), "Please enter a word that has the same length as the first word")
    with mock.patch('builtins.input', lambda x: 'abc'):
      with self.assertRaises(ValueError) as ve:
        user_input.target_word('gOad')
      er = ve.exception
      self.assertEqual(str(er), "Please enter a word that has the same length as the first word")
    with mock.patch('builtins.input', lambda x: 'aa'):
      with self.assertRaises(ValueError) as ve:
        user_input.target_word('aal')
      er = ve.exception
      self.assertEqual(str(er), "Please enter a word that has the same length as the first word")
    
############# END Test target_word ##################

# ------    ------    ------    ------    ------

############# Test list_words ##################
  # test return a list of word that has the same length as the input word
  def test_list_words(self): 
    # Initialise
    list_words = ['aa', 'ab', 'nb', 'nhs', 'abc', 'aahed', 'aahing', 'aahs', 'aal', 'aalii', 'aaliis', 'aals', 'what', 'side', 'site', 'sits', 'sies', 'sees', 'seas', 'hell', 'look', 'load', 'goad', 'mine', 'lime', 'hide', 'hike', 'seek', 'lead', 'gold', 'bead', 'brad', 'bred', 'bree', 'dree', 'dreg', 'drag', 'drab', 'head', 'leaf', 'loaf', 'loof', 'woof', 'wood', 'wold', 'hide', 'aide', 'aids', 'yids', 'rids', 'rods', 'sods', 'suds', 'sudd', 'rudd', 'rued', 'ruer', 'suer', 'seer', 'soda', 'sods']
    user_input = UserInput(list_words)
    # ---------- test case -------------
    self.assertEqual(user_input.list_words('aa'), ['aa', 'ab', 'nb'])
    self.assertEqual(user_input.list_words('nhs'), ['nhs', 'abc', 'aal'])
    self.assertEqual(user_input.list_words('aahed'), ['aahed', 'aalii'])
    self.assertEqual(user_input.list_words('aahing'), ['aahing', 'aaliis'])
    
############# END Test list_words ##################

# ------    ------    ------    ------    ------

############# Test unwant ##################
  # test if it returns a list of words or empty list according to user input
  def test_unwant(self): 
    # Initialise
    list_words = ['aa', 'ab', 'nb', 'nhs', 'abc', 'aahed', 'aahing', 'aahs', 'aal', 'aalii', 'aaliis', 'aals', 'what', 'side', 'site', 'sits', 'sies', 'sees', 'seas', 'hell', 'look', 'load', 'goad', 'mine', 'lime', 'hide', 'hike', 'seek', 'lead', 'gold', 'bead', 'brad', 'bred', 'bree', 'dree', 'dreg', 'drag', 'drab', 'head', 'leaf', 'loaf', 'loof', 'woof', 'wood', 'wold', 'hide', 'aide', 'aids', 'yids', 'rids', 'rods', 'sods', 'suds', 'sudd', 'rudd', 'rued', 'ruer', 'suer', 'seer', 'soda', 'sods']
    user_input = UserInput(list_words)
    # ---------- test case -------------
    with mock.patch('builtins.input', side_effect=['y', 'hello, world']):
      assert user_input.unwant() == ['hello', 'world']
    
    with mock.patch('builtins.input', side_effect=['Y', 'ciao no!']):
      assert user_input.unwant() == ['ciao', 'no']
    
    with mock.patch('builtins.input', side_effect=['y', '']):
      assert user_input.unwant() == []

    with mock.patch('builtins.input', side_effect=['y', 'you am']):
      assert user_input.unwant() == ['you', 'am']

    with mock.patch('builtins.input', side_effect=['y', 'lead']):
      assert user_input.unwant() == ['lead']

    with mock.patch('builtins.input', side_effect=['y', 'need game']):
      assert user_input.unwant() == ['need', 'game']

    with mock.patch('builtins.input', side_effect=['y', 'side seek154']):
      assert user_input.unwant() == ['side', 'seek154']

    with mock.patch('builtins.input', side_effect=['y', '1897']):
      assert user_input.unwant() == ['1897']

    with mock.patch('builtins.input', side_effect=['y', 'donut']):
      assert user_input.unwant() == ['donut']
    
    with mock.patch('builtins.input', lambda x: 'n'):
      assert user_input.unwant() == []

############# END Test unwant ##################

# ------    ------    ------    ------    ------

############# Test UserRequire ##################
  # Test if UserRequire class return the value when accessing its instance variable
  def test_user_require(self):
    user_req = UserRequire('hide', 'seek', ['bead', 'brad', 'bred', 'bree'], [])
    self.assertEqual(user_req.start, 'hide')
    self.assertEqual(user_req.target, 'seek')
    self.assertEqual(user_req.words, ['bead', 'brad', 'bred', 'bree'])
    self.assertEqual(user_req.unwant, [])
    
    user_req = UserRequire('lead', 'gold', ['lead', 'bead', 'dish', 'need'], ['bake'])
    self.assertEqual(user_req.start, 'lead')
    self.assertEqual(user_req.target, 'gold')
    self.assertEqual(user_req.words, ['lead', 'bead', 'dish', 'need'])
    self.assertEqual(user_req.unwant, ['bake'])

############# END Test UserRequire ##################

# ------    ------    ------    ------    ------

############# Test open_file ##################
  def test_open_file(self):
    # Test if the file has the correct file extension
    with mock.patch('builtins.input', lambda x: 'file.py'):
      with self.assertRaises(ValueError) as ve:
        word_ladder.open_file('file.py')
      er = ve.exception
      self.assertEqual(str(er), "File type not valid, please provide a txt file.")
    
    with mock.patch('builtins.input', lambda x: 'hello.pdf'):
      with self.assertRaises(ValueError) as ve:
        word_ladder.open_file('hello.pdf')
      er = ve.exception
      self.assertEqual(str(er), "File type not valid, please provide a txt file.")

    # Test if file can be open, read and return list of words
    with mock.patch('builtins.open', mock.mock_open (read_data='hello\nworld'),lambda x: ['hello', 'world']):
      result = word_ladder.open_file('sample.txt')
    assert result == ['hello', 'world']

    with mock.patch('builtins.open', mock.mock_open (read_data='meat\nfactory\nlive\nhead'),lambda x: ['meat', 'factory', 'live', 'head']):
      result = word_ladder.open_file('dictionary.txt')
    assert result == ['meat', 'factory', 'live', 'head']

    with mock.patch('builtins.open', mock.mock_open (read_data='oyster\nseafood\nlobster'),lambda x: ['oyster', 'seafood', 'lobster']):
      result = word_ladder.open_file('dictionary.txt')
    assert result == ['oyster', 'seafood', 'lobster']

############# END Test open_file ##################

# ------    ------    ------    ------    ------

############# Test word_path ##################
  # test if it can return a list of words that have the same length as word
  def test_word_path(self): 
    # Initialise
    word = 'lead'
    list_words = ['what', 'side', 'site', 'sits', 'sies', 'sees', 'seas', 'hell', 'look', 'load', 'goad', 'mine', 'lime', 'hide', 'hike', 'seek', 'gold', 'bead', 'brad', 'bred', 'bree', 'dree', 'dreg', 'drag', 'drab', 'head', 'leaf', 'loaf', 'loof', 'woof', 'wood', 'wold', 'hide', 'aide', 'aids', 'yids', 'rids', 'rods', 'sods', 'suds', 'sudd', 'rudd', 'rued', 'ruer', 'suer', 'seer', 'soda', 'sods']
    # ---------- test case -------------
    self.assertEqual(word_ladder.word_path(word, list_words, []), ['load', 'bead', 'head', 'leaf'])

    self.assertEqual(word_ladder.word_path(word, list_words, ['load']), ['bead', 'head', 'leaf'])
############# END Test word_path ##################

# ------    ------    ------    ------    ------

############# Test shortest_path ##################
  def test_shortest_path(self): # test if it can output correct result
    list_words = ['aals', 'what', 'side', 'site', 'sits', 'sies', 'sees', 'seas', 'hell', 'look', 'load', 'goad', 'mine', 'lime', 'hide', 'hike', 'seek', 'lead', 'gold', 'bead', 'brad', 'bred', 'bree', 'dree', 'dreg', 'drag', 'drab', 'head', 'leaf', 'loaf', 'loof', 'woof', 'wood', 'wold', 'hide', 'aide', 'aids', 'yids', 'rids', 'rods', 'sods', 'suds', 'sudd', 'rudd', 'rued', 'ruer', 'suer', 'seer', 'soda', 'sods']
    usr_req = UserRequire('lead', 'gold', list_words, [])

    self.assertEqual(word_ladder.shortest_path(usr_req), [3, ['lead', 'load', 'goad', 'gold']])
############# END Test shortest_path ##################

# ------    ------    ------    ------    ------

############## Test display_result ##################
  def test_display_result(self): # test if it can output correct result
    list_words = ['aals', 'what', 'side', 'site', 'sits', 'sies', 'sees', 'seas', 'hell', 'look', 'load', 'goad', 'mine', 'lime', 'hide', 'hike', 'seek', 'lead', 'gold', 'bead', 'brad', 'bred', 'bree', 'dree', 'dreg', 'drag', 'drab', 'head', 'leaf', 'loaf', 'loof', 'woof', 'wood', 'wold', 'hide', 'aide', 'aids', 'yids', 'rids', 'rods', 'sods', 'suds', 'sudd', 'rudd', 'rued', 'ruer', 'suer', 'seer', 'soda', 'sods']
    usr_req = UserRequire('lead', 'gold', list_words, [])

    self.assertEqual(word_ladder.display_result(usr_req), "It takes 3 steps to arrive from lead to gold. Path as follows:\nlead -> load -> goad -> gold")

############# END display_result ##################

#======================== END TEST =========================
if __name__ == '__main__':
  unittest.main()