"""
a docstring that i should fill out...
"""
#import this,antigravity
import sys,os,re,random



class Sweep(object):
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

      
      
   def print_board(self,bomb=False):
      """Prints the board to the console. If bomb is True, prints the bomb_field instead of the table"""
      if not bomb:
         toprint = self.table
      else:
         toprint = self.bomb_field
      
      for i in xrange(len(toprint)):
         for j in xrange(len(toprint)):
            print toprint[i][j],
         print
      return None
   
   def print_mines(self):
      """Just for convenience..."""
      self.print_board(bomb=True)
   
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
   
   def getpoint(self):
      xval = raw_input("x-val: ")
      yval = raw_input("y-val: ")
      try:
         xval = int(xval)
         yval = int(yval)
         return (xval,yval)
      except ValueError as e:
         if isinstance(xval,str):
            if xval.lower().startswith('q'):
               print "Quitting!"
               sys.exit("quit!")
         print e
   
      
   def adjbombs(self,x,y):
      count = 0
      for i in range(-1,2):
         nx = x + i
         for j in range(-1,2):
            ny = y + j
            if self.bomb_field[nx][ny] == -1: 
               count+=1
      return count
   
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
      
   
   
   def play(self,debug=True):
      self.print_board()
      print
      self.populate()
      if debug: self.print_mines
      x,y = self.getpoint()
      #FIXME: for some reason, below only works when inverted...HELP!
      while self.process(self.getpoint()):
         #TODO: fill this shit in
         pass
      else:
         #TODO: make an exit strategy for when you inevitably lose the game.
         pass
      
      
      
     
      
      
#End class Sweep

def main():
   #Should only have to do `game = Sweep();game.play()` will implement later.
   game = Sweep()
   game.print_board()
   print
   game.populate()
   game.print_mines()
   while True:
      x,y = game.getpoint()
      game.process(y,x) #for some reason it only works when inverted....wat

main()

raw_input('enter anything to exit')