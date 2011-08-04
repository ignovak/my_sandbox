#!/usr/bin/env python
#-*- coding: utf-8 -*-

def _buildArr(s, key):
  arr = []
  while s:
    arr.append(list(s[:key]))
    s = s[key:]
  return arr


def encrypt(s, key):
  if len(s) % key:
    s = s + ' ' * (key - len(s) % key)

  arr = _buildArr(s, key)
  return ''.join(map(lambda a: ''.join(a), zip(*arr)))

def decrypt(s, key):
  key = len(s) / key

  arr = _buildArr(s, key)
  return ''.join(map(lambda a: ''.join(a), zip(*arr))).strip()

s = """QUnit is a powerful, easy-to-use, JavaScript test suite.

It's used by the jQuery project to test its code and plugins but is capable of testing any generic JavaScript code (and even capable of testing JavaScript code on the server-side).

QUnit is especially useful for regression testing: Whenever a bug is reported, write a test that asserts the existence of that particular bug. Then fix it and commit both.

Every time you work on the code again, run the tests. If the bug comes up again - a regression - you'll spot it immediately and know how to fix it, because you know what code you just changed."""

print s
print '\n\n'
print encrypt(s, 15)
print '\n\n'
print decrypt(encrypt(s, 15), 15)
