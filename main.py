from src.ProjectManagement import ProjectManagement
from src.DataHandler import DataHandler


def main():
    # create project manager
    ProjectManager = ProjectManagement()
    


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
        print("\033[1;33mShutdown\033[0;0m")
