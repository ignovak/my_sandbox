#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re

def required(val):
  return val != ''

def limit(val, length):
  return len(val) < length

def type(val, type):
  '\+?\d{1,3}?'
  regexp = {
    'phone': '^\d{5,7}|(\(\d{3}\)|\d{3})\d{7}|\+\d{1,3}(\(\d{3}\)|\d{3})\d{7}$',
    'email': '^[_\w][-_.\w]+@(?:[a-z\d][-a-z\d]+\.)+[a-z]{2,6}$'
  }[type]
  return not not re.match(regexp, val)

def bridge(rule, val, *args):
  f = {
    'limit': limit,
    'required': required,
    'type': type
  }[rule]
  return f(val, *args)

# print bridge('limit', 'test', 10)
print bridge('type', '+7(123)2994345', 'phone')
# print bridge('required', '23443456')
