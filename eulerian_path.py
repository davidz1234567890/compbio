import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.
def is_empty_list(g: Dict[int, List[int]]):
    for i in g:
        if len(g[i])>0:
            return False
    return True

def lowest_index(g: Dict[int, List[int]]):
    index = 100000000
    for i in g:
        if i < index:
            index = i
    return index

def index_not_empty(llist, g: Dict[int, List[int]]):
    for i in llist:
        if len(g[i]) > 0:
            return i
    return -1
# Insert your eulerian_cycle function here, along with any subroutines you need
# g[u] is the list of neighbors of the vertex u
def eulerian_cycle(g: Dict[int, List[int]]) -> Iterable[int]:
    """Constructs an Eulerian cycle in a graph."""
    #print("hello")
    solution = []
    solution.append(lowest_index(g))
    index = lowest_index(g)
    next = g[index][0]
    
    #print("next = ")
    #print(next)
    count = 0
    while len(g[next]) > 0:
        solution.append(next)
        #print(index)
        (g[index]).remove(next)
        index = next
        #if len(g[index]) > 0:
        next = g[index][0]
    g[index].remove(next)
    index = index_not_empty(solution, g)
    if(index < 0):
        solution.append(lowest_index(g))
        return solution
    #while solution[0] != index:
    #    m = solution[0]
    #    del solution[0]
    #    solution.append(m)
        
    #print(solution)
    next = g[index][0]
    
    #while is_empty_list(g)==False:
    temp = solution.index(index)
    while is_empty_list(g)==False:    
        
      
        solution.insert(temp+1, next)
        temp = temp + 1
        
        g[index].remove(next)
        index = next
      
        if(len(g[next])>0):
            next = g[next][0]
        else:
            if(is_empty_list(g)==True):
                
                break
            
            index = index_not_empty(solution, g)
            next = g[index][0]
            temp = solution.index(index)
          
            continue
     
            
            
        
        count += 1
    #print("solution = ")
    solution.append(lowest_index(g))
    return solution
