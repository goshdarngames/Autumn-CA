import numpy as np

from cellular_automata.neighbourhood import *

def conway_rule ( space_in, space_out ):

    assert space_in.shape == space_out.shape
    
    #iterate through the lookup using numpy's iterator
    it = np.nditer(space_in, flags=['multi_index'])
    
    #calls to the neighbourhood function store results here
    n_out = np.zeros(9, dtype='uint8')
    
    while not it.finished:
        
        
        moore_neighbourhood ( 
            space_in, 
            it.multi_index[0], it.multi_index[1],
            n_out )
        
        space_out [it.multi_index[0]][it.multi_index[1]] = \
            np.count_nonzero(n_out)
        
        it.iternext()

    #dead_in = space_in < 1
    
    #dead cells with 3 neighbours are born 
    #live cells with 2 or 3 neighbours stay living (add 1 for cell itself)
    live_cells = (space_out == 3)  \
               | ( (space_in > 0) & ( space_out == 4 ) )
    
    
    space_out[:,:] = 0    
    space_out [live_cells] = 1

    

def conway_rule1 (space_in, space_out):
    
    assert space_in.shape == space_out.shape
    
    #iterate through the lookup using numpy's iterator
    it = np.nditer(space_in, flags=['multi_index'])
    
    while not it.finished:
        
        idx = it.multi_index
        
        neighbourhood = moore_neighbourhood ( space_in, idx )
        
        space_out [idx[0]][idx[1]] = np.count_nonzero(neighbourhood) 
        
        space_out [idx[0]][idx[1]] -= space_in [idx[0]][idx[1]]
        
        if space_in [idx[0]][idx[1]] == 0:
            if space_out [idx[0]][idx[1]] == 3:
            
                space_out [idx[0]][idx[1]] = 1
            else:
                space_out [idx[0]][idx[1]] = 0
                
        else:
            if space_out [idx[0]][idx[1]] > 1 and \
               space_out [idx[0]][idx[1]] < 4:
               
               space_out [idx[0]][idx[1]] = 1
            else:
                space_out [idx[0]][idx[1]] = 0
        
        it.iternext()
        
        
        
