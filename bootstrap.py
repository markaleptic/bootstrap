import numpy as np

def stationary_bootstrap(VectorDataSet, q = 0.1):
    """
    Description goes here

    Inputs:
        VectorDataSet   Description of variable

        q               Description of variable


    Return:
        NP array resampled from VectorDataSet


    Example:


    """

    # Get the vector
    # Generate empty vector of the same size


    # iterator i = 0
    # pos = some random index of the original price vector
    # for i < # of observations in data set:
    #     new_vect[i] =
    # Set  new_vect[i] = some random index of the original price vector
    # while i < the number of observations in OG Vector

    # Initialize variables

    vec_len = len(VectorDataSet)
    spread_index_vec = np.zeros(vec_len, dtype=int)
    starting_pos = np.random.randint(0, vec_len, dtype=int)
    spread_index_vec[0] = starting_pos

    stationary_bootstrap_vec = np.zeros(len(VectorDataSet), type(VectorDataSet[0]))
    std_unifs = np.random.normal(0.0, 1.0, vec_len)

    for i in range(1, vec_len):
        if (std_unifs[i] < q):
            spread_index_vec[i] = np.random.randint(0, vec_len, dtype=int)


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
