from src.Employee import Employee

class Programmer(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Programmer', project, accounting)

    def print_info(self):
        print(self.domain)


