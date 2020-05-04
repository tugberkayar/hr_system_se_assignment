import pandas as pd
import os
import src.constants as constants
from src.Employee import Employee
from src.Project import Project
from src.Accounting import Accounting
from collections import defaultdict


class DataHandler:
    def __init__(self):
        # paths relative to main script
        self.soruce_files_path = "src"
        self.data_path = "data"
        self.RED = "\033[1;31m"
        self.GREEN = "\033[1;32m"
        self.YELLOW = "\033[1;33m"
        self.RESET = "\033[0;0m"

    def get_data_from_file(self, filename: str):
        file_to_be_located = os.path.join(self.data_path, filename)
        print(self.YELLOW + "Searching for -> {} (relative to main script)".format(
            file_to_be_located) + self.RESET)
        if not os.path.isfile(file_to_be_located):
            raise Exception(
                self.RED + "The specified file was not found" + self.RESET)
        else:
            print(self.GREEN + "Found" + self.RESET)
            dataframe = pd.read_csv(file_to_be_located, delimiter=",")
            return dataframe

    def load_current_employees(self):
        emp_df = self.get_data_from_file(constants.EMPLOYEE_FILE_CSV)
        return {row['id']: Employee(
            salary=row['salary'],
            name=row['name'],
            domain=row['domain'],
            emp_id=row['id'],
            accounting=Accounting(
                True) if row['accounting'] == "WebService" else Accounting(False),
            project_id=row['project_id']) for index, row in emp_df.iterrows()}

    def load_applicants(self):
        applicants_df = self.get_data_from_file(constants.APPLICANT_FILE_NAME)
        return list(applicants_df.T.to_dict().values())

    def load_current_projects(self):
        proj_df = self.get_data_from_file(constants.PROJECT_FILE_CSV)
        return {row['id']: Project(
            pr_id=row['id'],
            name=row['name'],
            min_emp_num=row['min_emp_num'],
            max_emp_num=row['max_emp_num'],
            emp_counter=row['emp_counter'],
            running=row['running']
        ) for index, row in proj_df.iterrows()}

    def save_current_employees(self, emps):
        df_to_save = defaultdict(list)
        for e in emps:
            df_to_save["id"].append(e.id)
            df_to_save["name"].append(e.name)
            df_to_save["domain"].append(e.domain)
            df_to_save["project_id"].append(e.project_id)
            df_to_save["salary"].append(e.salary)
            accounting = "Default" if e.accounting.service == None else "WebService"
            df_to_save["accounting"].append(accounting)
        pd.DataFrame(df_to_save).to_csv(os.path.join(
            self.data_path, constants.EMPLOYEE_FILE_CSV), index=False)

    def save_current_projects(self, projects):
        df_to_save = defaultdict(list)
        for p in projects:
            df_to_save["id"].append(p.id)
            df_to_save["name"].append(p.name)
            df_to_save["min_emp_num"].append(p.min_emp_num)
            df_to_save["max_emp_num"].append(p.max_emp_num)
            df_to_save["emp_counter"].append(p.emp_counter)
            df_to_save["running"].append(p.running)
        pd.DataFrame(df_to_save).to_csv(os.path.join(self.data_path, constants.PROJECT_FILE_CSV), index=False)
        

    def save_current_applicants(self, applicants):
        pd.DataFrame(applicants).to_csv(os.path.join(self.data_path,constants.APPLICANT_FILE_NAME),index=False)
