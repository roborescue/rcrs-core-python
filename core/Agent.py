import core.rcrs_encoding_utils as rcrs_encoding_utils
from world.WorldModel import WorldModel
from abc import ABC, abstractmethod
import sys
import traceback
import core.RCRSProto_pb2 as RCRSProto_pb2
import core.URN as URN
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
    def precompute(self):
        pass

    # @abstractmethod
    def think(self,time,changeSet,hear,overtime):
        pass

    def connect(self,host,port):
        try:
            import socket

            self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, port))
                # s.sendall(b'Hello, world')
                # data = s.recv(1024)

            # print('Received', repr(data))
            # reader, writer = asyncio.open_connection(host, port)
            # self.reader=reader
            # self.writer=writer
            self.sendAKConnect(requestId=1)
            self.parseMessageFromKernel()
        except IOError as e:
            print(f'Exception occured in connecting: {type(e).__name__}: {e}')
        

        
            

    def messageReceived(self,msg):
        if(msg.urn==URN.ControlMSG.KA_SENSE):
            self.handleKASense(msg)
        elif(msg.urn==URN.ControlMSG.KA_CONNECT_OK):
            self.handleKAConnectOk(msg)
        elif (msg.urn==URN.ControlMSG.KA_CONNECT_ERROR):
            self.handleKAConnectError(msg)
    
    def handleKASense(self,msg):
        overtime=False
        import socket
        if(self.sock.recv(1,socket.MSG_PEEK)):
            print("next cycle is recevied but you are still in the previous one")
            overtime=True
        agentId=msg.components[URN.ComponentControlMSG.AgentID].entityID
        time=msg.components[URN.ComponentControlMSG.Time].intValue
        changeSet=msg.components[URN.ComponentControlMSG.Updates].changeSet
        hear=msg.components[URN.ComponentControlMSG.Hearing].commandList
        if(self.id!=agentId):
            print(f'ERRROR this should not never happen agentid={self.id} but receive a sense for {agentId}')
        self.world.merge(changeSet)
        try:
            actmsg=self.think(time,changeSet,hear,overtime)
            rcrs_encoding_utils.write_msg(actmsg,self.sock)
        except Exception as e:
            print(f'Exception occured in think: {type(e).__name__}: {e} \n {traceback.format_exc()}')

    def handleKAConnectOk(self,msg):    
        entities=msg.components[URN.ComponentControlMSG.Entities].entityList.entities
        self.world=WorldModel()
        self.world.addEntitiesProto(entities)
        requestId=msg.components[URN.ComponentControlMSG.RequestID].intValue
        self.id=msg.components[URN.ComponentControlMSG.AgentID].entityID
        self.config=msg.components[URN.ComponentControlMSG.AgentConfig].config
        print(f'Connected successfully agent id={self.id}')
        try:
            self.precompute()
        except Exception as e:
            print(f'Exception occured in Precompute: {type(e).__name__}: {e} \n {traceback.format_exc()}')

        self.sendAKAcknowledge(requestId)


    def handleKAConnectError(self,msg):
        requestId=msg.components[URN.ComponentControlMSG.RequestID].intValue
        reason=msg.components[URN.ComponentControlMSG.Reason].stringValue
        print(f'Connect Error reason={reason} requestId={requestId}')
        self.sock.close()
        import sys
        sys.exit(1)

    def sendAKConnect(self,requestId):
        msg=RCRSProto_pb2.MessageProto()
        msg.urn=URN.ControlMSG.AK_CONNECT
        msg.components[URN.ComponentControlMSG.RequestID].intValue=requestId
        msg.components[URN.ComponentControlMSG.Version].intValue=2
        msg.components[URN.ComponentControlMSG.Name].stringValue=self.name()
        for urn in self.requestedEntityTypes():
            msg.components[URN.ComponentControlMSG.RequestedEntityTypes].intList.values.append(urn)
        rcrs_encoding_utils.write_msg(msg,self.sock)

    def sendAKAcknowledge(self,requestId):
        msg=RCRSProto_pb2.MessageProto()
        msg.urn=URN.ControlMSG.AK_ACKNOWLEDGE
        msg.components[URN.ComponentControlMSG.RequestID].intValue=requestId
        msg.components[URN.ComponentControlMSG.AgentID].entityID=self.id
        rcrs_encoding_utils.write_msg(msg,self.sock)

    def parseMessageFromKernel(self):
        try:
            while 1:
                msg=rcrs_encoding_utils.read_msg(self.sock)
                # print(msg)
                self.messageReceived(msg)
        except IOError as e:
            print(f'Communication error: {type(e).__name__}: {e}')

    

####################################commands
    def rest(self,time):
        msg=RCRSProto_pb2.MessageProto()
        msg.urn=URN.Command.AK_REST
        msg.components[URN.ComponentControlMSG.AgentID].entityID=self.id
        msg.components[URN.ComponentControlMSG.Time].intValue=time
        return msg
