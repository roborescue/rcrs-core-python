from connection import Connection
from message import AKAcknowledge
from message import KAConnectOK
from message import KAConnectError
from message import KASense
from message import AKConnect


class Agent:

    def __init__(self):
        print('agent created .... ')
        self.connection = None
        self.name = ''
        self.connect_request_id = None
        self.world_model = None
        self.config = None
        self.random = None
        self.agent_id = None
        self.connect()

    def get_name(self):
        return self.name

    def connect(self):
        self.connection = Connection()
        self.connection.agent = self
        self.connection.connect('127.0.0.1', 7000)
        akconnect_msg = AKConnect()
        akconnect_msg.set_agent(self)
        akconnect_msg.prepare_message()
        self.connection.send_msg(akconnect_msg)

    def message_received(self, msg):
        if isinstance(msg, KAConnectOK):
            self.handle_connect_ok(msg)
        elif isinstance(msg, KAConnectError):
            self.handle_connect_error(msg)
        elif isinstance(msg, KASense):
            self.process_sense(msg)

    def handle_connect_error(self, msg):
        pass

    def handle_connect_ok(self, msg):
        print('handle_connect_ok(msg): ', msg.request_id, msg.agent_id)
        self.agent_id = msg.agent_id
        # entities received from server should be merged to the world model
        world = msg.world

        # configs received from server
        config = msg.config

        ack_msg = AKAcknowledge()
        ack_msg.set_agent_id(msg.agent_id)
        ack_msg.set_request_id(msg.request_id)
        ack_msg.prepare_message()
        self.connection.send_msg(ack_msg)

    def process_sense(self, msg):
        self.think(msg.get_time(), msg.get_change_set(), msg.get_hearing())

    def think(self, timestep, change_set, heard):
        print('think method. timestep = ', timestep , self.agent_id)


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
