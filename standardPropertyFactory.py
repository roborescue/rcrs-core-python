from standardPropertyURN import StandardPropertyURN
from property import IntProperty
from property import IntArrayProperty
from property import BooleanProperty
from property import EdgeListProperty
from property import EntityIDListProperty
from property import EntityIDProperty

class StandardPropertyFactory:
    def __init__(self) -> None:
        pass

    def make_property(urn):
        # return {
        #     StandardPropertyURN.START_TIME.value: IntProperty(urn),
        #     StandardPropertyURN.LONGITUDE.value: IntProperty(urn),
        #     StandardPropertyURN.LATITUDE.value: IntProperty(urn),
        #     StandardPropertyURN.WIND_FORCE.value: IntProperty(urn),
        #     StandardPropertyURN.WIND_DIRECTION.value: IntProperty(urn),
        #     StandardPropertyURN.X.value: IntProperty(urn),
        #     StandardPropertyURN.Y.value: IntProperty(urn),
        #     StandardPropertyURN.FLOORS.value: IntProperty(urn),
        #     StandardPropertyURN.BUILDING_ATTRIBUTES.value: IntProperty(urn),
        #     StandardPropertyURN.FIERYNESS.value: IntProperty(urn),
        #     StandardPropertyURN.BROKENNESS.value: IntProperty(urn),
        #     StandardPropertyURN.BUILDING_CODE.value: IntProperty(urn),
        #     StandardPropertyURN.BUILDING_AREA_GROUND.value: IntProperty(urn),
        #     StandardPropertyURN.BUILDING_AREA_TOTAL.value: IntProperty(urn),
        #     StandardPropertyURN.DIRECTION.value: IntProperty(urn),
        #     StandardPropertyURN.STAMINA.value: IntProperty(urn),
        #     StandardPropertyURN.HP.value: IntProperty(urn),
        #     StandardPropertyURN.DAMAGE.value: IntProperty(urn),
        #     StandardPropertyURN.BURIEDNESS.value: IntProperty(urn),
        #     StandardPropertyURN.WATER_QUANTITY.value: IntProperty(urn),
        #     StandardPropertyURN.TEMPERATURE.value: IntProperty(urn),
        #     StandardPropertyURN.IMPORTANCE.value: IntProperty(urn),
        #     StandardPropertyURN.TRAVEL_DISTANCE.value: IntProperty(urn),
        #     StandardPropertyURN.REPAIR_COST.value: IntProperty(urn),
        #     StandardPropertyURN.APEXES.value: IntArrayProperty(urn),
        #     StandardPropertyURN.POSITION_HISTORY.value: IntArrayProperty(urn),
        #     StandardPropertyURN.IGNITION.value: BooleanProperty(urn),
        #     StandardPropertyURN.POSITION.value: EntityIDProperty(urn),
        #     StandardPropertyURN.BLOCKADES.value: EntityIDListProperty(urn),
        #     StandardPropertyURN.EDGES.value: EdgeListProperty(urn)
        # }.get(urn, None)

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
        
        return None