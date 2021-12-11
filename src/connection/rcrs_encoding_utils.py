""" utils to handle connection """

from connection import RCRSProto_pb2


def write_int32(value, sock):
    b = [((value >> 24) & 0xFF),
         ((value >> 16) & 0xFF),
         ((value >> 8) & 0xFF),
         (value & 0xFF)]

    sock.sendall(bytes(b))


def readnbytes(sock, n):
    buff = b''
    while n > 0:
        b = sock.recv(n)
        buff += b
        if len(b) == 0:
            raise EOFError          # peer socket has received a SH_WR shutdown
        n -= len(b)
    return buff


def read_int32(sock):
    byte_array = readnbytes(sock, 4)
    value = int(((byte_array[0]) << 24) + ((byte_array[1])
                << 16) + ((byte_array[2]) << 8) + (byte_array[3]))
    return value


def write_msg(msg, sock):
    out = msg.SerializeToString()
    write_int32(len(out), sock)
    
    sock.sendall(out)


def read_msg(sock):
    # await reader.read(1)
    size = read_int32(sock)
    content = readnbytes(sock, size)
    message = RCRSProto_pb2.MessageProto()
    message.ParseFromString(bytes(content))
    return message
