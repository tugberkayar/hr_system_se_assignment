from src.Employee import Employee

class Maintainer(Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        Employee.__init__(self, salary, name, id, 'Maintainer', project, accounting)

    def print_info(self):
        print(self.domain)


