import stream

import asyncio
from agent.Civilian import Civilian

civilian= Civilian()
asyncio.run(civilian.connect("127.0.0.1",7000))