import random

board = {
   1:0, 2:1, 3:3,
   8:8, 9:2, 4:4,
   7:7, 6:6, 5:5
}


def displayBoard(board):
   j=0
   for i in board.items():
      print(list(i), end=" ")
      j+=1
      if j>=3:
         print(end="\n")
         j=0
         
         
def objValue(board):
   count=0
   for key,val in board.items():
      if key == val:
         count+=1
   return count   

def isgoalState(board):   
   if objValue(board) == 8:
      return 1 
   else:
      return 0        


def swapPoss(pos1, pos2, board):
   x=board[pos1]
   board[pos1]=board[pos2]
   board[pos2]=x 
   return board
   



   
def listToInt(list1):
   strings = [str(liststr) for liststr in list1]
   a_string = "".join(strings)
   a_int = int(a_string)
   return a_int
         

def generate_Poss(board):
   poss={}
   poss = board
   if poss[9] == 0:
      cklist = [2,8,4,6]
      a = random.sample(cklist, k=1) 
      i = listToInt(a)
      poss = swapPoss(9, i, poss)
      print("\n")
      displayBoard(poss)
      print("ObjValue is: ", objValue(poss))
      return poss
       
   elif poss[1] == 0:
      cklist = [2,8]
      a = random.sample(cklist, k=1) 
      i = listToInt(a)
      poss = swapPoss(1, i, poss)
      print("\n")
      displayBoard(poss)
      print("ObjValue is: ", objValue(poss))
      return poss
   
   elif poss[2] == 0:
      cklist = [1,3,9]
      a= random.sample(cklist, k=1)
      i=listToInt(a)
      poss = swapPoss(2, i, poss)
      print("\n")
      displayBoard(poss)
      print("ObjVal is: ", objValue(poss))
      return poss
   
   elif poss[3] == 0:
      cklist = [2,4]
      a=random.sample(cklist,k=1)
      i=listToInt(a)
      poss=swapPoss(3, i, poss)
      displayBoard(poss)
      print("\nObjVal is: ", objValue(poss))
      return poss
   
   elif poss[4] == 0:
      cklist = [3,9,5]
      a=random.sample(cklist,k=1)
      i=listToInt(a)
      poss=swapPoss(4, i, poss)
      displayBoard(poss)
      print("\nObjVal is: ", objValue(poss))
      return poss
   
   elif poss[5] == 0:
      cklist = [4,6]
      a=random.sample(cklist,k=1)
      i=listToInt(a)
      poss=swapPoss(5, i, poss)
      displayBoard(poss)
      print("\nObjVal is: ", objValue(poss))
      return poss
   
   elif poss[6] == 0:
      cklist = [7,9,5]
      a=random.sample(cklist,k=1)
      i=listToInt(a)
      poss=swapPoss(6, i, poss)
      displayBoard(poss)
      print("\nObjVal is: ", objValue(poss))
      return poss
   
   elif poss[7] == 0:
      cklist = [6,8]
      a=random.sample(cklist,k=1)
      i=listToInt(a)
      poss=swapPoss(7, i, poss)
      displayBoard(poss)
      print("\nObjVal is: ", objValue(poss))
      return poss
   
   elif poss[8] == 0:
      cklist = [1,7,9]
      a=random.sample(cklist,k=1)
      i=listToInt(a)
      poss=swapPoss(8, i, poss)
      displayBoard(poss)
      print("\nObjVal is: ", objValue(poss))
      return poss
      
   
      
"""def listToInt(list1):
      strings = [str(liststr) for liststr in list1]
      a_string = "".join(strings)
      a_int = int(a_string)
      return a_int"""



def hillclimb(board):
   curr={}
   curr = board      #this is getting the initial board 
   loop = True 
   count = 0
   while loop == True:
      if count <= 30:
         nxt = generate_Poss(curr)
         count +=1 
         if isgoalState(nxt):
            print("Goal State found!")
            displayBoard(nxt)
            print("ObjValue = ", objValue(nxt))
            loop = False
         else:
            if objValue(curr) < objValue(nxt):
               curr = nxt
            continue
         
      elif count >30:
         print("\nMax Iteration limit reached! Aborted")
         print("\nGoal Not Found!")
         loop = False
         
         


print("\n\n")
print("\033[32mAnish Vaidya Roll-62\033[0m")
print("\033[32mArtificial Intelligence Assign-3\033[0m")
print("\033[33mHill Climb\033[0m")
initial = board
print("\nThe initial State is: ")
displayBoard(initial)
print("ObjVal is: ", objValue(initial))
print("\n\n")

if isgoalState(initial)==1:
   print("The Initial State is Goal State!")
   displayBoard(initial)
   print("objVal is: ", objValue(initial))
   
else: 
   hillclimb(initial)





