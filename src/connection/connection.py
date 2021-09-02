import socket
import threading
from connection.encoding_tool import read_int32_from_byte_arr
from connection.encoding_tool import write_str
from connection.encoding_tool import write_int32
from connection.encoding_tool import read_msg
from connection.encoding_tool import write_msg
from connection.data_stream import OutputStream
from connection.data_stream import InputStream

class Connection:

    def __init__(self):
        self.socket = None
        self.agent = None
        self.buffer_size = 4096
        self.data_buffer = b''

    def connect(self, address, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((address, port))
        except socket.error as exception:
            print(str(exception))
            self.socket.close()
            return

        read_thread = threading.Thread(target=self.read_loop)
        read_thread.daemon = True
        read_thread.start()

    def set_agent(self, _agent):
        self.agent = _agent

    def msg_bytes_received(self, byte_array):
        input_stream = InputStream(byte_array)
        msg = read_msg(input_stream)
        if msg is not None:
            self.agent.message_received(msg)

    def read_loop(self):
        while True:
            try:
                message_data = self.recv_msg()
                self.msg_bytes_received(message_data)
            except IOError:
                self.socket.close()
                break

    def recv_msg(self):
        buffer_size = 4096
        msg_size_data = bytearray()
        while len(msg_size_data) < 4:
            try:
                msg_size_data += self.socket.recv(buffer_size)
            except socket.error as error_msg:
                raise IOError('tcp client IOError:' + error_msg)

        if msg_size_data:
            msg_size = read_int32_from_byte_arr(msg_size_data[0:4])
            msg_data = msg_size_data[4:]
            while len(msg_data) < msg_size:
                try:
                    msg_data += self.socket.recv(buffer_size)
                except socket.error as error_msg:
                    raise IOError('tcp client IOError:' + error_msg)
            if msg_data:
                self.data_buffer = msg_data[msg_size:]
                return msg_data[:msg_size]
        else:
            raise IOError('tcp client is disconnected')

        return ''

    def send_msg(self, msg):

        urn = msg.get_urn()
        content = msg.write()

        out1 = OutputStream()
        write_str(urn, out1)
        d1 = out1.getvalue().encode()

        out1 = OutputStream()
        write_int32(len(content), out1)
        d2 = out1.getvalue().encode()

        out1 = OutputStream()
        write_int32(0, out1)
        d3 = out1.getvalue().encode()

        data = d1 + d2 + content + d3

        out1 = OutputStream()
        write_int32(len(data), out1)

        data = out1.getvalue().encode() + data

        self.send_bytes(data)

    def send_bytes(self, byte_array):
        self.socket.sendall(byte_array)

    def shutdown(self):
        self.socket.close()
