from src.WebService import WebService
import numpy as np


class Accounting:

    def __init__(self,service:bool):
        if service:
            self.service = WebService()
        else:
            self.service = None
        self.percentage = np.random.rand(1)[0]

    @property
    def service(self):
        return self.__service

    @service.setter
    def service(self, service: WebService):
        self.__service = service

    def calc_salary(self, salary):
        return 5000 + self.service.percentage * 1000

    def calc_compensation(self, salary: float):
        if self.service is not None:
            return self.service.percentage * salary
        else:
            return self.percentage * salary
