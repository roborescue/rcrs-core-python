from entities.entity import Entity
from properties.entityIDProperty import EntityIDProperty
from properties.intArrayProperty import IntArrayProperty
from properties.intProperty import IntProperty
from entities.standardEntityURN import StandardEntityURN
from properties.standardPropertyURN import StandardPropertyURN


class Blockade(Entity):
    urn = StandardEntityURN.BLOCKADE.value

    def __init__(self, entity_id):
        super().__init__(entity_id)
        self.position = EntityIDProperty(StandardPropertyURN.POSITION.value)
        self.apexes = IntArrayProperty(StandardPropertyURN.APEXES.value)
        self.repair_cost = IntProperty(StandardPropertyURN.REPAIR_COST.value)
        self.shape = None

        self.register_properties(
            [self.position, self.apexes, self.repair_cost])

    def get_entity_name(self):
        return "Blockade"

    def set_entity(self, properties):
        super().set_entity(properties)

        for key, values in properties.items():
            _type = StandardPropertyURN.from_string(key)

            if _type == StandardPropertyURN.POSITION.name:
                self.position.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.REPAIR_COST.name:
                self.repair_cost.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.APEXES.name:
                self.apexes.set_value(values[0].listInt.values)

    def copy_impl(self):
        return Blockade(self.get_id())

    def get_property(self, urn):
        _type = StandardPropertyURN.from_string(urn)

        if(_type == StandardPropertyURN.X.value):
            return self.x
        elif(_type == StandardPropertyURN.Y.value):
            return self.y
        elif(_type == StandardPropertyURN.POSITION.value):
            return self.position
        elif(_type == StandardPropertyURN.APEXES.value):
            return self.apexes
        elif(_type == StandardPropertyURN.REPAIR_COST.value):
            return self.repair_cost
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

    def get_apexes_property(self):
        return self.apexes

    def get_apexes(self):
        return self.apexes.get_value()

    def set_apexes(self, value):
        self.apexes.set_value(value)

    def is_apexes_defined(self):
        return self.apexes.is_defined()

    def undefine_apexes(self):
        self.apexes.set_undefined()

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

    def get_repaire_cost_property(self):
        return self.repair_cost

    def get_repaire_cost(self):
        return self.repair_cost.get_value()

    def set_repaire_cost(self, value):
        self.repair_cost.set_value(value)

    def is_repaire_cost_defined(self):
        return self.repair_cost.is_defined()

    def undefine_repaire_cost(self):
        self.repair_cost.set_undefined()

    def get_shape(self):
        return None
