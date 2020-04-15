import src.Employee as em

class Tester(em.Employee):

    def __init__(self, salary: float,
                 name: str,
                 id: int,
                 project=None,
                 accounting=None):

        em.Employee.__init__(self, salary, name, id, 'Tester', project, accounting)

    def print_info(self):
        print(self.domain)


