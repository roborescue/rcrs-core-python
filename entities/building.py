from entities.edge import Edge
from entities.area import Area

from standardEntityURN import StandardEntityURN
from standardPropertyURN import StandardPropertyURN
from property import IntProperty



class Building(Area):
    urn = StandardEntityURN.BUILDING.value

    def __init__(self, entity_id):
        Area.__init__(self, entity_id)
        self.floors = IntProperty(StandardPropertyURN.FLOORS.value)
        self.ignition = IntProperty(StandardPropertyURN.IGNITION.value)
        self.fieryness = IntProperty(StandardPropertyURN.FIERYNESS.value)
        self.brokenness = IntProperty(StandardPropertyURN.BROKENNESS.value)
        self.building_code = IntProperty(StandardPropertyURN.BUILDING_CODE.value)
        self.attributes = IntProperty(StandardPropertyURN.BUILDING_ATTRIBUTES.value)
        self.ground_area = IntProperty(StandardPropertyURN.BUILDING_AREA_GROUND.value)
        self.total_area = IntProperty(StandardPropertyURN.BUILDING_AREA_TOTAL.value)
        self.temperature = IntProperty(StandardPropertyURN.TEMPERATURE.value)
        self.importance = IntProperty(StandardPropertyURN.IMPORTANCE.value)
        
        self.register_properties([self.floors, self.ignition, self.fieryness, self.brokenness, self.building_code])
        self.register_properties([self.attributes, self.ground_area, self.total_area, self.temperature, self.importance])

    def is__fiery(self):
        fieryness_value = self.fieryness.get_value()
        # HEATING:1 BURNING:2 INFERNO:3
        if fieryness_value == 1 or fieryness_value == 2 or fieryness_value == 3:
            return True
        return False
    
    def set_entity(self, properties):
        for key, values in properties.items():
            _type = StandardPropertyURN.from_string( key )
            
            if _type == StandardPropertyURN.X.name:
                self.x.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.Y.name:
                self.y.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.EDGES.name:
                egdes_list = []
                for edges in values[0].matrixInt.values:
                    edge = Edge(edges.values[0], edges.values[1], edges.values[2], edges.values[3], edges.values[4])
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
