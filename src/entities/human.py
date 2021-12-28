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

    #TODO
    def get_location(self, world_model):
        if self.x.defined and self.y.defined:
            return self.x.get_value(), self.y.get_value()
        if self.position.defined:
            pos_entity = world_model.get_entity(self.get_position())
            return pos_entity.get_location(world_model)
        return None, None

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

    def get_x_property(self):
        return self.x

    def get_x(self) -> int:
        return self.x.get_value()

    def set_x(self, value) -> None:
        self.x.set_value(value)

    def is_x_defined(self):
        return self.x.defined

    def undefine_x(self):
        self.x.set_undefined()

    def get_y_property(self):
        return self.y

    def get_y(self):
        return self.y.get_value()

    def set_y(self, value):
        self.y.set_value(value)

    def is_y_defined(self):
        return self.y.defined

    def undefine_y(self):
        self.y.set_undefined()

    def get_position_property(self):
        return self.position

    def get_position(self):
        return self.position.get_value()

    def set_position(self, value):
        self.position.set_value(value)

    def is_position_defined(self):
        return self.position.defined

    def undefine_position(self):
        self.position.set_undefined()

    def get_position_history_property(self):
        return self.position_history

    def get_position_history(self):
        return self.position_history.get_value()

    def set_position_history(self, value):
        self.position_history.set_value(value)

    def is_position_history_defined(self):
        return self.position_history.defined

    def undefine_position_history(self):
        self.position_history.set_undefined()

    def get_direction_property(self):
        return self.direction

    def get_direction(self):
        return self.direction.get_value()

    def set_direction(self, value):
        self.direction.set_value(value)

    def is_direction_defined(self):
        return self.direction.defined

    def undefine_direction(self):
        self.direction.set_undefined()

    def get_stamina_property(self):
        return self.stamina

    def get_stamina(self):
        return self.stamina.get_value()

    def set_stamina(self, value):
        self.stamina.set_value(value)

    def is_stamina_defined(self):
        return self.stamina.defined

    def undefine_stamina(self):
        self.stamina.set_undefined()

    def get_hp_property(self):
        return self.hp

    def get_hp(self):
        return self.hp.get_value()

    def set_hp(self, value):
        self.hp.set_value(value)

    def is_hp_defined(self):
        return self.hp.defined

    def undefine_hp(self):
        self.hp.set_undefined()

    def get_damage_property(self):
        return self.damage

    def get_damage(self):
        return self.damage.get_value()

    def set_damage(self, value):
        self.damage.set_value(value)

    def is_damage_defined(self):
        return self.damage.defined

    def undefine_damage(self):
        self.damage.set_undefined()

    def get_buriedness_property(self):
        return self.buriedness

    def get_buriedness(self):
        return self.buriedness.get_value()

    def set_buriedness(self, value):
        self.buriedness.set_value(value)

    def is_buriedness_defined(self):
        return self.buriedness.defined

    def undefine_buriedness(self):
        self.buriedness.set_undefined()

    def get_travel_distance_property(self):
        return self.travel_distance

    def get_travel_distance(self):
        return self.travel_distance.get_value()

    def set_travel_distance(self, value):
        self.travel_distance.set_value(value)

    def is_travel_distance_defined(self):
        return self.travel_distance.defined

    def undefine_travel_distance(self):
        self.travel_distance.set_undefined()
