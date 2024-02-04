import sys
from typing import List, Dict, Iterable
from collections import defaultdict
# Please do not remove package declarations because these are used by the autograder.
def is_empty_list(g: Dict[int, List[int]]):
    for i in g:
        if len(g[i])>0:
            return False
    return True
def foundInDict(g: Dict[int, List[int]], abc):
    for i in g:
        for j in g[i]:
            if j == abc:
                return True
    return False
'''
def lowest_index(g: Dict[int, List[int]]):
    #index = 100000000
    
    for i in g:
        if foundinDict(g, i) == False:
            #max = len(g[i])
            maxIndex = i
    return maxIndex
'''
def new_subroutine(g: Dict[int, List[int]]):
    array = []
    for i in g[0]:
        #for j in paths[i]:
        if i==number or i not in g:
            array.append(i)
        else:
            #array.append(new_subroutine(g, i))
            array = array + new_subroutine(g, i)
    return array
def index_with_node(g: Dict[int, List[int]]):
    for i in g:
        if(len(g[i]) > 0):
            return i
    return -1
def index_not_empty(llist, g: Dict[int, List[int]]):
    for i in llist:
        if len(g[i]) > 0:
            return i
    return -1

# Insert your eulerian_cycle function here, along with any subroutines you need
# g[u] is the list of neighbors of the vertex u
def eulerian_path(g: Dict[int, List[int]]) -> Iterable[int]:
    """Constructs an Eulerian cycle in a graph."""
    #neighbors = {}
    neighbors = defaultdict(int)
    for i in g:
        for j in g[i]:
            '''if i not in neighbors:
                neighbors.append(i)
                neighbors[i] = 0'''
            
            neighbors[i] = neighbors[i] + 1
            '''if j not in neighbors:
                neighbors.append(j)
                neighbors[j] = 0'''
            neighbors[j] = neighbors[j] - 1
    #print(neighbors)
    #print(g)
    #tempe = []
    #return tempe
    for i, j in neighbors.items():
        if j == 1:
            beginning = i
    for i, j in neighbors.items():
        if j == -1:
            end = j
    if end not in neighbors:
        g[end] = beginning
    if end in neighbors:
        g[end].append(beginning)
    path = {}
    while len(g) > 0:
        curr = next(iter(g))
        p1 = [curr]
        path[curr] = p1
        while (curr in g)==True:
            next_ = g[curr][0]
            #g[curr].remove(n)
            del g[curr][0]
            temp = curr
            
            if len(g[temp]) < 1:
                #g.remove(temp)
                del g[temp]
            curr = next_
            p1.append(curr)
        #path.append(p1)
    '''cycle = []
    #graph = {x: y for x, y in g}
    #print(graph)
    return cycle
    gMapKeys = list(g.keys())
    for listKey in gMapKeys:
        incomingEdges = 0
        outgoingEdges = g[listKey]
        for outgoingEdge in outgoingEdges:
            if outgoingEdge not in g:
                unbalancedNode = outgoingEdge
                unbalancedInOutNode = unbalancedNode
                g[unbalancedNode] = []
        for dictionaryKey in g:
            edges = g[dictionaryKey]
            if len(edges) != 1:
                for i in range(len(edges)):
                    if listKey == edges[i]:
                        incomingEdges += 1
            else:
                if listKey == edges[0]:
                    incomingEdges += 1
# Find unbalanced nodes
        if len(outgoingEdges) - incomingEdges == 1:
            unbalancedOutInNode = listKey
            activeNode = listKey
            cycle.append(activeNode)
    
    
    
    solution = []
    solution.append(unbalancedOutInNode)
    index = unbalancedOutInNode
    next = g[index][0]
    
    count = 0
    while next in g and len(g[next]) > 0:
        solution.append(next)
     
        (g[index]).remove(next)
        index = next
        if index in g and len(g[index]) > 0:
            next = g[index][0]
    if index in g and next in g[index] and next not in solution:
        solution.append(next)
        g[index].remove(next)
    elif index in g and next in g[index]:
        solution.append(next)
        g[index].remove(next)
    index = index_with_node(g)
    desired_index = index
    if(index < 0):
        
        #solution.append(next)
        return solution
    #while index in solution and solution[0] != index:
    #    m = solution[0]
    #    del solution[0]
    #    solution.append(m)
 
    next = g[index][0]
    if index in solution:
        temp = solution.index(index)
    else:
        solution.insert(0, index)
        temp = 0
    while is_empty_list(g)==False:    
        if((temp == 0 and solution[1]==next)==False):
            solution.insert(temp+1, next)
        temp = temp + 1
        
        g[index].remove(next)
        index = next
        if index not in g:
            index = index_with_node(g)
            if index < 0:
                return solution
            next = g[index][0]
            if index in solution:
                temp = solution.index(index)
            else:
                solution.insert(0, index)
                temp = 0
        if(len(g[next])>0):
            next = g[next][0]
        else:
            if(is_empty_list(g)==True):
                
                break
            
            index = index_with_node(g)
            next = g[index][0]
            if index in solution:
                temp = solution.index(index)
            else:
                solution.insert(0, index)
                temp = 0
          
            continue
        
        '''
    sol = []
    sol = new_subroutine(path)
    for i in sol:
        if sol[i]==end:
            if sol[i+1] == beginning:
                start_index = i+1
    sol = sol[i+1: len(sol)] + sol[1:i+1]
    return sol
    '''
        if(next in g and len(g[next]) > 0):
            if(solution[len(solution) - 1] != index):
                solution.append(index)
            solution.append(next)
      
        else:
            if(next not in g):
                solution.append(index)
                solution.append(next)
            elif(len(g[next]) == 0):
                if next in g[index]:
                    g[index].remove(next)
                    index = index_with_node(g)
                    if index == -1:
                        index = desired_index
                        break
                    next = g[index][0]
                    continue
        g[index].remove(next)
        index = next
      
        if(next in g and len(g[next])>0):
            next = g[next][0]
        else:
            if(is_empty_list(g)==True):
                
                break
            
            index = index_with_node(g)
            desired_index = index
            next = g[index][0]
        
          
            continue
        '''
            
            
        
        #count += 1
    '''
    solution.append(index)
    while solution[0] != index:
        m = solution[0]
        del solution[0]
        solution.append(m)
    '''
    #return solution




