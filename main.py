import json, os
from project import *
from user import *
from encoder import *

CRED = '\033[91m'
CEND = '\033[0m'

clear = lambda: os.system('cls')

inv_opt = CRED + 'Invalid option, choose a number from the list!' + CEND
inv_par = CRED + 'Invalid parameter, try again!' + CEND

def load():
    data = json.load(open('users.json'))
    for user in data:
        user = User(**user)
        Users.add_user(user)

def save():
    with open("users.json", "w") as f:
        l = Users.get_users()
        json.dump(l, f, cls=CustomEncoder, indent=4)

def user_screen(e):
    clear()
    if e:
        print(inv_opt)
    print('Welcome to the Project Manager, please select an option:\n0.Exit\n1.View Users\n2.Add User\n3.Remove User')
    try:
        n = int(input())
    except ValueError:
        user_screen(True)
        return

    if n == 0:
        save()
        return 
    elif n == 1:
        user_choose_screen(False)
    elif n == 2:
        add_user_screen(False)
    elif n == 3:
        remove_user_screen(False)
    else:
        user_screen(True)

def user_choose_screen(e):
    clear()
    if e:
        print(inv_opt)
    print("Choose the id for the user's projects you want to access, type '0' to go back:")

    for user in Users.users:
        print(user.__str__())

    try:
        id = int(input())
    except ValueError:
        user_choose_screen(user, True)
        return
    
    if id == 0:
        user_screen(False)
        return
    user = Users.find_user(id)
    if user:
        project_screen(user, False)
    else:
        user_choose_screen(True)

def add_user_screen(e):
    clear()
    if e:
        print(inv_par)
    print("To cancel at any point, type '0'.\nEnter the user's name:")
    name = input()
    print("Enter the user's surname:")
    surname = input()
    print("Enter the user's email:")
    email = input()

    if '0' in (name, surname, email):
        user_screen(False)
        return

    id = Id_Generator.gen_id()
    user = User(id, name, surname, email)
    Users.add_user(user)
    user_screen(False)

def remove_user_screen(e):
    clear()
    if e:
        print(inv_par)
    for user in Users.users:
        print(user.__str__())
    print("Choose the id for the user you want to remove, type '0' to go back:")

    try:
        id = int(input())
    except ValueError:
        user_screen(True)
        return

    if id == 0:
        user_screen(False)
        return
    elif Users.find_user(id):
        Users.remove_user(Users.find_user(id))
        user_screen(False)
    else:
        remove_user_screen(True)

def project_screen(user, e):
    clear()
    if e:
        print(inv_opt)
    print(f'{user.name} {user.surname}\nMail: {user.email}')
    print("Choose an option:\n0.Back\n1.View Projects\n2.Add Project\n3.Remove Project")

    try:
        n = int(input())
    except ValueError:
        project_screen(user, True)
        return

    if n == 0:
        user_screen(False)
        return
    elif n == 1:
        project_choose_screen(user, False)
    elif n == 2:
        add_project_screen(user, False)
    elif n == 3:
        remove_project_screen(user, False)
    else:
        project_screen(user, True)

def project_choose_screen(user, e):
    clear()
    if e:
        print(inv_opt)
    print(f"Choose the id for the project you want to access, or type '0' to go back:\nProjects for user {user.name} {user.surname}:")

    for project in user.projects:
        print(project.__str__())

    try:
        id = int(input())
    except ValueError:
        project_choose_screen(user, True)
        return
    
    if id == 0:
        project_screen(user, False)
        return
    for project in user.projects:
        if project.id == id:
            task_screen(user, project, e)
            return
    project_screen(user, True)
            
            

def add_project_screen(user, e):
    clear()
    if e:
        print(inv_par)
    print("To cancel at any point, type '0'.\nEnter the project's name:")
    name = input()
    print("Enter the project's description:")
    description = input()
    print("Enter the project's deadline(YYYY-MM-DD):")
    deadline_input = input()
    
    if '0' in (name, description, deadline_input):
        project_screen(user, False)
        return
    
    try:
        deadline = (datetime.fromisoformat(deadline_input) if deadline_input else None)
    except ValueError:
        add_project_screen(user, True)
        return

    id = Id_Generator.gen_id()
    project = Project(id=id, name=name, description=description, deadline=deadline)
    user.projects.add(project)
    project_screen(user, False)

def remove_project_screen(user, e):
    clear()
    if e:
        print(inv_par)
    print(f"Choose the id for the project you want to remove, or type '0' to go back:\nProjects for user {user.name} {user.surname}:")

    for project in user.projects:
        print(project.__str__())

    try:
        id = int(input())
    except ValueError:
        remove_project_screen(user, True)
        return

    if id == 0:
        project_screen(user, False)
        return

    for project in user.projects:
        if project.id == id:
            user.projects.remove(project)
            project_screen(user, False)
            return

    remove_project_screen(user, True)
    
