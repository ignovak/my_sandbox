#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto import Random

from datetime import datetime

def sign():
  rng = Random.new().read
  print datetime.now()
  rsa = RSA.generate(1024, rng)
  print datetime.now()

  pub = rsa.publickey()
  f = open('key', 'w')
  f.write(rsa.exportKey())
  f.close()

  s = 'var1=val1&var2=val2'
  sign = rsa.sign(s, rng)
  f = open('sign', 'w')
  f.write(str(sign[0]))
  f.close()

def verify():
  sign = (long(open('sign').read()),)
  s = 'var1=val1&var2=val2'
  print sign

  pub = RSA.importKey(open('key').read())
  print pub.verify(s, sign)


