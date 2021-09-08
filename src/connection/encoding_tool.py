from connection.data_stream import OutputStream
from messages.controlMessageFactory import ControlMessageFactory


def write_int32(value, output_stream):
    output_stream.write(chr((value >> 24) & 0xFF))
    output_stream.write(chr((value >> 16) & 0xFF))
    output_stream.write(chr((value >> 8) & 0xFF))
    output_stream.write(chr((value & 0xFF)))


def read_int32_from_byte_arr(byte_array):
    value = int(((byte_array[0]) << 24) + ((byte_array[1])
                                           << 16) + ((byte_array[2]) << 8) + (byte_array[3]))
    return value


def read_int32(input_stream):
    byte_array = input_stream.read(4)
    return read_int32_from_byte_arr(byte_array)


def write_str(value, output_stream):
    write_int32(len(value), output_stream)
    output_stream.write(value)


def read_str(input_stream):
    str_len = read_int32(input_stream)
    return input_stream.read(str_len)


def write_msg(msg, output_stream):
    tmp_output_stream = OutputStream()
    msg.write(tmp_output_stream)
    msg_data = tmp_output_stream.getvalue()

    write_str(msg.urn, output_stream)
    write_int32(len(msg_data), output_stream)
    output_stream.write(msg_data)


def read_msg(input_stream):
    urn = read_str(input_stream)
    data_size = read_int32(input_stream)
    if data_size > 0:
        msg_data = b''
        msg_data = input_stream.read(data_size)
        cmf = ControlMessageFactory()
        msg = cmf.make_message(urn.decode(), msg_data)
        return msg

    return None
