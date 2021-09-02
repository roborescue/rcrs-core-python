from enum import Enum
from constants.constants import PROPERTY_URN_PREFIX


class StandardPropertyURN(Enum):

    START_TIME = PROPERTY_URN_PREFIX + "starttime"
    LONGITUDE = PROPERTY_URN_PREFIX + "longitude"
    LATITUDE = PROPERTY_URN_PREFIX + "latitude"
    WIND_FORCE = PROPERTY_URN_PREFIX + "windforce"
    WIND_DIRECTION = PROPERTY_URN_PREFIX + "winddirection"

    X = PROPERTY_URN_PREFIX + "x"
    Y = PROPERTY_URN_PREFIX + "y"

    BLOCKADES = PROPERTY_URN_PREFIX + "blockades"
    REPAIR_COST = PROPERTY_URN_PREFIX + "repaircost"

    FLOORS = PROPERTY_URN_PREFIX + "floors"
    BUILDING_ATTRIBUTES = PROPERTY_URN_PREFIX + "buildingattributes"
    IGNITION = PROPERTY_URN_PREFIX + "ignition"
    FIERYNESS = PROPERTY_URN_PREFIX + "fieryness"
    BROKENNESS = PROPERTY_URN_PREFIX + "brokenness"
    BUILDING_CODE = PROPERTY_URN_PREFIX + "buildingcode"
    BUILDING_AREA_GROUND = PROPERTY_URN_PREFIX + "buildingareaground"
    BUILDING_AREA_TOTAL = PROPERTY_URN_PREFIX + "buildingareatotal"
    APEXES = PROPERTY_URN_PREFIX + "apexes"
    EDGES = PROPERTY_URN_PREFIX + "edges"

    POSITION = PROPERTY_URN_PREFIX + "position"
    DIRECTION = PROPERTY_URN_PREFIX + "direction"
    POSITION_HISTORY = PROPERTY_URN_PREFIX + "positionhistory"
    STAMINA = PROPERTY_URN_PREFIX + "stamina"
    HP = PROPERTY_URN_PREFIX + "hp"
    DAMAGE = PROPERTY_URN_PREFIX + "damage"
    BURIEDNESS = PROPERTY_URN_PREFIX + "buriedness"
    TRAVEL_DISTANCE = PROPERTY_URN_PREFIX + "traveldistance"
    WATER_QUANTITY = PROPERTY_URN_PREFIX + "waterquantity"

    TEMPERATURE = PROPERTY_URN_PREFIX + "temperature"
    IMPORTANCE = PROPERTY_URN_PREFIX + "importance"

    CAPACITY = PROPERTY_URN_PREFIX + "capacity"
    BEDCAPACITY = PROPERTY_URN_PREFIX + "bedCapacity"
    OCCUPIEDBEDS = PROPERTY_URN_PREFIX + "occupiedBeds"
    REFILLCAPACITY = PROPERTY_URN_PREFIX + "refillCapacity"
    WAITINGLISTSIZE = PROPERTY_URN_PREFIX + "waitingListSize"

    def from_id(index):
        return list(StandardPropertyURN)[index].value

    def from_string(urn):
        for key in StandardPropertyURN:
            if key.value == urn:
                return key.name
        return ''


if __name__ == '__main__':
    # for key in StandardPropertyURN:
    #     print(key.name, key.value)

    print(StandardPropertyURN.from_string('property:buildingareatotal'))
