import random
import os,sys 



def primary():
  # print("Keep it logically awesome.")
    # print("Well hi there, gotta keep it going!.")
  f = open("quotes.txt")
  quote1 = f.readlines()
  f.close()
  g = open("quotes.txt")
  quote2 = g.readlines()
  g.close
  
  frst =13
  rad=random.randint(0, frst)   
  last = 13
  rnd=random.randint(0, last)
  
  print(" " + quote1[rad], end=" " )
  print(quote2[rnd], end=" " )
  #print(quote2[rnd])
  e = open('testtext.txt', 'w')
  print (quote1[rad], quote2[rnd], file=e)
  e.close


if __name__== "__main__":
  primary()
