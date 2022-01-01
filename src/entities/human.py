from connection import URN
from entities.entity import Entity
from properties.intProperty import IntProperty
from properties.entityIDProperty import EntityIDProperty
from properties.intArrayProperty import IntArrayProperty

class Human(Entity):
    def __init__(self, entity_id):
        super().__init__(entity_id)
        self.travel_distance = IntProperty(URN.Property.TRAVEL_DISTANCE)
        self.position = EntityIDProperty(URN.Property.POSITION)
        self.position_history = IntArrayProperty(URN.Property.POSITION_HISTORY)
        self.direction = IntProperty(URN.Property.DIRECTION)
        self.stamina = IntProperty(URN.Property.STAMINA)
        self.hp = IntProperty(URN.Property.HP)
        self.damage = IntProperty(URN.Property.DAMAGE)
        self.buriedness = IntProperty(URN.Property.BURIEDNESS)

        self.register_properties(
            [self.travel_distance, self.position, self.position_history])
        self.register_properties(
            [self.direction, self.stamina, self.hp, self.damage, self.buriedness])

    def get_location(self):
        return self.x.value, self.y.value

    def set_entity(self, properties: dict):
        super().set_entity(properties)
        for key, values in properties.items():

            if key == URN.Property.POSITION:
                self.position.set_value(values)

            elif key == URN.Property.POSITION_HISTORY:
                self.position_history.set_value(values)

            elif key == URN.Property.DIRECTION:
                self.direction.set_value(values)

            elif key == URN.Property.STAMINA:
                self.stamina.set_value(values)

            elif key == URN.Property.HP:
                self.hp.set_value(values)

            elif key == URN.Property.DAMAGE:
                self.damage.set_value(values)

            elif key == URN.Property.BURIEDNESS:
                self.buriedness.set_value(values)

            elif key == URN.Property.TRAVEL_DISTANCE:
                self.travel_distance.set_value(values)

    def get_property(self, urn):
        if(urn == URN.Property.POSITION):
            return self.position
        elif(urn == URN.Property.POSITION_HISTORY):
            return self.position_history
        elif(urn == URN.Property.DIRECTION):
            return self.direction
        elif(urn == URN.Property.STAMINA):
            return self.stamina
        elif(urn == URN.Property.HP):
            return self.hp
        elif(urn == URN.Property.X):
            return self.x
        elif(urn == URN.Property.Y):
            return self.y
        elif(urn == URN.Property.DAMAGE):
            return self.damage
        elif(urn == URN.Property.BURIEDNESS):
            return self.buriedness
        elif(urn == URN.Property.TRAVEL_DISTANCE):
            return self.travel_distance
        else:
            return super().get_property(urn)