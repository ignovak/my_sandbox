#!/usr/bin/env python
#-*- coding: utf-8 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template, util

import os
import logging

class Handler(webapp.RequestHandler):
  def get(self):
    path = os.path.join('index.html')
    params = {

        }

    self.response.out.write(template.render(path, params))

  def post(self):
    self.__validateInput()
    self.redirect('/ok')
    return

  def __validateInput(self):
    for i in ['nickname', 'name', 'phone', 'email']:
      if 
      self.response.out.write(i + ': ' + self.request.get(i))
    
class Ok(webapp.RequestHandler):
  def get(self):
    path = os.path.join('ok.html')
    params = {}

    self.response.out.write(template.render(path, params))

def main():
  application = webapp.WSGIApplication([('/', Handler), ('/ok', Ok)],
                                       debug=True)
  util.run_wsgi_app(application)

if __name__ == '__main__':
  main()

