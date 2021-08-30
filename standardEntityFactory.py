from standardEntityURN import StandardEntityURN
from entities.building import Building
from entities.road import Road
from entities.blockade import Blockade
from entities.refuge import Refuge
from entities.policeForce import PoliceForceEntity
from entities.policeOffice import PoliceOfficeEntity
from entities.ambulanceTeam import AmbulanceTeamEntity
from entities.ambulanceCenter import AmbulanceCentreEntity
from entities.fireBrigade import FireBrigadeEntity
from entities.fireStation import FireStationEntity
from entities.civilian import Civilian
from entities.hydrant import Hydrant
from entities.gassStation import GasStation



class StandardEntityFactory:
    def __init__(self) -> None:
        pass

    def make_entity(urn, id):

        if urn == StandardEntityURN.BUILDING.value:
            return Building(id)
        if urn == StandardEntityURN.REFUGE.value:
            return Refuge(id)
        if urn == StandardEntityURN.ROAD.value:
            return Road(id)
        if urn == StandardEntityURN.BLOCKADE.value:
            return Blockade(id)

        if urn == StandardEntityURN.POLICE_FORCE.value:
            return PoliceForceEntity(id)
        if urn == StandardEntityURN.POLICE_OFFICE.value:
            return PoliceOfficeEntity(id)
        if urn == StandardEntityURN.AMBULANCE_TEAM.value:
            return AmbulanceTeamEntity(id)
        if urn == StandardEntityURN.AMBULANCE_CENTRE.value:
            return AmbulanceCentreEntity(id)
        if urn == StandardEntityURN.FIRE_BRIGADE.value:
            return FireBrigadeEntity(id)
        if urn == StandardEntityURN.FIRE_STATION.value:
            return FireStationEntity(id)
        if urn == StandardEntityURN.CIVILIAN.value:
            return Civilian(id)
        
        
        if urn == StandardEntityURN.HYDRANT.value:
            return Hydrant(id)
        if urn == StandardEntityURN.GAS_STATION.value:
            return GasStation(id)

