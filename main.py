from src.ProjectManagement import ProjectManagement
from src.DataHandler import DataHandler
from src.Employee import Employee
EMP_FILE_CSV = "current_employees.csv"
PRO_FILE_CSV = "current_projects.csv"

def main():
    # create project manager
    ProjectManager = ProjectManagement()
    emp_dict = ProjectManager.data_handler.load_current_employees(EMP_FILE_CSV)
    pro_dict = ProjectManager.data_handler.load_current_projects(PRO_FILE_CSV)
    print(emp_dict)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\033[1;31m", end="")
        print(e)
        print("\033[0;0m")
    else:
        print("\033[1;32mEverything was fine\033[0;0m")
    finally:
        print("Shutdown")
