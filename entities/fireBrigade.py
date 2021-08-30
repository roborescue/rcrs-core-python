from standardPropertyURN import StandardPropertyURN
from entities.policeForce import PoliceForceEntity
from standardEntityURN import StandardEntityURN
from entities.human import Human
from property import IntProperty

class FireBrigadeEntity(Human):
    urn = StandardEntityURN.FIRE_BRIGADE.value

    def __init__(self, entity_id):
        Human.__init__(self, entity_id)
        self.water = IntProperty(StandardPropertyURN.WATER_QUANTITY)
        
        self.register_properties([self.water])

    def set_entity(self, properties):
        for key, values in properties.items():
            _type = StandardPropertyURN.from_string( key )
            
            if _type == StandardPropertyURN.WATER_QUANTITY.name:
                Human.set_entity(properties)
                self.water.set_value(values[0].valueInt)
