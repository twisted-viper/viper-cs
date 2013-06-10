#coding:utf-8
'''
Created on 2013-6-10

@author: wolf_m
'''
from biz.BalanceServer import BanlanceServer
from biz.util.info import getConnectorInfo
from log.viper_log import ViperLogger
from settings import BANLANCE_SERVER_HOST, BANLANCE_SERVER_PORT
from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver
import json

logger = ViperLogger.getLogger()

class ViperConnectorServerProtocol(LineReceiver):
    def __init__(self):
        pass
        
    def connectionMade(self):
        logger.info('Connected to Banlance Server...' )
        banlanceServer = BanlanceServer.getInstance()
        BanlanceServer.getInstance().setProtocol(self)
        
        message = {}
        message['name'] = 'connector-init'
        message['connector'] = getConnectorInfo()
        banlanceServer.sendMessage(json.dumps(message))
    
    def connectionLost(self, reason):
        print 'clientconnectionLost'
        
    def lineReceived(self, line):
        print line
        
class ConnectionTestFactory(ClientFactory):
    def buildProtocol(self, addr):
        return ViperConnectorServerProtocol()  
    

def buildConnectonToBalanceServer():
    testFactory = ConnectionTestFactory()
    reactor.connectTCP(BANLANCE_SERVER_HOST, BANLANCE_SERVER_PORT, testFactory)