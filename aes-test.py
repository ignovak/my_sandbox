#!/usr/bin/env python
#-*- coding: utf-8 -*-

from sys import argv
from Crypto.Cipher import AES

key = argv[1]
key = 'cf7b81e651414d43aa4671ff52ceb83b'
aes = AES.new(key)

s = argv[2]
s = s + ' ' * (16 - len(s) % 16)

print aes.encrypt(s).encode('hex')
