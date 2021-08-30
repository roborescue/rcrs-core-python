from standardPropertyURN import StandardPropertyURN
from standardEntityURN import StandardEntityURN
from entities.entity import Entity
from property import IntProperty
from property import EntityIDProperty
from property import IntArrayProperty

class Human(Entity):
    def __init__(self, entity_id):
        Entity.__init__(self, entity_id)
        self.x = IntProperty(StandardPropertyURN.X.value)
        self.y = IntProperty(StandardPropertyURN.Y.value)
        self.travel_distance = IntProperty(StandardPropertyURN.TRAVEL_DISTANCE.value)
        self.position = EntityIDProperty(StandardPropertyURN.POSITION.value)
        self.position_history = IntArrayProperty(StandardPropertyURN.POSITION_HISTORY.value)
        self.direction = IntProperty(StandardPropertyURN.DIRECTION.value)
        self.stamina = IntProperty(StandardPropertyURN.STAMINA.value)
        self.hp = IntProperty(StandardPropertyURN.HP.value)
        self.damage = IntProperty(StandardPropertyURN.DAMAGE.value)
        self.buriedness = IntProperty(StandardPropertyURN.BURIEDNESS.value)

        self.register_properties([self.x, self.y, self.travel_distance, self.position, self.position_history])
        self.register_properties([self.direction, self.stamina, self.hp, self.damage, self.buriedness])

    def get_position(self):
        return self.position.get_value()

    def get_location(self, world_model):
        if self.x.is_defined() and self.y.is_defined():
            return self.x.get_value(), self.y.get_value()
        if self.position.is_defined():
            pos_entity = world_model.get_entity(self.get_position())
            return pos_entity.get_location(world_model)
        return None, None

    def __str__(self):
        return str(self.position.get_value())
    
    def set_entity(self, properties):
        for key, values in properties.items():
            _type = StandardPropertyURN.from_string( key )
            
            if _type == StandardPropertyURN.X.name:
                self.x.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.Y.name:
                self.y.set_value(values[0].valueInt)
            
            elif _type == StandardPropertyURN.POSITION.name:
                self.position_history.set_value(values[0].valueInt)
            
            elif _type == StandardPropertyURN.POSITION_HISTORY.name:
                self.position_history.set_value(values[0].valueInt)#todo

            elif _type == StandardPropertyURN.DIRECTION.name:
                self.direction.set_value(values[0].valueInt)
            
            elif _type == StandardPropertyURN.STAMINA.name:
                self.stamina.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.HP.name:
                self.hp.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.DAMAGE.name:
                self.damage.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.BURIEDNESS.name:
                self.buriedness.set_value(values[0].valueInt)
            
            elif _type == StandardPropertyURN.TRAVEL_DISTANCE.name:
                self.travel_distance.set_value(values[0].valueInt)
