import socket
import sys
import rcrs_core.connection.rcrs_encoding_utils as rcrs_encoding_utils


class Connection:

    def __init__(self, host, port):
        self.socket = None
        self.agent = None
        self.buffer_size = 4096
        self.data_buffer = b''
        self.host = host
        self.port = port

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.host, self.port))
        except socket.error as ex:
            print('Error connecting server. ', ex)
            sys.exit(0)

    def parseMessageFromKernel(self):
        try:
            while True:
                msg = rcrs_encoding_utils.read_msg(self.socket)
                self.agent_message_received(msg)

        except IOError as e:
            print(f'Communication error: {type(e).__name__}: {e}')

    def message_received(self, agent_message_received):
        self.agent_message_received = agent_message_received
    
    def send_msg(self, msg):
        rcrs_encoding_utils.write_msg(msg, self.socket)

    