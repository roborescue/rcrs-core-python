from connection import URN
from properties.intProperty import IntProperty
from properties.intArrayProperty import IntArrayProperty
from properties.booleanProperty import BooleanProperty
from properties.edgeListProperty import EdgeListProperty
from properties.entityIDListProperty import EntityIDListProperty
from properties.entityIDProperty import EntityIDProperty


class StandardPropertyFactory:
    def __init__(self) -> None:
        pass

    def make_property(urn):
        if urn == URN.Property.START_TIME:
            return IntProperty(urn)
        if urn == URN.Property.LONGITUDE:
            return IntProperty(urn)
        if urn == URN.Property.LATITUDE:
            return IntProperty(urn)
        if urn == URN.Property.WIND_FORCE:
            return IntProperty(urn)
        if urn == URN.Property.WIND_DIRECTION:
            return IntProperty(urn)
        if urn == URN.Property.X:
            return IntProperty(urn)
        if urn == URN.Property.Y:
            return IntProperty(urn)
        if urn == URN.Property.FLOORS:
            return IntProperty(urn)
        if urn == URN.Property.BUILDING_ATTRIBUTES:
            return IntProperty(urn)
        if urn == URN.Property.FIERYNESS:
            return IntProperty(urn)
        if urn == URN.Property.BROKENNESS:
            return IntProperty(urn)
        if urn == URN.Property.BUILDING_CODE:
            return IntProperty(urn)
        if urn == URN.Property.BUILDING_AREA_GROUND:
            return IntProperty(urn)
        if urn == URN.Property.BUILDING_AREA_TOTAL:
            return IntProperty(urn)
        if urn == URN.Property.DIRECTION:
            return IntProperty(urn)
        if urn == URN.Property.STAMINA:
            return IntProperty(urn)
        if urn == URN.Property.HP:
            return IntProperty(urn)
        if urn == URN.Property.DAMAGE:
            return IntProperty(urn)
        if urn == URN.Property.BURIEDNESS:
            return IntProperty(urn)
        if urn == URN.Property.WATER_QUANTITY:
            return IntProperty(urn)
        if urn == URN.Property.TEMPERATURE:
            return IntProperty(urn)
        if urn == URN.Property.IMPORTANCE:
            return IntProperty(urn)
        if urn == URN.Property.TRAVEL_DISTANCE:
            return IntProperty(urn)
        if urn == URN.Property.REPAIR_COST:
            return IntProperty(urn)
        if urn == URN.Property.APEXES:
            return IntArrayProperty(urn)
        if urn == URN.Property.POSITION_HISTORY:
            return IntArrayProperty(urn)
        if urn == URN.Property.IGNITION:
            return BooleanProperty(urn)
        if urn == URN.Property.POSITION:
            return EntityIDProperty(urn)
        if urn == URN.Property.BLOCKADES:
            return EntityIDListProperty(urn)
        if urn == URN.Property.EDGES:
            return EdgeListProperty(urn)
        if urn == URN.Property.CAPACITY:
            return IntProperty(urn)
        if urn == URN.Property.BEDCAPACITY:
            return IntProperty(urn)
        if urn == URN.Property.OCCUPIEDBEDS:
            return IntProperty(urn)
        if urn == URN.Property.REFILLCAPACITY:
            return IntProperty(urn)
        if urn == URN.Property.WAITINGLISTSIZE:
            return IntProperty(urn)
        return None
