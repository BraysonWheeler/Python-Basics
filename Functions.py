

#def declares function dont need to declare anynumber
def activity(anynumber):
  if (anynumber == 0):
    print ("given number is 0")
  elif (anynumber > 0):
    print ("given number is pos")
  else:
    print("given numbe is negative")

number = int(input("Enter any number"))

activity(number)
activity(number*-2)

#nano python5.py
##!usr/bin/python

string = str(input("Type any string you want"))

def reverse_string(anystring):
  print(anystring[::-1]) #[::-1] will reverse the order of whats inputed

reverse_string(string)

number_list =[1,2,3,4,5]

def function(anylist):
  even_list = []
  odd_list = []
  for i in range(len(anylist)):
    if (number_list[i]% 2 == 0):
      even_list.append(anylist[i])
    else:
      odd_list.append(anylist[i])
  print (even_list)
  print (odd_list)

function(number_list)
