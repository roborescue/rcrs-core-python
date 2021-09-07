from entities.standardEntityURN import StandardEntityURN
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
        elif urn == StandardEntityURN.REFUGE.value:
            return Refuge(id)
        elif urn == StandardEntityURN.ROAD.value:
            return Road(id)
        elif urn == StandardEntityURN.BLOCKADE.value:
            return Blockade(id)
        elif urn == StandardEntityURN.POLICE_FORCE.value:
            return PoliceForceEntity(id)
        elif urn == StandardEntityURN.POLICE_OFFICE.value:
            return PoliceOfficeEntity(id)
        elif urn == StandardEntityURN.AMBULANCE_TEAM.value:
            return AmbulanceTeamEntity(id)
        elif urn == StandardEntityURN.AMBULANCE_CENTRE.value:
            return AmbulanceCentreEntity(id)
        elif urn == StandardEntityURN.FIRE_BRIGADE.value:
            return FireBrigadeEntity(id)
        elif urn == StandardEntityURN.FIRE_STATION.value:
            return FireStationEntity(id)
        elif urn == StandardEntityURN.CIVILIAN.value:
            return Civilian(id)
        elif urn == StandardEntityURN.HYDRANT.value:
            return Hydrant(id)
        elif urn == StandardEntityURN.GAS_STATION.value:
            return GasStation(id)

        return None
