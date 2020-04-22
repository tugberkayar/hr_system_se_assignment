import src.Employee as em
import src.Project as prj


a = em.Analyst(1000, 'tugberk', 1)
d = em.Designer(400, 'ipek', 2)
m = em.Manager(20000, 'dogan', 3)
p = em.Programmer(2000, 'etkin', 4)
t = em.Tester(3, 'deniz', 5)

project = prj.Project(2, 4)
project.add_new_employee(a)
project.add_new_employee(d)
project.add_new_employee(m)
project.add_new_employee(p)
project.add_new_employee(t)
print('asdf')
