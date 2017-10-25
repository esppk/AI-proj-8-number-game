# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 19:42:47 2017

@author: Emrick
"""
#%%

#define a class for state of each state of the board
class State():
    def __init__(self, num):
        if type(num) is not list:
            raise TypeError("Number input must be list")
        elif len(num) != 9:
            raise ValueError("Incorrect length")
        self.num = num
    
    def up(self, inplace = True):
        #locate the space 
        pos_space = self.num.index(0)
        if pos_space > 5:
            if inplace == False:
                return None
            else:
                raise ValueError("can't not move up")
        num = self.num.copy()
        num[pos_space] = self.num[pos_space+3]
        num[pos_space+3] = 0
        if inplace == True:
            self.num = num
        else:
            return(num)
    
    def down(self, inplace = True):
        pos_space = self.num.index(0)
        if pos_space < 3:
            if inplace == False:
                return None
            else:
                raise ValueError("can't not move down")
        num = self.num.copy()
        num[pos_space] = self.num[pos_space-3]
        num[pos_space-3] = 0
        if inplace == True:
            self.num = num
        else:
            return(num)
        
    def left(self, inplace = True):
        pos_space = self.num.index(0)
        if pos_space in [2,5,8]:
            if inplace == False:
                return None
            else:
                raise ValueError("can't not move left")
        num = self.num.copy()
        num[pos_space] = self.num[pos_space+1]
        num[pos_space+1] = 0
        if inplace == True:
            self.num = num
        else:
            return(num)
    
    def right(self, inplace = True):
        pos_space = self.num.index(0)
        if pos_space in [0,3,6]:
            if inplace == False:
                return None
            else:
                raise ValueError("can't not move right")
            
        num = self.num.copy()
        num[pos_space] = self.num[pos_space-1]
        num[pos_space-1] = 0
        if inplace == True:
            self.num = num
        else:
            return(num)
        
    def neighbor(self, num):
        neighbor = []
        self.num = num
        for f in [self.down, self.up, self.right, self.left]:
            neighbor.append(f(inplace = False))    
        return(neighbor)
        
#%%
class node():
    def __init__(self, pos):
        self.pos = pos
        self.parent = None
        self.move = None
        #self.visited = False
        

        
#%%            
def DFS(start):
    #state object
    st = State(start)
    s = start
    goal = [0,1,2,3,4,5,6,7,8]
    #only frontier consist of node objects
    frontier = [s]
    g_dict = dict()
    g_dict[tuple(start)] = None
    move = ["right", "left","down","up"]
    while(frontier is not []):
        current = frontier.pop()
        if current == goal:
            path = []
            current = (0,tuple(current))
            while(True):
                
                current = g_dict[current[1]]
                if current == None:
                    break
                path.append(current[0])
               
            path.reverse()
            return ("Success", path)
        #generate neighbor
        neighbor = st.neighbor(current)
        neighbor.reverse()
        for i,neib in enumerate(neighbor):
            if neib is not None:
                if (tuple(neib) not in g_dict.keys())&(neib not in frontier):
                    g_dict[tuple(neib)] = (move[i], tuple(current))
                    frontier.append(neib)
            
    
    return("failure") 
#%%
class Queue(list):
    def __init__(self,list):
        self.value = list
    def add(self,elem):
        self.value.append(elem)
    def pop(self):
        
        return self.value.pop(0)
    
        
 #%%
def BFS(state):
    #state object
    s = state
    goal = [0,1,2,3,4,5,6,7,8]
    #only frontier consist of node objects
    frontier = Queue([node(s.num)])
    front_states = Queue([s.num])
    visited = []
    move = ["down","up","right", "left"]
    while(frontier.value is not []):
        
        current = frontier.pop()
        visited.append(current.pos)
        
        if current.pos == goal:
            path = [current.move]
            pa = current.parent 
            while pa != None:
                path.append(pa.move)
                pa = pa.parent
            path.reverse()
            return("success", path)
            break
        
        #generate neighbor
        gen = State(current.pos)
        neighbor = gen.neighbor()
        for neib in neighbor:
            if (neib not in visited)&(neib not in front_states.value)& (neib != None):
                front_states.pop()
                frontier.add(node(neib))
                front_states.add(neib)
                frontier.value[-1].parent = current
                frontier.value[-1].move = move[neighbor.index(neib)]
  
    return("failure")    
        
    
#%%

        
    



























       
        
        