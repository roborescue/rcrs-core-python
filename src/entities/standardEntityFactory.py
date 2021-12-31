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
from connection import URN



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
