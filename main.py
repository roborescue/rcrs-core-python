import stream
import ControlMessageProto_pb2  # or any other compiled protobuf module

import asyncio
from Civilian import Civilian

civilian= Civilian()
asyncio.run(civilian.connect("127.0.0.1",7000))