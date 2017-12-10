import numpy as np

def bootstrap_data(VectorDataSet):
    # Get the vector
    # Generate empty vector of the same size

    # iterator i = 0
    # while i < the number of observations in OG Vector
        # Set  new_vect[i] = some random




    vec_len = len(VectorDataSet)
    std_norm_vec = np.zeros(vec_len, dtype=float)
    bootVec = np.zeros(vec_len, dtype=float)



    while bootVec[vec_len-1] != 0:
        pos = np.random.randint(0, vec_len, 1)
        bootVec[i] = VectorDataSet[pos]

        if pos + 1 > vec_len:
            # stop

        for i in range(vec_len):
            # keep moving


def main():
    oil_vec_1 = np.random.randint(0,100,50,float)
    oil_vec_2 = np.random.randint(0,100,50,float)
    rand_vec_1 = bootstrap_data(oil_vec_1)
    rand_vec_2 = bootstrap_data(oil_vec_2)
