#!/usr/bin/env python
#-*- coding: utf-8 -*-

from pprint import pprint
from time import sleep

class Board():

  def __init__(self, chars=[]):
    self.SIZE = 8
    self.board = [[0 for i in range(self.SIZE)] for i in range(self.SIZE)]
    self.CHARS = {
      'queen':  ['Q',  self.__queen],
      'king':   ['K',   self.__king],
      'rook':   ['R',   self.__rook],
      'bishop': ['B', self.__bishop],
      'knight': ['H', self.__knight]
    }

    for char in chars:
      self.applyChar(char[0], char[1], char[2])

  def applyChar(self, name, x, y):
    x -= 1
    y -= 1

    if not(-1 < x < self.SIZE and -1 < y < self.SIZE):
      print name + ': invalid coordinate'
      return

    if type(self.board[self.SIZE - 1 - y][x]).__name__ == 'str':
      print name + ': coordinate collision'
      return
    
    self.board[self.SIZE - 1 - y][x] = self.CHARS[name][0]
    self.CHARS[name][1](x, y)

  def __incrCell(self, x, y):
    y = self.SIZE - 1 - y
    if -1 < x < self.SIZE and -1 < y < self.SIZE:
      if type(self.board[y][x]).__name__ == 'str':
        return self.board[y][x]
      self.board[y][x] += 1


  def __rook(self, x, y):
    for i in range(0, self.SIZE):
      self.__incrCell(x, i)
      self.__incrCell(i, y)

  def __getChar(self, x, y):
    y = self.SIZE - 1 - y
    if -1 < x < self.SIZE and -1 < y < self.SIZE:
      return self.board[y][x]

  def __getRanges(self, x, y, name):
    def getRange(_x, _y):
      char = self.__getChar(_x, _y)
      _range = None
      if type(char).__name__ == 'str' and char != name:
        if char in ['B', 'Q']:
          _range = range(min(_x, x), max(_x, x))
        else:
          if _x > x:
            _range = range(0, _x)
          else:
            _range = range(_x, self.SIZE)
        print char, _x + 1, _y + 1
      return _range

    rangeX = rangeY = range(0, self.SIZE)
    for i in range(0, self.SIZE):
      rangeX = getRange(i, i - x + y) or rangeX
      rangeY = getRange(i, -i + x + y) or rangeY

    return (rangeX, rangeY)

  def __bishop(self, x, y, name='B'):
    rangeX, rangeY = self.__getRanges(x, y, name)

    for i in rangeX:
      char = self.__incrCell(i, i - x + y)

    for i in rangeY:
      char = self.__incrCell(i, -i + x + y)

  def __queen(self, x, y):
    self.__rook(x, y)
    self.__bishop(x, y, 'Q')

  def __king(self, x, y):
    for i in range(x - 1, x + 2):
      for j in range(y - 1, y + 2):
        self.__incrCell(i, j)

  def __knight(self, x, y):
    for i in range(-2, 3):
      for j in range(-2, 3):
        if abs(i) + abs(j) == 3:
          self.__incrCell(x - i, y - j)

# b.applyChar('queen', 5, 3)
chars = [
    ['king', 3, 3],
    ['bishop', 3, 7],
    ['queen', 5, 5],
]
b = Board(chars)

print '\n'
board = map(lambda x: map(lambda y: str(y), x), b.board)
print '\n'.join(map(lambda x: ' '.join(x), board))
print '\n'
 
count = [0]
cache = {}
def mix(a):
  count[0] += 1
  if len(a) < 2:
    return [a]
  else:
    s = ''.join(map(str, a))
    if cache.get(s):
      return cache[s]
    else:
      res = []
      for k, v in enumerate(a):
        res += map(lambda x: [v] + x, mix(a[:k] + a[k + 1:]))
      cache[s] = res
      return res


# chars = [i for i in CHARS]
# pprint(mix(chars))

