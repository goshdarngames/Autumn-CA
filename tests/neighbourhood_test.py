import unittest
import numpy as np

import autumn_ca

from autumn_ca.cellular_automata.neighbourhood import *


class NeighbourhoodTestCase ( unittest.TestCase ):    

    def test_moore_neighbourhood ( self ):
    
        #put dummy data 0 to 100 (10,10) in 2d array
        np_2d_array = np.arange(100, dtype='uint8').reshape(10,10)
        
        #create an array for neighbourhood func to write data
        n_out = np.zeros ( 9, dtype = 'uint8' )  

        #position to test and expected result
        pos_A = (5,9)
        expt_A = np.array( [48, 49, 40, 58, 59, 50, 68, 69, 60] )
        
        #call neighbourhood function and check result
        moore_neighbourhood( np_2d_array, pos_A[0], pos_A[1], n_out)
        
        self.assertTrue( np.array_equiv( expt_A , n_out ))
        
        pos_B = (5,0)
        expt_B = np.array( [49, 40, 41, 59, 50, 51, 69, 60, 61] )
        
        moore_neighbourhood ( np_2d_array, pos_B[0], pos_B[1], n_out)
        
        self.assertTrue( np.array_equiv( expt_B, n_out ))
        
        #check that function has not changed cell data
        self.assertTrue( 
            np.array_equiv( np_2d_array , np.arange(100).reshape(10,10) ))
            