def task_screen(user, project, e):
    clear()
    if e:
        print(inv_opt)
    print(f"{project.__str__()}\nChoose an option:\n0.Back\n1.View Tasks\n2.Add Task\n3.Remove Task")

    try:
        n = int(input())
    except ValueError:
        task_screen(user, project, True)
        return

    if n == 0:
        project_screen(user, False)
        return
    elif n == 1:
        task_choose_screen(user, project, False)
    elif n == 2:
        add_task_screen(user, project, False)
    elif n == 3:
        remove_task_screen(user, project, False)
    else:
        task_screen(user, project, True)

def task_choose_screen(user, project, e):
    clear()
    if e:
        print(inv_opt)
    print(f"Choose the id for the task you want to access, or type '0' to go back:\nTasks for project {project.name}")

    for task in project.tasks:
        print(task.__str__())

    try:
        id = int(input())
    except ValueError:
        task_choose_screen(user, project, True)
        return

    if id == 0:
        task_screen(user, project, False)
        return

    for task in project.tasks:
        if task.id == id:
            task_opt_screen(user, project, task, False)
            return

    task_choose_screen(user, project, True)

def task_opt_screen(user, project, task, e):
    clear()
    if e:
        print(inv_opt)
    print(f"{task.__class__.__name__}:{task.name} - {task.description}\nStatus:{task.status.name}\nPriority:{task.priority.name}")
    print("Choose an option:\n0.Back\n1.Increase Status\n2.Decrease Status\n3.Increase Priority\n4.Decrease Priority")

    try:
        n = int(input())
    except ValueError:
        task_opt_screen(user, project, task, True)
        return

    if n == 0:
        task_choose_screen(user, project, False)
        return
    elif n == 1:
        if task.status.value < len(Status):
            task.status = Status(task.status.value + 1)
        task_opt_screen(user, project, task, False)
    elif n == 2:
        if task.status.value > 1:
            task.status = Status(task.status.value - 1)
        task_opt_screen(user, project, task, False)
    elif n == 3:
        if task.priority.value < len(Priority):
            task.priority = Priority(task.priority.value + 1)
        task_opt_screen(user, project, task, False)
    elif n == 4:
        if task.priority.value > 1:
            task.priority = Priority(task.priority.value - 1)
        task_opt_screen(user, project, task, False)
    else:
        task_opt_screen(user, project, task, True)

def add_task_screen(user, project, e):
    clear()
    if e:
        print(inv_par)
    print("To cancel at any point, type '0'.\nEnter the task's name:")
    name = input()
    print("Enter the task's description:")
    description = input()
    print("Enter the task's priority (1-LOW, 2-MEDIUM, 3-HIGH, 4-CRITICAL):")
    priority_input = input()
    print("Choose task type:\n1.DevTask\n2.QATask\n3.DocTask")
    task_type_input = input()

    if '0' in (name, description, priority_input, task_type_input):
        task_screen(user, project, False)
        return
        
    try:
        priority = int(priority_input)
    except ValueError:
        add_task_screen(user, project, True)
        return
    
    try:
        task_type = int(task_type_input)
    except ValueError:
        add_task_screen(user, project, True)
        return
    
    if priority not in [e.value for e in Priority or not (0 < task_type < 4)]:
        add_task_screen(user, project, True)
        return

    id = Id_Generator.gen_id()

    if task_type == 1:
        print("Enter the programming language:")
        language = input()
        task = DevTask(id, name, description, Priority(priority), Status.NOT_STARTED, language)
    elif task_type == 2:
        print("Enter the test type:")
        test_type = input()
        task = QATask(id, name, description, Priority(priority), Status.NOT_STARTED, test_type)
    elif task_type == 3:
        print("Enter the document name:")
        document = input()
        task = DocTask(id, name, description, Priority(priority), Status.NOT_STARTED, document)
    else:
        add_task_screen(user, project, True)
        return

    project.tasks.add(task)
    task_screen(user, project, False)

def remove_task_screen(user, project, e):
    clear()
    if e:
        print(inv_par)
    print(f"Tasks for project {project.name}\nChoose the id for the task you want to remove, or type '0' to go back:")

    for task in project.tasks:
        print(task.__str__())

    try:
        id = int(input())
    except ValueError:
        remove_task_screen(user, project, True)
        return

    if id == 0:
        task_screen(user, project, False)
        return

    for task in project.tasks:
        if task.id == id:
            project.tasks.remove(task)
            task_screen(user, project, False)
            return

    remove_task_screen(user, project, True)

load()
user_screen(False)
