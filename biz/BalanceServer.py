'''
Created on 2013-5-26

@author: wolf_m
'''
from biz.util.info import getConnectorInfo
from log.viper_log import ViperLogger
from twisted.internet import reactor
import json

logger = ViperLogger.getLogger()
SEND_PING_INTERVAL = 60 * 0.5

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
    def sendIntervalPing():
        logger.info('Send Ping to Banlance Server')
        banlanceServer = BanlanceServer.getInstance()
        message = {}
        message['name'] = 'connector-ping'
        message['connector'] = getConnectorInfo()
        banlanceServer.sendMessage(json.dumps(message))
        reactor.callLater(SEND_PING_INTERVAL, BanlanceServer.sendIntervalPing)
    
    @staticmethod
    def getInstance():
        if not BanlanceServer.inst:
            BanlanceServer.inst = BanlanceServer()
        return BanlanceServer.inst
