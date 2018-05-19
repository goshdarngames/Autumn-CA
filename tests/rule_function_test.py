import unittest
import numpy as np

from autumn_ca.cellular_automata.rule_function import *


class RuleFunctionTestCase ( unittest.TestCase ):  

    def test_conway_rule_zeros (self):
        
        test_zeros = np.zeros(9, dtype='uint8').reshape(3,3)
        test_out = np.ones(9, dtype='uint8').reshape(3,3)
        
        conway_rule ( test_zeros, test_out )
        
        #check all values are equal
        self.assertTrue ( np.array_equiv ( test_zeros, test_out ) )
        
        #check the values reference different instances
        self.assertFalse( test_zeros is test_out )
        
        #check all values and shape
        self.assertEqual ( test_out [ test_out == 0].size, 9 ) 
        self.assertEqual ( test_out.shape, (3,3) ) 
        
    #-------------------------------------------------------------------------
    
    def test_conway_rule_ones (self):
        
        test_ones = np.ones(9, dtype='uint8').reshape(3,3)
        test_out = np.ones(9, dtype='uint8').reshape(3,3)
        
        conway_rule ( test_ones, test_out )
        
        #check arrays not equal (ones should flip to 0s )
        self.assertFalse( np.array_equiv ( test_ones, test_out ) )
        
        #check the values reference different instances
        self.assertFalse( test_ones is test_out )
        
        #check values and shape of input array weren't changed
        self.assertEqual ( test_ones [ test_ones == 1].size, 9 ) 
        self.assertEqual ( test_ones.shape, (3,3) ) 
        
        #check all values of output are zero and shape is maintained
        self.assertEqual ( test_out [ test_out == 0].size, 9 ) 
        self.assertEqual ( test_out.shape, (3,3) )

    #-------------------------------------------------------------------------

    def test_dead_with_3_live_neighbours ( self ):

        test_in = np.zeros(16, dtype='uint8').reshape(4,4)
        test_out = np.zeros(16, dtype='uint8').reshape(4,4)
        
        #arrange 3 live cells around (0,0)
        test_in[0][1] = 1
        test_in[1][3] = 1
        test_in[3][3] = 1
        
        #apply the rule function
        conway_rule ( test_in, test_out )
        
        #check output - there should be 2 live cells
        
        self.assertEqual ( test_out[0][0], 1 )
        self.assertEqual ( test_out[0][2], 1 )
        
        self.assertEqual ( test_out [ test_out == 0 ].size, 
                           test_out.size - 2 )
        self.assertEqual ( test_out.shape, (4,4) )
        
        #check input not  changed
        self.assertEqual ( test_in[0][1], 1 )
        self.assertEqual ( test_in[1][3], 1 )
        self.assertEqual ( test_in[3][3], 1 )
        
        self.assertEqual ( test_in [ test_in == 0 ].size, 
                           test_in.size - 3 )
        self.assertEqual ( test_in.shape, (4,4) )
    
    #-------------------------------------------------------------------------
    
    def test_live_with_3_live_neighbours ( self ):

        test_in = np.zeros(16, dtype='uint8').reshape(4,4)
        test_out = np.zeros(16, dtype='uint8').reshape(4,4)
        
        #set (0,0) to 1
        test_in[0][0] = 1
        
        #arrange 3 live cells around (0,0)
        test_in[1][3] = 1
        test_in[1][1] = 1
        test_in[3][3] = 1
        
        #apply rule function
        conway_rule ( test_in, test_out )
        
        #check output
        
        self.assertEqual ( test_out[0][0], 1 )
        
        self.assertEqual ( test_out [ test_out == 0 ].size, 
                           test_out.size - 6 )
        self.assertEqual ( test_out.shape, (4,4) )
        
        #check input not  changed
        self.assertEqual ( test_in[1][3], 1 )
        self.assertEqual ( test_in[1][1], 1 )
        self.assertEqual ( test_in[3][3], 1 )
        
        self.assertEqual ( test_in [ test_in == 0 ].size, 
                           test_in.size - 4 )
        self.assertEqual ( test_in.shape, (4,4) )
        
    
        
