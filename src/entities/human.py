from properties.standardPropertyURN import StandardPropertyURN
from entities.standardEntityURN import StandardEntityURN
from entities.entity import Entity
from properties.intProperty import IntProperty
from properties.entityIDProperty import EntityIDProperty
from properties.intArrayProperty import IntArrayProperty


class Human(Entity):
    def __init__(self, entity_id):
        Entity.__init__(self, entity_id)
        self.x = IntProperty(StandardPropertyURN.X.value)
        self.y = IntProperty(StandardPropertyURN.Y.value)
        self.travel_distance = IntProperty(
            StandardPropertyURN.TRAVEL_DISTANCE.value)
        self.position = EntityIDProperty(StandardPropertyURN.POSITION.value)
        self.position_history = IntArrayProperty(
            StandardPropertyURN.POSITION_HISTORY.value)
        self.direction = IntProperty(StandardPropertyURN.DIRECTION.value)
        self.stamina = IntProperty(StandardPropertyURN.STAMINA.value)
        self.hp = IntProperty(StandardPropertyURN.HP.value)
        self.damage = IntProperty(StandardPropertyURN.DAMAGE.value)
        self.buriedness = IntProperty(StandardPropertyURN.BURIEDNESS.value)

        self.register_properties(
            [self.x, self.y, self.travel_distance, self.position, self.position_history])
        self.register_properties(
            [self.direction, self.stamina, self.hp, self.damage, self.buriedness])

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
            _type = StandardPropertyURN.from_string(key)

            if _type == StandardPropertyURN.X.name:
                self.x.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.Y.name:
                self.y.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.POSITION.name:
                self.position.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.POSITION_HISTORY.name:
                _values = []
                for position in values[0].listInt.values:
                    _values.append(position)

                self.position_history.set_value(_values)

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

    def get_property(self, urn):
        _type = StandardPropertyURN.from_string(urn)

        if(_type == StandardPropertyURN.POSITION.value):
            return self.position
        elif(_type == StandardPropertyURN.POSITION_HISTORY.value):
            return self.position_history
        elif(_type == StandardPropertyURN.DIRECTION.value):
            return self.direction
        elif(_type == StandardPropertyURN.STAMINA.value):
            return self.stamina
        elif(_type == StandardPropertyURN.HP.value):
            return self.hp
        elif(_type == StandardPropertyURN.X.value):
            return self.x
        elif(_type == StandardPropertyURN.Y.value):
            return self.y
        elif(_type == StandardPropertyURN.DAMAGE.value):
            return self.damage
        elif(_type == StandardPropertyURN.BURIEDNESS.value):
            return self.buriedness
        elif(_type == StandardPropertyURN.TRAVEL_DISTANCE.value):
            return self.travel_distance
        else:
            return super().get_property(urn)

    def get_x_property(self):
        return self.x

    def get_x(self):
        return self.x.get_value()

    def set_x(self, value):
        self.x.set_value(value)

    def is_x_defined(self):
        return self.x.is_defined()

    def undefine_x(self):
        self.x.set_undefined()

    def get_y_property(self):
        return self.y

    def get_y(self):
        return self.y.get_value()

    def set_y(self, value):
        self.y.set_value(value)

    def is_y_defined(self):
        return self.y.is_defined()

    def undefine_y(self):
        self.y.set_undefined()

    def get_position_property(self):
        return self.position

    def get_position(self):
        return self.position.get_value()

    def set_position(self, value):
        self.position.set_value(value)

    def is_position_defined(self):
        return self.position.is_defined()

    def undefine_position(self):
        self.position.set_undefined()

    def get_position_history_property(self):
        return self.position_history

    def get_position_history(self):
        return self.position_history.get_value()

    def set_position_history(self, value):
        self.position_history.set_value(value)

    def is_position_history_defined(self):
        return self.position_history.is_defined()

    def undefine_position_history(self):
        self.position_history.set_undefined()

    def get_direction_property(self):
        return self.direction

    def get_direction(self):
        return self.direction.get_value()

    def set_direction(self, value):
        self.direction.set_value(value)

    def is_direction_defined(self):
        return self.direction.is_defined()

    def undefine_direction(self):
        self.direction.set_undefined()

    def get_stamina_property(self):
        return self.stamina

    def get_stamina(self):
        return self.stamina.get_value()

    def set_stamina(self, value):
        self.stamina.set_value(value)

    def is_stamina_defined(self):
        return self.stamina.is_defined()

    def undefine_stamina(self):
        self.stamina.set_undefined()

    def get_hp_property(self):
        return self.hp

    def get_hp(self):
        return self.hp.get_value()

    def set_hp(self, value):
        self.hp.set_value(value)

    def is_hp_defined(self):
        return self.hp.is_defined()

    def undefine_hp(self):
        self.hp.set_undefined()

    def get_damage_property(self):
        return self.damage

    def get_damage(self):
        return self.damage.get_value()

    def set_damage(self, value):
        self.damage.set_value(value)

    def is_damage_defined(self):
        return self.damage.is_defined()

    def undefine_damage(self):
        self.damage.set_undefined()

    def get_buriedness_property(self):
        return self.buriedness

    def get_buriedness(self):
        return self.buriedness.get_value()

    def set_buriedness(self, value):
        self.buriedness.set_value(value)

    def is_buriedness_defined(self):
        return self.buriedness.is_defined()

    def undefine_buriedness(self):
        self.buriedness.set_undefined()

    def get_travel_distance_property(self):
        return self.travel_distance

    def get_travel_distance(self):
        return self.travel_distance.get_value()

    def set_travel_distance(self, value):
        self.travel_distance.set_value(value)

    def is_travel_distance_defined(self):
        return self.travel_distance.is_defined()

    def undefine_travel_distance(self):
        self.travel_distance.set_undefined()
