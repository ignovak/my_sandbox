#!/usr/bin/env python
#-*- coding: utf-8 -*-

from pprint import pprint
from time import sleep

class Board():

  def __init__(self, chars=[]):
    self.SIZE = 8
    self.board = [[0 for i in range(self.SIZE)] for i in range(self.SIZE)]
    # self.OLD_CHARS = {
    #   'queen':  ['Q',  self.__queen],
    #   'king':   ['K',   self.__king],
    #   'rook':   ['R',   self.__rook],
    #   'bishop': ['B', self.__bishop],
    #   'knight': ['H', self.__knight]
    # }
    self.CHARS = {
        'Q':  self.__queen,
        'K':   self.__king,
        'R':   self.__rook,
        'B': self.__bishop,
        'H': self.__knight
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
    
    self.board[self.SIZE - 1 - y][x] = name
    self.CHARS[name](x, y)

  def printBoard(self):
    print '\n'
    board = map(lambda x: map(lambda y: str(y), x), self.board)
    print '\n'.join(map(lambda x: ' '.join(x), board))
    print '\n'

  def getMax(self):
    m, x, y = 0, 0, 0
    for i in range(self.SIZE):
      for j in range(self.SIZE):
        if m < self.board[i][j] < 10:
          m, x, y = self.board[i][j], j + 1, self.SIZE - i

    return m, x, y

  def getQuickMax(self):
    return max(
        map(
          lambda a: max(filter(lambda x: x < 10, a)),
          self.board
        )
    )

  def __incrCell(self, x, y):
    y = self.SIZE - 1 - y
    if -1 < x < self.SIZE and -1 < y < self.SIZE:
      if type(self.board[y][x]).__name__ == 'str':
        return self.board[y][x]
      self.board[y][x] += 1


  def __getChar(self, x, y):
    y = self.SIZE - 1 - y
    if -1 < x < self.SIZE and -1 < y < self.SIZE:
      return self.board[y][x]

  def __getRanges(self, x, y, name, direct):
    def getRange(_x, _y):
      def getDoubleBlockedRange(x, _x, y, _y):
        # For cases when queen-bishop or queen-rook are on one line.
        if _x != x:
          return range(min(_x, x), max(_x, x))
        else:
          return range(min(_y, y), max(_y, y))

      def getSingleBlockedRange(x, _x, y, _y):
        # For cases when queen-king or queen-knight are on one line.
        if _x > x:
          return range(0, _x)
        elif _x < x:
          return range(_x, self.SIZE)
        else:
          if _y > y:
            return range(0, _y)
          elif _y < y:
            return range(_y, self.SIZE)

      char = self.__getChar(_x, _y)
      if type(char).__name__ == 'str' and char != name:
        # print char, _x + 1, _y + 1
        if direct == 'diag' and char in ['B', 'Q'] \
            or direct == 'line' and char in ['R', 'Q']:
          return getDoubleBlockedRange(x, _x, y, _y)
        else:
          return getSingleBlockedRange(x, _x, y, _y)

    rangeX = rangeY = range(0, self.SIZE)
    for i in range(0, self.SIZE):
      if direct == 'diag':
        rangeX = getRange(i, i - x + y) or rangeX
        rangeY = getRange(i, -i + x + y) or rangeY
      elif direct == 'line':
        rangeX = getRange(x, i) or rangeX
        rangeY = getRange(i, y) or rangeY

    return (rangeX, rangeY)

  def __rook(self, x, y, name='R'):
    rangeX = rangeY = range(0, self.SIZE)
    rangeX, rangeY = self.__getRanges(x, y, name, direct='line')
    for i in rangeX:
      self.__incrCell(x, i)
    for i in rangeY:
      self.__incrCell(i, y)

  def __bishop(self, x, y, name='B'):
    rangeX, rangeY = self.__getRanges(x, y, name, direct='diag')
    for i in rangeX:
      self.__incrCell(i, i - x + y)
    for i in rangeY:
      self.__incrCell(i, -i + x + y)

  def __queen(self, x, y):
    self.__rook(x, y, 'Q')
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
CONSECUENCE = ('K', 'H', 'B', 'R', 'Q')
points = [
  (1, 2),
  (4, 1),
  (4, 4),
  (2, 5),
  (3, 7),
]

chars = zip(CONSECUENCE, [i[0] for i in points], [i[1] for i in points])

b = Board(chars)
b.printBoard()
print b.getMax()
print b.getQuickMax()
print ''.join(CONSECUENCE)

sugg = {
  'max': 0,
  'cons': '',
  'x': 0,
  'y': 0
}
 
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


chars = mix(list(CONSECUENCE))
for i in range(len(chars)):
  cons = chars[i]
  print cons
# pprint()
# print count

