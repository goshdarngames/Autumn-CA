import os
from random import randint

from cellular_automata.simulation import Simulation
from cellular_automata.pygame_simulation_viewer import simulation_viewer

from cellular_automata.rule_function import conway_rule

#import lib.space_file_io  as space_file_io


SIMULATION_SIZE = (100,100)
RANDOM_POPULATION = 7500
SCREEN_SIZE = (800,800)
TARGET_FPS = 60

               
               



#test_file = os.path.join( '.',  'saved_spaces','testing', 'pulsar_oscillator.csv' )

#space = space_file_io.read_space_state ( DATA_STRUCTURE, 
#                                             test_file )
#space.transition_function = state_transition




simulation = Simulation( ( SIMULATION_SIZE[0],SIMULATION_SIZE[1] ), conway_rule )
viewer = simulation_viewer( simulation, SCREEN_SIZE, TARGET_FPS ) 

start_space = next(simulation)
for i in range(RANDOM_POPULATION):
    
    start_space \
        [randint(0,SIMULATION_SIZE[0]-1)] \
        [randint(0,SIMULATION_SIZE[1]-1)] = 1   
    
while True:
    
    try:
        next(viewer)
    except StopIteration:
        break


   


