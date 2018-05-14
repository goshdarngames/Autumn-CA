import unittest

from .simulation import Simulation

def mock_rule ( array_in, array_out ):
    
    array_out *= 0
    
    array_out += array_in
    array_out += 1

class SimulationTestCase ( unittest.TestCase ):
    
        
    def test_buffer_swapping_pointers(self) :
        
        sim = Simulation ( (10,10) , mock_rule ) 
        
        
        s_space = next(sim)
        
        ss_space = next(sim)
        
        #assert returned space is not the previous
        self.assertFalse ( s_space  is ss_space )
        
        
        sss_space = next(sim)
        self.assertFalse ( sss_space  is ss_space )
        self.assertTrue (  sss_space is s_space )
        
    #-------------------------------------------------------------------------
    
    def test_values_apply_rule ( self ):
    
        sim = Simulation ( (10, 10), mock_rule )
        
        space = next(sim)
        
        for x,row in enumerate (space):
            for y,val in enumerate (row):
                
                self.assertEqual(val, 1)
                
        space = next(sim)
        
        for x,row in enumerate (space):
            for y,val in enumerate (row):
                
                self.assertEqual(val, 2)
        