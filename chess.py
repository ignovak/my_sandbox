#!/usr/bin/env python
#-*- coding: utf-8 -*-

from pprint import pprint

class Board():
  SIZE = 8

  def __init__(self):
    self.board = [[0 for i in range(self.SIZE)] for i in range(self.SIZE)]
    self.CHARS = {
      'queen':  ['Q',  self.__queen],
      'king':   ['K',   self.__king],
      'rook':   ['R',   self.__rook],
      'bishop': ['B', self.__bishop],
      'knight': ['H', self.__knight]
    }

  def applyChar(self, name, x, y):
    x -= 1
    y -= 1

    if not(-1 < x < self.SIZE and -1 < y < self.SIZE):
      print name + ': invalid coordinate'
      return

    if type(self.board[y][x]).__name__ == 'str':
      print name + ': coordinate collision'
      return
    
    self.board[self.SIZE - 1 - y][x] = self.CHARS[name][0]
    self.CHARS[name][1](x, self.SIZE - 1 - y)

  def __incrCell(self, x, y):
    if -1 < x < self.SIZE and -1 < y < self.SIZE:
      if type(self.board[y][x]).__name__ == 'int':
        self.board[y][x] += 1


  def __rook(self, x, y):
    for i in range(0, self.SIZE):
      self.__incrCell(x, i)
      self.__incrCell(i, y)

  def __bishop(self, x, y):
    for i in range(0, self.SIZE + 1):
      self.__incrCell(i, i - x + y)
      self.__incrCell(self.SIZE - i, i - self.SIZE + x + y)

  def __queen(self, x, y):
    self.__rook(x, y)
    self.__bishop(x, y)

  def __king(self, x, y):
    for i in range(x - 1, x + 2):
      for j in range(y - 1, y + 2):
        self.__incrCell(i, j)

  def __knight(self, x, y):
    for i in range(-2, 3):
      for j in range(-2, 3):
        if abs(i) + abs(j) == 3:
          self.__incrCell(x - i, y - j)

b = Board()
b.applyChar('queen', 3, 5)
board = map(lambda x: map(lambda y: str(y), x), b.board)
print '\n'.join(map(lambda x: ' '.join(x), board))

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

