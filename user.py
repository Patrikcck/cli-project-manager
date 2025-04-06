from id_generator import *
from project import Project, Projects

class User:
    def __init__(self, id, name, surname, email, projects = None):
        Id_Generator.bump_id()
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.projects = set()
        if projects is not None:
            for project in projects:
                project = Project(**project)
                Projects.add_project(project)
                self.projects.add(project)
        else:
            self.projects = set()
            
    def __str__(self):
        return f'id:{self.id} {self.name} {self.surname}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'projects': list(self.projects)
        }
        
    def get_projects(self):
        for project in self.projects:
            print(Project.__str__(project))
            
            
    

class Users:
    users = set()
        
    @classmethod
    def get_users(cls):
        return list(cls.users)
    
    @classmethod
    def add_user(cls, user: User) -> None:
        cls.users.add(user)
        
    @classmethod
    def remove_user(cls, user: User) -> None:
        cls.users.remove(user)
        
    @classmethod
    def find_user(cls, id) -> User:
        for user in cls.users:
            if user.id == id:
                return user
        return False