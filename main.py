import src.Analyst as an
import src.Designer as ds
import src.Manager as mng
import src.Programmer as prgr
import src.Tester as tester
import src.Project as prj



a = an.Analyst(1000, 'tugberk', 1)
d = ds.Designer(400, 'ipek', 2)
m = mng.Manager(20000, 'dogan', 3)
p = prgr.Programmer(2000, 'etkin', 4)
t = tester.Tester(3, 'deniz', 5)

project = prj.Project(2, 4)
project.add_new_employee(a)
project.add_new_employee(d)
project.add_new_employee(m)
project.add_new_employee(p)
project.add_new_employee(t)
print('asdf')
