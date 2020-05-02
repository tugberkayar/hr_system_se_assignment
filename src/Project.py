class Project:

    def __init__(self, pr_id: int, min_emp_num: int, max_emp_num: int, emp_counter = 0, employees={}, running=False):
        self.id = pr_id
        self.min_emp_num = min_emp_num
        self.max_emp_num = max_emp_num
        self.emp_counter = emp_counter
        self.employees = employees
        self.running = running

    @property
    def min_emp_num(self):
        return self.__min_emp_num

    @min_emp_num.setter
    def min_emp_num(self, min_emp_num: int):
        self.__min_emp_num = min_emp_num

    @property
    def max_emp_num(self):
        return self.__max_emp_num

    @max_emp_num.setter
    def max_emp_num(self, max_emp_num: int):
        self.__max_emp_num = max_emp_num

    @property
    def emp_counter(self):
        return self.__emp_counter

    @emp_counter.setter
    def emp_counter(self, value: int):
        self.__emp_counter = value

    @property
    def employess(self):
        return self.__employees

    #fixes no member named __employees problem??
    #@employess.setter
    #def employees(self):
    #    self.__employees = None
    
    def __str__(self):
        return "id : {}\nmin_emp_num : {}\nmax_emp_num : {}\nemp_counter : {}\nis_running : {}\n".format(self.id,self.__min_emp_num,self.__max_emp_num, self.__emp_counter, self.running)

    def add_emp(self, new_emp):
        if self.max_emp_num == self.emp_counter:
            print('PRoje maksimum kapasitede')
            return False
        elif new_emp.id in self.employees.keys():
            print('Eleman zaten bu projede calısıyor')
            return False
        else:
            self.employees[new_emp.id] = new_emp
            self.emp_counter += 1
            return True

    def remove_emp(self, employee_id: int):
        if employee_id not in self.employees.keys():
            print('Bu kisi bu projede calismiyor')
            return False
        elif self.emp_counter == self.min_emp_num:
            print('Calisani cikaramazsiniz. Minimum sayida kisi calisiyor.')
            return False
        else:
            self.employees.pop(employee_id)
            self.emp_counter -= 1
            return True

    def print_all_employees(self):
        for e in self.employees:
            print(self.employees[e])

