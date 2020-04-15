from src.Employee import Employee

class Analyst(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Analyst', project, accounting)

    def print_info(self):
        print(self.domain)


