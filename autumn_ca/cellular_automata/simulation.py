import numpy as np

def Simulation(size, rule_function):
    """
    This generator is used to advance a simulations function by
    applying a transition function to the space.
    """
    
    def state_transition ( space, buffer ):
            
        #apply the rule funtion
        rule_function ( space, buffer )
        
        #swap the space and the buffer
        temp = space
        space = buffer
        buffer = temp
        
        return space, buffer
    
    
    space = np.zeros( size[0] * size [1], dtype='uint8').reshape (size)
    buffer = np.zeros( size[0] * size [1], dtype='uint8').reshape (size)
    
    while True:
        
        space, buffer = state_transition(space, buffer)
        
        yield space

        
