from src.Employee import Employee

class Manager(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Manager', project, accounting)

    def print_info(self):
        print(self.domain)


