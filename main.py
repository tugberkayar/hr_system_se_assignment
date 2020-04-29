#from src.Employee import Employee
#from src.Project import Project
#from src.Accounting import Accounting
from src.ProjectManagement import ProjectManagement

#a = em.Analyst(1000, 'tugberk', 1, accounting=ac1)
#d = em.Designer(400, 'ipek', 2, accounting=ac2)
#m = em.Manager(20000, 'dogan', 3,accounting= ac1)
#p = em.Programmer(2000, 'etkin', 4,accounting= ac1)
#t = em.Tester(3, 'deniz', 5, accounting=ac1)

#create project manager
ProjectManager = ProjectManagement()
#create an example project
ProjectManager.create_project(0,2,3)