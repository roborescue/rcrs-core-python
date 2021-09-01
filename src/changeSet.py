

from typing import overload


class ChangeSet:
    def __init__(self, _change_set = None):
        
        self.changed = {}
        self.deleted = set()
        self.entity_urns = {}
        
        if _change_set is not None:
            self.merge(_change_set)

    
    # def add_change(self, entity, property):
    #     self.add_change(entity.get_id(), entity.get_urn(), property)

    
    def add_change(self, entity_id, entity_urn, property):
        
        if entity_id in self.deleted:
            return

        new_property = property.copy()
        property_dict = {}
        if entity_id in self.changed:
            property_dict = self.changed.get(entity_id)

        property_dict[new_property.get_urn()] = new_property
        self.changed[entity_id] = property_dict
        self.entity_urns[entity_id] = entity_urn
    
    def entity_deleted(self, _entity_id):
        self.deleted.add(_entity_id)
        if _entity_id in self.changed:
            del self.changed[_entity_id]
        
    def get_changed_properties(self, _entity_id):
        if _entity_id in self.changed:
            return self.changed[_entity_id].values()
        return []
    
    def get_changed_property(self, _entity_id, prop_urn):
        if _entity_id in self.changed:
            property_dict = self.changed.get(_entity_id)
            if property_dict is not None and len(property_dict) > 0:
                if prop_urn in property_dict:
                    return property_dict[prop_urn]
        return None
    
    def get_changed_entities(self):
        return self.changed.keys()
    
    def get_deleted_entities(self):
        return self.deleted
    
    def get_entity_urn(self, _entity_id):
        return self.entity_urns.get(_entity_id)
    
    def merge(self, _change_set):
        for _entity_id in _change_set.changed:
            _entity_urn = _change_set.get_entity_urn(_entity_id)
            _property_dict = _change_set.changed[_entity_id]
            for _property_urn in _property_dict:
                self.add_change(_entity_id, _entity_urn, _property_dict[_property_urn])

        for _entity_id in _change_set.deleted:
            self.entity_deleted(_entity_id)
    
    
    
                
            
    
    
            
    
    
        
    