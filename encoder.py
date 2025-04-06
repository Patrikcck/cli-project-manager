from enum import Enum
from json import *
from user import *
from project import *
from task import *

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value
        elif isinstance(obj, Project):
            return obj.to_dict()
        elif isinstance(obj, User):
            return obj.to_dict()
        elif isinstance(obj, Task):
            return obj.to_dict()
        elif isinstance(obj, Users):
            return obj.to_dict()
        return super().default(obj)
        