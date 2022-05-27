
A = 0
B = 1

goal = [2,0]

def applyFuncs(state):
   states=[]
   if state[A] == 0:
      states.append([4, state[B]])
   if state[B] == 0:
      states.append([state[A], 3])
   if state[A] > 0:
      states.append([0, state[B]])
   if state[B] > 0:
      states.append([state[A], 0])
      
   if state[A] < 4 and state[B] > 0:
      space = 4 - state[A]
      fill = min(space, state[B])
      states.append([state[A]+fill, state[B]-fill])
      
      
   if state[A] > 0 and state[B] < 3:
      space = 3 - state[B]
      fill = min(space, state[A])
      states.append([state[A]-fill, state[B]+fill])
      
   return states 




def dfs():
   nodeslist=[[0,0]]
   seq=[]
   visited=[]
   
   while(len(nodeslist)!=0):
      E = nodeslist.pop()
      if E not in visited:
         seq.append(E)
         print(f"{E} added to the sequence\n")
         visited.append(E)
         if E == goal:
            print("\nGoal found!\n")
            return seq
         else:
            for state in applyFuncs(E):
               nodeslist.append(state)
               
      else:
         print(f"{E} not added to the sequence as already there\n")
         
         
         
def bfs():
   nodeslist=[[0,0]]
   seq=[]
   visited=[]
   
   while(len(nodeslist)!=0):
      E = nodeslist.pop(0)
      if E not in visited:
         seq.append(E)
         print(f"{E} added to the sequence\n")
         visited.append(E)
         if E == goal:
            print("\nGoal found!\n")
            return seq
         else:
            for state in applyFuncs(E):
               nodeslist.append(state)
               
      else:
         print(f"{E} not added to the sequence as already there\n")
         
         
         
         
print("\nDFS: ")
dfsans = dfs()
print(f"\n\nDFS ans: {dfsans}")

print("\n\nBFS: ")
bfsans = bfs()
print(f"\n\nBFS ans: {bfsans}")            
   
      
       
      