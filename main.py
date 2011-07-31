#!/usr/bin/env python
#

from binascii import unhexlify
from uuid import uuid4

from Crypto.Cipher import AES

from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import util, template

# from Crypto.PublicKey import RSA
# from Crypto.PublicKey.RSA import Random

class Game(db.Model):
  passphrase = db.StringProperty()

class Handler(webapp.RequestHandler):
  def get(self, id):
    record = Game.get_by_id(int(id))
    passphrase = record.passphrase
    cyphertext = self.request.query_string

    encobj = AES.new(passphrase)
    plaintext = encobj.decrypt(unhexlify(cyphertext))
    self.response.out.write(plaintext)
    
class NewHandler(webapp.RequestHandler):
  def get(self):
    passphrase = str(uuid4()).replace('-', '')
    record = Game(passphrase=passphrase)
    record.put()
    self.response.out.write(record.key().id())
    self.response.out.write('<br>')
    self.response.out.write(passphrase)

class OldHandler(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('It Works')
    self.response.out.write('\n')
    f = open('test.gpg')
    self.response.out.write(f.read())
    self.response.out.write('\n')
    f = open('pub.key')
    self.response.out.write(f.read())

def main():
  application = webapp.WSGIApplication([
    ('/new', NewHandler),
    ('/(\d+)', Handler)
    ], debug=True)
  util.run_wsgi_app(application)

if __name__ == '__main__':
  main()
