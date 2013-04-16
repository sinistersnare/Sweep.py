"""
a docstring that i should fill out...
"""
#import this,antigravity
import sys,os,re,random

from pprint import pprint


class Sweep(object):
   def __init__(self,board_length=10,num_bombs=10):
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
         
   def process(self,x,y):
      
      if (0 <= x < self.board_len) and (0 <= y < self.board_len): #valid point
         if self.bomb_field[x][y] == -1:
            print "YOU DIE MOTHERFUCKER"
         else:
            print "lived...for now"
   
   
   "" #this is how i get notepad++ to end the class...dont worry...


game = Sweep()
game.print_board()
print
game.populate()
game.print_mines()

x,y = game.getpoint()
game.process(x,y)

def main():
   #Should only have to do `game = Sweep();game.play()` will implement later.
   game = Sweep()
   game.print_board()
   print
   game.populate()
   game.print_mines()
   x,y = game.getpoint()
   game.process(x,y)


raw_input('enter anything to exit')