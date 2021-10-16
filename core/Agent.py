import core.rcrs_encoding_utils as rcrs_encoding_utils
from world.WorldModel import WorldModel
from abc import ABC, abstractmethod
import asyncio
import sys
import traceback
import core.RCRSProto_pb2 as RCRSProto_pb2
import core.urn as urn
class Agent(ABC):
    def __init__(self):
        pass

    # @abstractmethod
    def name(self):
        return "PythonAgent-None"

    # @abstractmethod
    def requestedEntityTypes(self):
        return []
        
    
    # @abstractmethod
    async def precompute(self):
        pass

    # @abstractmethod
    async def think(self,time,changeSet,hear):
        pass

    async def connect(self,host,port):
        try:
            reader, writer = await asyncio.open_connection(host, port)
            self.reader=reader
            self.writer=writer
            await self.sendAKConnect(requestId=1)
            await self.parseMessageFromKernel()
        except IOError as e:
            print(f'Exception occured in connecting: {type(e).__name__}: {e}')
        

        
            

    async def messageReceived(self,msg):
        if(msg.urn==urn.ControlMSG.KA_SENSE):
            await self.handleKASense(msg)
        elif(msg.urn==urn.ControlMSG.KA_CONNECT_OK):
            await self.handleKAConnectOk(msg)
        elif (msg.urn==urn.ControlMSG.KA_CONNECT_ERROR):
            await self.handleKAConnectError(msg)
    
    async def handleKASense(self,msg):
        agentId=msg.components["Agent ID"].entityID
        time=msg.components['Time'].intValue
        changeSet=msg.components['Updates'].changeSet
        hear=msg.components['Hearing'].commandList
        if(self.id!=agentId):
            print(f'ERRROR this should not never happen agentid={self.id} but receive a sense for {agentId}')
        self.world.merge(changeSet)
        try:
            await self.think(time,changeSet,hear)
        except Exception as e:
            print(f'Exception occured in think: {type(e).__name__}: {e} \n {traceback.format_exc()}')

    async def handleKAConnectOk(self,msg):
        
        entities=msg.components["Entities"].entityList.entities
        self.world=WorldModel()
        self.world.addEntitiesProto(entities)
        requestId=msg.components['Request ID'].intValue
        self.id=msg.components["Agent ID"].entityID
        self.config=msg.components["Agent config"].config
        print(f'Connected successfully agent id={self.id}')
        try:
            await self.precompute()
        except Exception as e:
            print(f'Exception occured in Precompute: {type(e).__name__}: {e} \n {traceback.format_exc()}')

        await self.sendAKAcknowledge(requestId)


    async def handleKAConnectError(self,msg):
        requestId=msg.components['Request ID'].intValue
        reason=msg.components['Reason'].stringValue
        print(f'Connect Error reason={reason} requestId={requestId}')
        self.writer.close()
        await self.writer.wait_closed()
        import sys
        sys.exit()

    async def sendAKConnect(self,requestId):
        msg=RCRSProto_pb2.MessageProto()
        import core.urn as urn
        msg.urn=urn.ControlMSG.AK_CONNECT
        msg.components['Request ID'].intValue=requestId
        msg.components['Version'].intValue=2
        msg.components['Name'].stringValue=self.name()
        for urn in self.requestedEntityTypes():
            msg.components['Requested entity types'].intList.values.append(urn)
        await rcrs_encoding_utils.write_msg(msg,self.writer)

    async def sendAKAcknowledge(self,requestId):
        msg=RCRSProto_pb2.MessageProto()
        msg.urn=urn.ControlMSG.AK_ACKNOWLEDGE
        msg.components['Request ID'].intValue=requestId
        msg.components['Agent ID'].entityID=self.id
        await rcrs_encoding_utils.write_msg(msg,self.writer)

    async def parseMessageFromKernel(self):
        try:
            while 1:
                msg=await rcrs_encoding_utils.read_msg(self.reader)
                # print(msg)
                await self.messageReceived(msg)
        except IOError as e:
            print(f'Communication error: {type(e).__name__}: {e}')

    

####################################commands
    async def rest(self,time):
        msg=RCRSProto_pb2.MessageProto()
        msg.urn=urn.Command.AK_REST
        msg.components['Agent ID'].entityID=self.id
        msg.components['Time'].intValue=time
        await rcrs_encoding_utils.write_msg(msg,self.writer)
