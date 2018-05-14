#cython: boundscheck=False, wraparound=False, nonecheck=False, cdivision=True

cimport numpy as cnp

  
cpdef cnp.ndarray[cnp.uint8_t, ndim=1] moore_neighbourhood( 
    cnp.ndarray[cnp.uint8_t,  ndim=2] np_2d_array, 
    int x, int y,
    cnp.ndarray[cnp.uint8_t, ndim=1] n_out 
    ):

    """
    Calculates the 9 cells of the moore neighbourhood
    at position (x,y) of the input np_2d_array.

    Writes results in the n_out buffer supplied.  The buffer
    is used to save objects testing thousands of neighbours
    from recreating it.
    """


    cdef int width = np_2d_array.shape[0]
    cdef int height = np_2d_array.shape[1]

    #the index of the current neighbour
    cdef int n_x, n_y = 0

    #loop counters for sampling 2D array input
    cdef int i,j = 0

    #count for the 1D output array
    cdef int count = 0

    #loop through -1 to 0 
    for i in range ( 3 ):
        for j in range ( 3 ):
            
            n_x = ( width + x + i - 1 ) % width 
            n_y = ( height + y + j - 1 ) % height

            n_out [ count ] =  np_2d_array [n_x, n_y]   
            count+=1
    
        
