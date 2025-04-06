from abc import ABC
from enums import Priority, Status
from id_generator import *

class Task(ABC):
    def __init__(self, id, name, description, priority, status = 1):
        Id_Generator.bump_id()
        self.id = id
        self.name = name
        self.description = description
        if isinstance(priority, Priority):
            self.priority = priority
        elif isinstance(priority, int) and priority in [e.value for e in Priority]:
            self.priority = Priority(priority)
        else:
            raise ValueError(f"Invalid priority value: {priority}")
        if isinstance(status, Status):
            self.status = status
        elif isinstance(status, int) and status in [e.value for e in Status]:
            self.status = Status(status)
        else:
            raise ValueError(f"Invalid status value: {status}")
    
    def __repr__(self):
        return f'{self.name} - {self.description}'
    
    def __str__(self):
        return f'id: {self.id} {self.__class__.__name__}: {self.name} - {self.description}'
    
    def __hash__(self):
        return hash((self.name, self.description))

    def __eq__(self, other):
        if not isinstance(other, Task):
            return False
        return self.name == other.name and self.description == other.description 
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            '_type': self.__class__.__name__
        }

class DevTask(Task):
    
    def __init__(self, id, name, description, priority, status = 1, language = None):
        super().__init__(id, name, description, priority, status)
        self.language = language
    
    def to_dict(self):
        d = super().to_dict()
        d['language'] = self.language
        d['_type'] = 'DevTask'
        return d
    
class QATask(Task):
    
    def __init__(self, id, name, description, priority, status = 1, test_type = None):
        super().__init__(id, name, description, priority, status)
        self.test_type = test_type
        
    def to_dict(self):
        d = super().to_dict()
        d['test_type'] = self.test_type
        d['_type'] = 'QATask'
        return d
    
class DocTask(Task):
    
    def __init__(self, id, name, description, priority, status = 1, document = None):
        super().__init__(id, name, description, priority, status)
        self.document = document
        
    def to_dict(self):
        d = super().to_dict()
        d['document'] = self.document
        d['_type'] = 'DocTask'
        return d