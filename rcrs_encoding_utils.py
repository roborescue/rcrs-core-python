import ControlMessageProto_pb2
def write_int32(value, writer):
    b=[((value >> 24) & 0xFF),
        ((value >> 16) & 0xFF),
        ((value >> 8) & 0xFF),
        (value & 0xFF)
    ]
    writer.write(bytes(b))

async def read_int32(reader):
    byte_array=await reader.readexactly(4)
    print(byte_array)
    value = int(((byte_array[0]) << 24) + ((byte_array[1])<< 16) + ((byte_array[2]) << 8) + (byte_array[3]))
    return value

async def write_msg(msg,writer):
    out = msg.SerializeToString()
    write_int32(len(out),writer)
    writer.write(out)
    await writer.drain()

async def read_msg(reader):
    await reader.read(1)
    size=await read_int32(reader)
    content=await reader.readexactly(size)
    message=ControlMessageProto_pb2.MessageProto();
    message.ParseFromString(bytes(content))
    return message