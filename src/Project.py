


class Project:

    def __init__(self, min_employee: int,
                 max_employee: int):

        self.min_employee = min_employee
        self.max_employee = max_employee
        self.employee_counter = 0
        self.employees = dict()

    @property
    def min_employee(self):
        return self.__min_employee

    @min_employee.setter
    def min_employee(self, min_employee: int):
        self.__min_employee = min_employee

    @property
    def max_employee(self):
        return self.__max_employee

    @max_employee.setter
    def max_employee(self, max_employee: int):
        self.__max_employee = max_employee

    @property
    def employee_counter(self):
        return self.__employee_counter

    @employee_counter.setter
    def employee_counter(self, value: int):
        self.__employee_counter = value


    @property
    def employess(self):
        return self.__employees

    def add_new_employee(self, new_employee):
        if self.max_employee == self.employee_counter:
            print('PRoje maksimum kapasitede')
        elif new_employee.id in self.employees.keys():
            print('Eleman zaten bu projede calısıyor')
        else:
            self.employees[new_employee.id] = new_employee
            self.employee_counter += 1
        return

    def remove_employee(self, employee_id: int):
        if employee_id not in self.employees.keys():
            print('Bu kisi bu projede calismiyor')
        elif self.employee_counter == self.min_employee:
            print('Calisani cikaramazsiniz. Minimum sayida kisi calisiyor.')
        else:
            self.employees.pop(employee_id)
            self.employee_counter -= 1




