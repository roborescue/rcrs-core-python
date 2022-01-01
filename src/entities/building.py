from connection import URN
from entities.edge import Edge
from entities.area import Area
from properties.intProperty import IntProperty



class Building(Area):
    urn = URN.Entity.BUILDING

    def __init__(self, entity_id):
        super().__init__(entity_id)
        self.floors = IntProperty(URN.Property.FLOORS)
        self.ignition = IntProperty(URN.Property.IGNITION)
        self.fieryness = IntProperty(URN.Property.FIERYNESS)
        self.brokenness = IntProperty(URN.Property.BROKENNESS)
        self.building_code = IntProperty(URN.Property.BUILDING_CODE)
        self.attributes = IntProperty(URN.Property.BUILDING_ATTRIBUTES)
        self.ground_area = IntProperty(URN.Property.BUILDING_AREA_GROUND)
        self.total_area = IntProperty(URN.Property.BUILDING_AREA_TOTAL)
        self.temperature = IntProperty(URN.Property.TEMPERATURE)
        self.importance = IntProperty(URN.Property.IMPORTANCE)
        self.capacity = IntProperty(URN.Property.CAPACITY)

        self.register_properties(
            [self.floors, self.ignition, self.fieryness, self.brokenness])
        self.register_properties(
            [self.attributes, self.ground_area, self.total_area])
        self.register_properties(
            [self.capacity, self.temperature, self.importance, self.building_code])

    def is__fiery(self):
        fieryness_value = self.fieryness.value
        # HEATING:1 BURNING:2 INFERNO:3
        if fieryness_value == 1 or fieryness_value == 2 or fieryness_value == 3:
            return True
        return False

    def set_entity(self, properties):
        super().set_entity(properties)

        for key, values in properties.items():
            if key == URN.Property.FLOORS:
                self.floors.set_value(values)

            elif key == URN.Property.IGNITION:
                self.ignition.set_value(values)

            elif key == URN.Property.FIERYNESS:
                self.fieryness.set_value(values)

            elif key == URN.Property.BROKENNESS:
                self.brokenness.set_value(values)

            elif key == URN.Property.BUILDING_CODE:
                self.building_code.set_value(values)

            elif key == URN.Property.BUILDING_ATTRIBUTES:
                self.attributes.set_value(values)

            elif key == URN.Property.BUILDING_AREA_GROUND:
                self.ground_area.set_value(values)

            elif key == URN.Property.BUILDING_AREA_TOTAL:
                self.total_area.set_value(values)

            elif key == URN.Property.TEMPERATURE:
                self.temperature.set_value(values)

            elif key == URN.Property.IMPORTANCE:
                self.importance.set_value(values)

    def get_property(self, urn):
        if(urn == URN.Property.FLOORS):
            return self.floors
        elif(urn == URN.Property.IGNITION):
            return self.ignition
        elif(urn == URN.Property.FIERYNESS):
            return self.fieryness
        elif(urn == URN.Property.BROKENNESS):
            return self.brokenness
        elif(urn == URN.Property.BUILDING_CODE):
            return self.building_code
        elif(urn == URN.Property.BUILDING_ATTRIBUTES):
            return self.attributes
        elif(urn == URN.Property.BUILDING_AREA_GROUND):
            return self.ground_area
        elif(urn == URN.Property.BUILDING_AREA_TOTAL):
            return self.total_area
        elif(urn == URN.Property.TEMPERATURE):
            return self.temperature
        elif(urn == URN.Property.IMPORTANCE):
            return self.importance
        else:
            return super().get_property(urn)