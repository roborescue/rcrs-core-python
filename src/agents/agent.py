from connection.connection import Connection
from messages.AKAcknowledge import AKAcknowledge
from messages.KAConnectOK import KAConnectOK
from messages.KAConnectError import KAConnectError
from messages.KASense import KASense
from messages.AKConnect import AKConnect


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

    def get_id(self):
        return self.agent_id

    def connect(self):
        self.connection = Connection()
        self.connection.set_agent(self)
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

    



