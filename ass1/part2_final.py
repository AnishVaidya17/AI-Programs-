#IMPLEMENTATION OF NON-AI TECHNIQUE FOR THE ODD NUMBERED MAGIC SQUARE
#For 3x3 Matrix, 5x5 Matrix and 7x7 Matrix

import time
from tabulate import tabulate

def build_matrix(rows, cols):
   matrix = []
   for r in range(0, rows):
      matrix.append([0 for c in range(0, cols)])
   return matrix


def colored(r, g, b, text):
   return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)


def checkpos(x,y,num,m,stype):
   if stype==3:
      sleep=1
      maxnum=10
      para1=0
      para2=2
   
   elif stype==5:
      sleep=1.5
      maxnum=26
      para1=0
      para2=4

   elif stype==7:
      sleep=1.5
      maxnum=50
      para1=0
      para2=6
     
   while(num<= maxnum):
      if num==maxnum:
         return
      if x < para1 and y <= para2:
         x=para2
         x,y,num=placeElement(x,y,num,m)
         
      elif y > para2 and x >=para1:
         y=para1
         x,y,num=placeElement(x,y,num,m)
         
      elif x <para1 and y>para2:
         x=x+2
         y=y-1
         x,y,num=placeElement(x,y,num,m)

      else:
         x,y,num=placeElement(x,y,num,m)
      
      time.sleep(sleep)   
      print("\n\n")
      print(tabulate(m, tablefmt="grid"))
      
      

def placeElement(x,y,num,m):
   if m[x][y] == 0:
      colstr=str(num)
      m[x][y]=colored(255, 255, 0, colstr)
      num+=1
      x=x-1
      y=y+1
      
   
   elif m[x][y] != 0:
      x=x+2
      y=y-1
      colstr=str(num)
      m[x][y]=colored(255, 255, 0, colstr)
      num+=1
      x=x-1
      y+=1
      
   return x,y,num



def threeByThree():
   tbtm=build_matrix(3,3)
   stype=3
   num=1
   x=0
   y=1
   x,y,num=placeElement(x,y,num,tbtm)
   print(tabulate(tbtm, tablefmt="grid"))
   checkpos(x,y,num,tbtm,stype)


def fiveByfive():
   fbfm=build_matrix(5,5)
   stype=5
   num=1
   x=0
   y=2
   x,y,num=placeElement(x,y,num,fbfm)
   print(tabulate(fbfm, tablefmt="grid"))
   checkpos(x,y,num,fbfm,stype)
   
   
def sevenByseven():
   m7=build_matrix(7,7)
   stype=7
   num=1
   x=0
   y=3
   x,y,num=placeElement(x,y,num,m7)
   print(tabulate(m7, tablefmt="grid"))
   checkpos(x,y,num,m7,stype)


      
#MAIN
while(1):
   time.sleep(1)
   print("\n\n")
   print("\033[32mAnish Vaidya Roll-62\033[0m")
   print("\033[32mArtificial Intelligence Assign-1 Part-2\033[0m")
   print("\033[33mImplementation of NON-AI Technique to solve odd numbered Magic Square\033[0m")
   print("\nMagic Square Size Menu")
   print("\n1. 3X3 Matrix")
   print("2. 5X5 Matrix")
   print("3. 7X7 Matrix")
   print("4. Exit")
   ch = int(input("\nEnter Choice:"))
   
   if ch == 1:
      threeByThree()
      
   elif ch == 2:
      fiveByfive()
   
   elif ch == 3:
      sevenByseven()
      
   elif ch == 4:
      print("\033[31mProgram Terminated!\033[0m")
      exit(0)
      
   else:
      print("\nChoose correctly!")