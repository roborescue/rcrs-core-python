from agents.agent import Agent
from log.logger import Logger
from connection import URN


class AmbulanceCenterAgent(Agent):
    def __init__(self, pre):
        Agent.__init__(self, pre)
        self.name = 'AmbulanceCenterAgent'

    def get_requested_entities(self):
        return [URN.Entity.AMBULANCE_CENTRE]

    def think(self, timestep, change_set, heard):
        pass
