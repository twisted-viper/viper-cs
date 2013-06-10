'''
Created on 2013-5-26

@author: wolf_m
'''
from log.viper_log import ViperLogger

logger = ViperLogger.getLogger()

class BanlanceServer():
    inst = None

    def __init__(self):
        self.protocol = None
        
    def sendMessage(self, msg):
        if self.protocol == None:
            return
        logger.debug('Seng Message ' + msg)
        self.protocol.sendLine(msg)
    
    def getId(self):
        return str(self.protocol.transport.getPeer())
    
    
    def closeConnecton(self):
        self.protocol.transport.loseConnection()
     
    
    def setProtocol(self,protocol):
        self.protocol = protocol
        
    @staticmethod
    def getInstance():
        if not BanlanceServer.inst:
            BanlanceServer.inst = BanlanceServer()
        return BanlanceServer.inst
