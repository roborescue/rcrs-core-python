from properties.standardPropertyURN import StandardPropertyURN
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

        if urn == StandardPropertyURN.START_TIME.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.LONGITUDE.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.LATITUDE.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.WIND_FORCE.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.WIND_DIRECTION.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.X.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.Y.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.FLOORS.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.BUILDING_ATTRIBUTES.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.FIERYNESS.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.BROKENNESS.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.BUILDING_CODE.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.BUILDING_AREA_GROUND.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.BUILDING_AREA_TOTAL.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.DIRECTION.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.STAMINA.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.HP.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.DAMAGE.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.BURIEDNESS.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.WATER_QUANTITY.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.TEMPERATURE.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.IMPORTANCE.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.TRAVEL_DISTANCE.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.REPAIR_COST.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.APEXES.value:
            return IntArrayProperty(urn)
        if urn == StandardPropertyURN.POSITION_HISTORY.value:
            return IntArrayProperty(urn)
        if urn == StandardPropertyURN.IGNITION.value:
            return BooleanProperty(urn)
        if urn == StandardPropertyURN.POSITION.value:
            return EntityIDProperty(urn)
        if urn == StandardPropertyURN.BLOCKADES.value:
            return EntityIDListProperty(urn)
        if urn == StandardPropertyURN.EDGES.value:
            return EdgeListProperty(urn)
        if urn == StandardPropertyURN.CAPACITY.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.BEDCAPACITY.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.OCCUPIEDBEDS.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.REFILLCAPACITY.value:
            return IntProperty(urn)
        if urn == StandardPropertyURN.WAITINGLISTSIZE.value:
            return IntProperty(urn)

        return None
