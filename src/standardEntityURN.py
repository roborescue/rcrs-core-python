from enum import Enum
from typing import List
from constants import ENTITY_URN_PREFIX

class StandardEntityURN(Enum):

    WORLD = ENTITY_URN_PREFIX + "world" 
    ROAD = ENTITY_URN_PREFIX + "road" 
    BLOCKADE = ENTITY_URN_PREFIX + "blockade" 
    BUILDING = ENTITY_URN_PREFIX + "building" 
    REFUGE = ENTITY_URN_PREFIX + "refuge" 
    HYDRANT = ENTITY_URN_PREFIX + "hydrant" 
    GAS_STATION = ENTITY_URN_PREFIX + "gasstation" 
    FIRE_STATION = ENTITY_URN_PREFIX + "firestation" 
    AMBULANCE_CENTRE = ENTITY_URN_PREFIX + "ambulancecentre"
    POLICE_OFFICE = ENTITY_URN_PREFIX + "policeoffice" 
    CIVILIAN = ENTITY_URN_PREFIX + "civilian" 
    FIRE_BRIGADE = ENTITY_URN_PREFIX + "firebrigade" 
    AMBULANCE_TEAM = ENTITY_URN_PREFIX + "ambulanceteam" 
    POLICE_FORCE = ENTITY_URN_PREFIX + "policeforce" 

    def from_id(index):
        return list(StandardEntityURN)[index].value
    
    def from_string(urn):
        for key in StandardEntityURN:
            if key.name == urn:
                return key.value
        return ''


if __name__ == '__main__':
    print(StandardEntityURN.from_string('WORLD'))