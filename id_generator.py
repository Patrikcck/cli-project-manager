class Id_Generator:
    next_id = 41
    
    @classmethod
    def gen_id(cls):
        return cls.next_id
    
    @classmethod
    def bump_id(cls):
        cls.next_id += 1