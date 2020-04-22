import src.Employee as em
import src.Project as prj
import src.Accounting as Acc

ac1 = Acc.Accounting()
ac2 = Acc.Accounting()

print('ac1:', ac1.service.percentage)
print('ac2:', ac2.service.percentage)

a = em.Analyst(1000, 'tugberk', 1, ac1)
d = em.Designer(400, 'ipek', 2, ac2)
m = em.Manager(20000, 'dogan', 3, ac1)
p = em.Programmer(2000, 'etkin', 4, ac1)
t = em.Tester(3, 'deniz', 5, ac1)

print(a.__str__())
exit()

project = prj.Project(2, 4)
project.add_new_employee(a)
project.add_new_employee(d)
project.add_new_employee(m)
project.add_new_employee(p)
project.add_new_employee(t)

project.remove_employee(2)
project.print_all_employees()
