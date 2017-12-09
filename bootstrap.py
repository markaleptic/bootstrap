import numpy as np

class BootstrapData(VectorDataSet):
    len = len(VectorDataSet)
    stdNormVec = np.zeros(len, dtype=float)
    bootVec = np.zeros(len, dtype=float)



    while bootVec[len-1] != 0:
        pos = np.random.randint(0, len, 1)
        bootVec[i] = VectorDataSet[pos]

        if pos + 1 > len:
            # stop

        for i in range(len):
            # keep moving 


