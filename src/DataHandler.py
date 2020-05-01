import pandas as pd
import os


class DataHandler:
    def __init__(self):
        # paths relative to main script
        self.souce_files_path = "src"
        self.data_path = "data"
        self.RED = "\033[1;31m"
        self.GREEN = "\033[1;32m"
        self.YELLOW = "\033[1;33m"
        self.RESET = "\033[0;0m"

    def get_data_from_file(self, filename: str):
        file_to_be_located = os.path.join(self.data_path, filename)
        print(self.YELLOW + "Searching for -> {} (relative to main script)".format(file_to_be_located) + self.RESET)
        if not os.path.isfile(file_to_be_located):
            raise Exception(self.RED + "The specified file was not found" + self.RESET)
        else:
            print(self.GREEN + "Found" + self.RESET)
            dataframe = pd.read_csv(file_to_be_located, delimiter=",")
            return dataframe

    def load_current_employees(self, filename: str):
        emp_df = self.get_data_from_file(filename)
        return [dict(row) for index, row in emp_df.iterrows()]

    def load_current_projects(self, filename: str):
        proj_df = self.get_data_from_file(filename)
        return [dict(row) for index, row in proj_df.iterrows()]

    def save_current_employees(self, emps):
        pass

    def save_current_projects(self, projects):
        pass

    def generate_random_employee_data(self, size: int):
        pass
