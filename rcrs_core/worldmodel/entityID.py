
class EntityID:
    def __init__(self, id: int):
        if isinstance(id, EntityID):
            assert()
        self.id = id
        
    def __eq__(self, other):
        if isinstance(other, EntityID):
            return self.id == other.id
        return False

    def __hash__(self):
        return int(self.id)
    
    def get_value(self):
        return self.id
    
    def __str__(self):
        return str(self.id)

    def equals(self, o):
        if isinstance(o, EntityID):
            return self.id == EntityID(o).id
        
        return False