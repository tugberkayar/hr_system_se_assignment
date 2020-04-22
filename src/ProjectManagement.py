from Project import Project


class ProjectManagement:
    def __init__(self, tr: int):
        self.projects = []
        self.project_start_threshold = 3

    def add_project(self, project):
        self.projects.append(project)

    def is_project_ready_to_start(self, project):
        if project.employee_counter < self.project_start_threshold:
            print("not enough employees")
            return False
        return True
