#nano python6.py
#!#usr/bin/python

#class will strore a name and email

class info():
  def __init__(self,name,email):
    self.name = name
    self.email = email

jack = info('jack','jack@gmail.com')
print ("This users name is : " + jack.name)
print ("This users email is : " + jack.email)
