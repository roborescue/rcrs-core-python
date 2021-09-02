from entities.edge import Edge
from entities.area import Area

from entities.standardEntityURN import StandardEntityURN
from properties.standardPropertyURN import StandardPropertyURN
from properties.intProperty import IntProperty


class Building(Area):
    urn = StandardEntityURN.BUILDING.value

    def __init__(self, entity_id):
        Area.__init__(self, entity_id)
        self.floors = IntProperty(StandardPropertyURN.FLOORS.value)
        self.ignition = IntProperty(StandardPropertyURN.IGNITION.value)
        self.fieryness = IntProperty(StandardPropertyURN.FIERYNESS.value)
        self.brokenness = IntProperty(StandardPropertyURN.BROKENNESS.value)
        self.building_code = IntProperty(
            StandardPropertyURN.BUILDING_CODE.value)
        self.attributes = IntProperty(
            StandardPropertyURN.BUILDING_ATTRIBUTES.value)
        self.ground_area = IntProperty(
            StandardPropertyURN.BUILDING_AREA_GROUND.value)
        self.total_area = IntProperty(
            StandardPropertyURN.BUILDING_AREA_TOTAL.value)
        self.temperature = IntProperty(StandardPropertyURN.TEMPERATURE.value)
        self.importance = IntProperty(StandardPropertyURN.IMPORTANCE.value)

        self.register_properties(
            [self.floors, self.ignition, self.fieryness, self.brokenness, self.building_code])
        self.register_properties(
            [self.attributes, self.ground_area, self.total_area, self.temperature, self.importance])

    def is__fiery(self):
        fieryness_value = self.fieryness.get_value()
        # HEATING:1 BURNING:2 INFERNO:3
        if fieryness_value == 1 or fieryness_value == 2 or fieryness_value == 3:
            return True
        return False

    def set_entity(self, properties):
        for key, values in properties.items():
            _type = StandardPropertyURN.from_string(key)

            if _type == StandardPropertyURN.X.name:
                self.x.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.Y.name:
                self.y.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.EDGES.name:
                egdes_list = []
                for edges in values[0].matrixInt.values:
                    edge = Edge(
                        edges.values[0], edges.values[1], edges.values[2], edges.values[3], edges.values[4])
                    egdes_list.append(edge)
                self.edges.set_value(egdes_list)

            elif _type == StandardPropertyURN.BLOCKADES.name:
                print(values)

            elif _type == StandardPropertyURN.FLOORS.name:
                self.floors.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.IGNITION.name:
                self.ignition.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.FIERYNESS.name:
                self.fieryness.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.BROKENNESS.name:
                self.brokenness.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.BUILDING_CODE.name:
                self.building_code.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.BUILDING_ATTRIBUTES.name:
                self.attributes.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.BUILDING_AREA_GROUND.name:
                self.ground_area.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.BUILDING_AREA_TOTAL.name:
                self.total_area.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.TEMPERATURE.name:
                self.temperature.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.IMPORTANCE.name:
                self.importance.set_value(values[0].valueInt)

    def copy_impl(self):
        return Building(self.get_id())

    def get_entity_name(self):
        return "Building"

    def get_property(self, urn):
        _type = StandardPropertyURN.from_string(urn)

        if(_type == StandardPropertyURN.FLOORS.value):
            return self.floors
        elif(_type == StandardPropertyURN.IGNITION.value):
            return self.ignition
        elif(_type == StandardPropertyURN.FIERYNESS.value):
            return self.fieryness
        elif(_type == StandardPropertyURN.BROKENNESS.value):
            return self.brokenness
        elif(_type == StandardPropertyURN.BUILDING_CODE.value):
            return self.building_code
        elif(_type == StandardPropertyURN.BUILDING_ATTRIBUTES.value):
            return self.attributes
        elif(_type == StandardPropertyURN.BUILDING_AREA_GROUND.value):
            return self.ground_area
        elif(_type == StandardPropertyURN.BUILDING_AREA_TOTAL.value):
            return self.total_area
        elif(_type == StandardPropertyURN.TEMPERATURE.value):
            return self.temperature
        elif(_type == StandardPropertyURN.IMPORTANCE.value):
            return self.importance
        else:
            return super().get_property(urn)

    def get_floors_property(self):
        return self.floors

    def get_floors(self):
        return self.floors.get_value()

    def set_floors(self, value):
        self.floors.set_value(value)

    def is_floors_defined(self):
        return self.floors.is_defined()

    def undefine_floors(self):
        self.floors.set_undefined()

    def get_ignition_property(self):
        return self.ignition

    def get_ignition(self):
        return self.ignition.get_value()

    def set_ignition(self, value):
        self.ignition.set_value(value)

    def is_ignition_defined(self):
        return self.ignition.is_defined()

    def undefine_ignition(self):
        self.ignition.set_undefined()

    def get_fieryness_property(self):
        return self.fieryness

    def get_fieryness(self):
        return self.fieryness.get_value()

    def set_fieryness(self, value):
        self.fieryness.set_value(value)

    def is_fieryness_defined(self):
        return self.fieryness.is_defined()

    def undefine_fieryness(self):
        self.fieryness.set_undefined()

    def get_fieryness_enum(self):
        pass  # todo

    def get_brokenness_property(self):
        return self.brokenness

    def get_brokenness(self):
        return self.brokenness.get_value()

    def set_brokenness(self, value):
        self.brokenness.set_value(value)

    def is_brokenness_defined(self):
        return self.brokenness.is_defined()

    def undefine_brokenness(self):
        self.brokenness.set_undefined()

    def get_building_code_property(self):
        return self.building_code

    def get_building_code(self):
        return self.building_code.get_value()

    def set_building_code(self, value):
        self.building_code.set_value(value)

    def is_building_code_defined(self):
        return self.building_code.is_defined()

    def undefine_building_code(self):
        self.building_code.set_undefined()

    def get_building_code_enum(self):
        pass  # todo

    def get_attributes_property(self):
        return self.attributes

    def get_attributes(self):
        return self.attributes.get_value()

    def set_attributes(self, value):
        self.attributes.set_value(value)

    def is_attributes_defined(self):
        return self.attributes.is_defined()

    def undefine_attributes(self):
        self.attributes.set_undefined()

    def get_ground_area_property(self):
        return self.ground_area

    def get_ground_area(self):
        return self.ground_area.get_value()

    def set_ground_area(self, value):
        self.ground_area.set_value(value)

    def is_ground_area_defined(self):
        return self.ground_area.is_defined()

    def undefine_ground_area(self):
        self.ground_area.set_undefined()

    def get_total_area_property(self):
        return self.total_area

    def get_total_area(self):
        return self.total_area.get_value()

    def set_total_area(self, value):
        self.total_area.set_value(value)

    def is_total_area_defined(self):
        return self.total_area.is_defined()

    def undefine_total_area(self):
        self.total_area.set_undefined()

    def get_temperature_property(self):
        return self.temperature

    def get_temperature(self):
        return self.temperature.get_value()

    def set_temperature(self, value):
        self.temperature.set_value(value)

    def is_temperature_defined(self):
        return self.temperature.is_defined()

    def undefine_temperature(self):
        self.temperature.set_undefined()

    def get_importance_property(self):
        return self.importance

    def get_importance(self):
        return self.importance.get_value()

    def set_importance(self, value):
        self.importance.set_value(value)

    def is_importance_defined(self):
        return self.importance.is_defined()

    def undefine_importance(self):
        self.importance.set_undefined()
