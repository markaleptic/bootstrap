import numpy as np

class BootstrapData(VectorDataSet):
  len = len(VectorDataSet)
  stdNormVec = np.zeros(len,dtype=float)

  for i in range(len):
    stdNormVec[i] = np.random.normal(0.0, 1.0, len)

