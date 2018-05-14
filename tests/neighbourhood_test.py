import unittest
import numpy as np

from .neighbourhood import *


class NeighbourhoodTestCase ( unittest.TestCase ):    

    def test_moore_neighbourhood ( self ):
    
        #put dummy data 0 to 100 (10,10) in 2d array
        np_2d_array = np.arange(100).reshape(10,10)
        
        #position to test and expected result
        pos_A = (5,9)
        expt_A = np.array( [[48, 49, 40],  [58, 59, 50],  [68, 69, 60]] )
        
        #call neighbourhood function and check result
        neigh_A = moore_neighbourhood( np_2d_array, pos_A)
        
        self.assertTrue( np.array_equiv(expt_A,neigh_A))
        
        pos_B = (5,0)
        expt_B = np.array( [[49, 40, 41], [59, 50, 51], [69, 60, 61]] )
        
        neigh_B = moore_neighbourhood ( np_2d_array, pos_B )
        self.assertTrue( np.array_equiv(expt_B,neigh_B))
        
        #check that function has not changed cell data
        self.assertTrue( 
            np.array_equiv( np_2d_array , np.arange(100).reshape(10,10) ))
            