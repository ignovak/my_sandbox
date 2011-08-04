#!/usr/bin/env python
#-*- coding: utf-8 -*-

from pprint import pprint

SIZE = 8
board = [[0 for i in range(SIZE)] for i in range(SIZE)]

def incrCell(x, y):
  if -1 < x < SIZE and -1 < y < SIZE:
    if type(board[y][x]).__name__ == 'int':
      board[y][x] += 1

def rook(x, y):
  for i in range(0, SIZE):
    incrCell(x, i)
    incrCell(i, y)

def bishop(x, y):
  for i in range(0, SIZE + 1):
    incrCell(i, i - x + y)
    incrCell(SIZE - i, i - SIZE + x + y)

def queen(x, y):
  rook(x, y)
  bishop(x, y)

def king(x, y):
  for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):
      incrCell(i, j)

def knight(x, y):
  for i in range(-2, 3):
    for j in range(-2, 3):
      if abs(i) + abs(j) == 3:
        incrCell(x - i, y - j)

CHARS = {
  'queen': ['Q', queen],
  'king': ['K', king],
  'rook': ['R', rook],
  'bishop': ['B', bishop],
  'knight': ['H', knight]
}

def applyChar(name, x, y):
  x -= 1
  y -= 1

  if not(-1 < x < SIZE and -1 < y < SIZE):
    print name + ': invalid coordinate'
    return

  if type(board[y][x]).__name__ == 'str':
    print name + ': coordinate collision'
    return
  
  board[y][x] = CHARS[name][0]
  CHARS[name][1](x, y)

# applyChar('queen', 3, 6)
# board = map(lambda x: map(lambda y: str(y), x), board)
# print '\n'.join(map(lambda x: ' '.join(x), board))

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

