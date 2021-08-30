from connection import Connection
from message import *


class Agent:

    def __init__(self):
        print('agent created .... ')
        self.connection = None
        self.name = ''
        self.connect_request_id = None
        self.world_model = None
        self.config = None
        self.random = None
        self.entity_id = None
        self.connect()

    def agentName(self):
        return self.name
    
    
    
    def connect(self):
        self.connection = Connection()
        self.connection.agent = self    
        self.connection.connect('127.0.0.1', 7000)
        connect_msg = AKConnect(self)
        self.connection.send_msg(connect_msg)

    def message_received(self, msg):
        if isinstance(msg, KAConnectOK):
            self.handle_connect_ok(msg)
        elif isinstance(msg, KAConnectError):
            self.handle_connect_error(msg)
        elif isinstance(msg, KASense):
            self.process_sense(msg)
    
    def handle_connect_ok(self, msg):
        print('handle_connect_ok(msg): ', msg.requestID , msg.agentId)
        #entities received from server should be merged to the world model
        entities = msg.entities

        #configs received from server
        config = msg.config

       
        ack_msg = AKAcknowledge(msg.requestID, msg.agentId)
        self.connection.send_msg(ack_msg)

    
    def process_sense(self, msg):
        self.think(msg.get_time(), msg.get_change_set(), msg.get_hearing())
        
    def think(self, timestep, change_set, heard):
        print('think method. timestep = ', timestep)

class PoliceForceAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = 'rescue_agent.PoliceForceAgent'

    def get_requested_entities(self):
        return 'entity:policeforce'

class FireBrigadeAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = 'rescue_agent.FireBrigadeAgent'

    def get_requested_entities(self):
        return 'entity:firebrigade'

class AmbulanceTeamAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = 'rescue_agent.AmbulanceTeamAgent'

    def get_requested_entities(self):
        return 'entity:ambulanceteam'
