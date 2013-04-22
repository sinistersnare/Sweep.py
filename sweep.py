#!usr/bin/python 
"""
a docstring that i should fill out...
i want this to be very terse with information, so i will fill this out...later...

works with python 2.7. Requires: swag
"""
#import this,antigravity
import sys,os,re,random



class Sweep(object):
   """This is the game object to be used."""
   def __init__(self,board_length=10,num_bombs=10):
      """Initializes the board."""
      self.board_len = board_length
      self.num_bombs = num_bombs
      self.char = '*'
      
      self.table = \
         [[self.char for i in xrange(self.board_len)] \
            for j in xrange(self.board_len)]
         
      self.bomb_field = \
      [[0 for i in xrange(self.board_len)] \
         for j in xrange(self.board_len)]
            
      return None
   #
   def print_board(self,bomb=False):
      """Prints the board to the console. If bomb is True, prints the bomb_field instead of the table"""
      if not bomb:
         toprint = self.table
      else:
         toprint = self.bomb_field
      
      for i in xrange(len(toprint)):
         for j in xrange(len(toprint)):
            print toprint[j][i],
         print
      return None
   #
   def print_mines(self):
      """Just for convenience..."""
      self.print_board(bomb=True)
      
      return None
   #
   def populate(self):
      """Populates the mine field with the number of bombs """
      i = 0
      while i < self.num_bombs:
         x = random.randint(0,self.num_bombs-1)
         y = random.randint(0,self.num_bombs-1)
         if self.bomb_field[x][y] != -1:
            self.bomb_field[x][y] = -1
            i += 1
         else:
            pass
      return None
   #
   def getpoint(self):
      xval = raw_input("x-val: ")
      yval = raw_input("y-val: ")
      try:
         xval = int(xval)
         yval = int(yval)
         return (xval,yval)
      except ValueError as e:
         #do this better later. just say "invalid, and continue..."
         print "Quitting!"
         sys.exit("quit!")
         print e
      return None
   #

   def adjbombs(self,x,y):
      """Returns the number of adjacent bombs to a specified point."""
      count = 0
      for i in range(-1,2):
         nx = x + i
         for j in range(-1,2):
            ny = y + j
            if self.bomb_field[nx][ny] == -1: 
               count+=1
      return count
   #
   def process(self,x,y):
      """Processes the point given."""
      
      if (0 <= x < self.board_len) and (0 <= y < self.board_len): #valid point
         if self.bomb_field[x][y] == -1:
            print "YOU DIE MOTHERFUCKER"
            self.table[x][y] = 'X'
         else:
            print "lived...for now"
            self.table[x][y] = self.adjbombs(x,y)
      else:
         print "not a valid point!"
      
      self.print_board()
      return None
   #
   def play(self,debug=True):
      """this is the main game loop."""
      self.print_board()
      print
      self.populate()
      if debug: self.print_mines
      x,y = self.getpoint()
      while self.process(self.getpoint()):
         #TODO: fill this shit in
         pass
      else:
         #TODO: make an exit strategy for when you inevitably lose the game.
         pass
      
      
      Return None
   #  

#End class Sweep

def main():
   """Will be the below comment eventually..."""
   #Should only have to do `game = Sweep();game.play()` will implement later.
   game = Sweep()
   game.print_board()
   print
   game.populate()
   game.print_mines()
   while True:
      x,y = game.getpoint()
      game.process(x,y) 
   return None
   #
   
   
   
if "__name__" == "__main__":
   main()

raw_input('enter anything to exit')