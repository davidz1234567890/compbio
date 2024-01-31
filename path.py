import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.
def is_empty_list(g: Dict[int, List[int]]):
    for i in g:
        if len(g[i])>0:
            return False
    return True

def index_not_empty(g: Dict[int, List[int]]):
    for i in g:
        if len(g[i]) > 0:
            return i
    return -1
# Insert your eulerian_cycle function here, along with any subroutines you need
# g[u] is the list of neighbors of the vertex u
def eulerian_path(g: Dict[int, List[int]]) -> Iterable[int]:
    """Constructs an Eulerian cycle in a graph."""
    #print("hello")
    solution = []
    solution.append(0)
    index = 0
    next = g[0][0]
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
    index = index_not_empty(g)
    #print("here is index in line 34")
    #print(index)
    while solution[0] != index:
        m = solution[0]
        del solution[0]
        solution.append(m)
        
    #print(solution)
    next = g[index][0]
    #print("here is next:")
    #print(next)
    solution.append(index)
    solution.append(next)
    g[index].remove(next)
    while is_empty_list(g)==False:
        #print("comes in here")
        #break
        index = index_not_empty(g)
        next = g[index][0]
        new_sol = []
        new_sol.append(index)
        
        #break
        while len(g[next]) > 0:
            new_sol.append(next)
            #print("here is index in line 53")
            #print(index)
            #print("here is next in line 53")
            #print(next)
            (g[index]).remove(next)
            index = next
        #if len(g[index]) > 0:
            next = g[index][0]
        g[index].remove(next)
        #print(g)
        #print(is_empty_list(g))
        #print(new_sol)
        #print(solution)
        
        #if count == 1:
        #    break
       
        index = index_not_empty(g)
        #print("here is index in line 34")
        #print(index)
        solution = new_sol + solution
        
        
        if is_empty_list(g) == True:
            
            #while solution[0] != 0:
            #    m = solution[0]
            #    del solution[0]
            #    solution.append(m)
            #solution.append(solution[0])
            break
        while solution[0] != index:
            m = solution[0]
            del solution[0]
            solution.append(m)
        
        #print(solution)
        next = g[index][0]
        #print("here is next in line 72")
        #print(next)
        #print("here is index in line 72")
       # print(index)
        #new_sol = []
        
        #print(new_sol)
        #print(g)
        #break
        
            
       
            
            
        
        count += 1
    #print("solution = ")
    return solution
