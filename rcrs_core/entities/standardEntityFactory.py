from rcrs_core.entities.building import Building
from rcrs_core.entities.road import Road
from rcrs_core.entities.blockade import Blockade
from rcrs_core.entities.refuge import Refuge
from rcrs_core.entities.policeForce import PoliceForceEntity
from rcrs_core.entities.policeOffice import PoliceOfficeEntity
from rcrs_core.entities.ambulanceTeam import AmbulanceTeamEntity
from rcrs_core.entities.ambulanceCenter import AmbulanceCentreEntity
from rcrs_core.entities.fireBrigade import FireBrigadeEntity
from rcrs_core.entities.fireStation import FireStationEntity
from rcrs_core.entities.civilian import Civilian
from rcrs_core.entities.hydrant import Hydrant
from rcrs_core.entities.gassStation import GasStation
from rcrs_core.connection import URN



class StandardEntityFactory:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        pass

    def make_entity(urn, id):
        if urn == URN.Entity.BUILDING:
            return Building(id)
        elif urn == URN.Entity.REFUGE:
            return Refuge(id)
        elif urn == URN.Entity.ROAD:
            return Road(id)
        elif urn == URN.Entity.BLOCKADE:
            return Blockade(id)
        elif urn == URN.Entity.POLICE_FORCE:
            return PoliceForceEntity(id)
        elif urn == URN.Entity.POLICE_OFFICE:
            return PoliceOfficeEntity(id)
        elif urn == URN.Entity.AMBULANCE_TEAM:
            return AmbulanceTeamEntity(id)
        elif urn == URN.Entity.AMBULANCE_CENTRE:
            return AmbulanceCentreEntity(id)
        elif urn == URN.Entity.FIRE_BRIGADE:
            return FireBrigadeEntity(id)
        elif urn == URN.Entity.FIRE_STATION:
            return FireStationEntity(id)
        elif urn == URN.Entity.CIVILIAN:
            return Civilian(id)
        elif urn == URN.Entity.HYDRANT:
            return Hydrant(id)
        elif urn == URN.Entity.GAS_STATION:
            return GasStation(id)

        return None
