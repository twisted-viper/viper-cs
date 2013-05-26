'''
Created on 2013-5-25

@author: wolf_m
'''

from twisted.internet.protocol import Protocol, ClientFactory, defer
from twisted.internet.selectreactor import SelectReactor
from twisted.protocols.basic import LineReceiver
import json

reactor = SelectReactor()

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
        reactor.stop()
        
    def lineReceived(self, line):
        print line
        
class ConnectionTestFactory(ClientFactory):
    def buildProtocol(self, addr):
        return ViperConnectorServerProtocol()
        
def testConnect(host, port):
    testFactory = ConnectionTestFactory()
    reactor.connectTCP(host, port, testFactory)

    
if __name__ == "__main__":
    connecting = testConnect('127.0.0.1', 55024)
#    connecting.addCallback(handleSuccess, 55024)
#    connecting.addErrback(handleFailure, 55024)
    reactor.run()
