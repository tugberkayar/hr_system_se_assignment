import numpy as np


class API:

    def __init__(self):
        self.__percentage = np.random.rand(1)[0]

    @property
    def percentage(self):
        return self.__percentage