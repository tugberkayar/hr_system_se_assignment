from src.Analyst import Analyst
from src.Designer import Designer
from src.Manager import Manager
from src.Programmer import Programmer
from src.Tester import Tester
from src.Maintainer import Maintainer

a = Analyst(1000, 'tugberk', 1)
d = Designer(400, 'ipek', 2)
m = Manager(20000, 'dogan', 3)
p = Programmer(2000, 'etkin', 4)
t = Tester(3, 'deniz', 5)
ma = Maintainer(5, 'fatma', 7)

a.print_info()
d.print_info()
m.print_info()
p.print_info()
t.print_info()
ma.print_info()
