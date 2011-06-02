#!/usr/bin/env python
#-*- coding: utf-8 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template, util

import os
import logging
import re


RULES = {
  'name': {
     'required': {
        'onerror': 'missingName'
     },
     'limit': {
        'limit': 100,
        'onerror': 'tooLongName'
     }
  },
  'phone': {
     'required': {
        'onerror': 'missingPhone'
     },
     'type': {
        'type': 'phone',
        'onerror': 'incorrectPhone'
     }
  },
  'email': {
     'required': {
        'onerror': 'missingName'
     },
     'type': {
        'type': 'email',
        'onerror': 'incorrectEmail'
     }
  }
}

# RULES = {
#   'name': {
#      'required': True,
#      'limit': 100
#   },
#   'phone': {
#      'required': True,
#      'type': 'phone'
#   },
#   'email': {
#      'required': True,
#      'type': 'email'
#   }
# }
 
def limit(val, args):
  if len(val) > args['limit']:
    return args['onerror']

def required(val, args):
  if not val:
    return args['onerror']

def type(val, args):
  regexp = {
    'phone': '^(\d{5,7}|(\(\d{3}\)|\d{3})\d{7}|\+\d{1,3}(\(\d{3}\)|\d{3})\d{7})$',
    'email': '^[-.\w]+@(?:[a-z\d][-a-z\d]+\.)+[a-z]{2,6}$'
  }[args['type']]
  if not re.match(regexp, val):
    return args['onerror']

def bridge(rule, val, args):
  f = {
    'limit': limit,
    'required': required,
    'type': type
  }[rule]
  return f(val, args)


class Main(webapp.RequestHandler):
  def get(self):
    path = os.path.join('index.html')
    params = {

        }

    self.response.out.write(template.render(path, params))

  def post(self):
    if not self.__validateInput():
      self.redirect('/error')
      return

    self.redirect('/ok')

  def __validateInput(self):
    for field in RULES.keys():
      val = self.request.get(field)
      for rule in RULES[field].keys():
        # logging.info('field: %s, rule: %s, val: %s' % (field, rule, val))
        # logging.info(RULES[field][rule])
        error = bridge(rule, val, RULES[field][rule])
        if error:
          logging.info(error)
          return False
    return True
    # self.response.out.write(i + ': ' + self.request.get(i))
    
class Others(webapp.RequestHandler):
  def get(self):
    page = self.request.path[1:]
    path = os.path.join('ok.html')
    params = {
        'label': 'Thank you!' if page == 'ok' else 'Error!'
        }

    try:
      self.response.out.write(template.render(path, params))
    except Exception:
      pass
    

def main():
  application = webapp.WSGIApplication([('/', Main), ('/.*', Others)],
                                       debug=True)
  util.run_wsgi_app(application)

if __name__ == '__main__':
  main()

