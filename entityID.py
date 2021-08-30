
class EntityID:
    def __init__(self, _id):
        self.id = _id
        
    def __eq__(self, other):
        if isinstance(other, EntityID):
            return self.id == other.id
        return False

    def __hash__(self):
        return self.id
    
    def get_value(self):
        return self.id
    
    def __str__(self):
        return str(self.id)