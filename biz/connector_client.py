#coding:utf-8
'''
Created on 2013-6-10

@author: wolf_m
'''
from settings import BANLANCE_SERVER_HOST, BANLANCE_SERVER_PORT
from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver
import json

class ViperConnectorServerProtocol(LineReceiver):
    def __init__(self):
        print type(reactor)
        
    def connectionMade(self):
        print 'clientconnectionMade'
        message = {}
        message['name'] = 'connector-init'
        self.sendLine(json.dumps(message))
    
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