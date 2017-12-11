import numpy as np


class Commodity(object):
    '''
    Description

    Inputs:
    '''

    def __init__(self, price_vector):
        self.__price_vec = price_vector

    def get_price(self):
        return self.__price

    def set_price(self, price_vector):
        self.__price_vec = price_vector


class CommodityWorkingClass(object):
    '''
    Description

    Inputs:
    '''

    def __init__(self, price_vec_1, price_vec_2):
        self.__spread = price_vec_1.get_price() - price_vec_2.get_price()
        self.__ln_spread = np.log(self.__spread)
        self.__ln_MA_fast_vec = set_MA_fast()
        self.__ln_MA_slow_vec = set_MA_slow()

    def set_MA_fast(self, window = 5):
        ret = np.cumsum(self.__ln_spread, dtype=float)
        ret[window:] = ret[window:] - ret[:-window]
        return ret[window - 1:] / window

    def set_MA_slow(self, window = 30):
        ret = np.cumsum(self.__ln_spread, dtype=float)
        ret[window:] = ret[window:] - ret[:-window]
        return ret[window - 1:] / window
