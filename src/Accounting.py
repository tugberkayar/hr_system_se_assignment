from src.API import API
class Accounting:

    def __init__(self):
        self.service = API()

    @property
    def service(self):
        return self.__service

    @service.setter
    def service(self, api: API):
        self.__service = api

    def calculate_salary(self, salary):
        return self.base_salary + 1000 * self.service.percentage

    def calculate_compensation(self, salary):
        return self.service.percentage * salary
