import numpy as np

from lib.simulation import Simulation

from lib.rule_function import conway_rule

from Conway.lib.neighbourhood import moore_neighbourhood


SIMULATION_SIZE = (100,100)
NUMBER_OF_STEPS = 2  

sim = Simulation( SIMULATION_SIZE, conway_rule)      
       
def time_numpy ():
    """
    Times the numpy implementation.  To run use command-line:
    
    python3 -m timeit -s 'from benchmark import time_numpy' 'time_numpy()'
    """

    
    
    for i in range(NUMBER_OF_STEPS):
    
        next(sim)
        
     
#time_numpy ()

neighbourhood_data = np.zeros(10000,dtype='uint8').reshape(100,100)
neighbourhood_pos = (0,0)
n_out = np.zeros(9, dtype='uint8')

def time_neighbourhoods ():
    """
    Times the numpy implementation.  To run use command-line:
    
    python3 -m timeit -s 'from benchmark import time_neighbourhoods' 'time_neighbourhoods()'
    """
    
    for _ in range(10000):
        moore_neighbourhood (neighbourhood_data, 
                             neighbourhood_pos[0], neighbourhood_pos[1],
                             n_out)  



