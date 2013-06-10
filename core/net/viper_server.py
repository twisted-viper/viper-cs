# coding:utf-8
'''
Created on May 24, 2013

@author: HP
'''


from core.net.viper_callback import onConectorConnectionMade, \
    onConectorConnectionLost, onLineReceived, onViperConnectorServerRunning
from log.viper_log import ViperLogger
from settings import SERVER_PORT
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver


try:
    from twisted.internet import epollreactor
    epollreactor.install()
except:
    pass


class ViperConnectorServerProtocol(LineReceiver):
    def __init__(self):
        pass
        
    def connectionMade(self):
        onConectorConnectionMade(self)
    
    def connectionLost(self, reason):
        onConectorConnectionLost(self, reason)
        
    def lineReceived(self, line):
        onLineReceived(self,line)

        
class ViperConnectorServerFactory(Factory):
    def buildProtocol(self, addr):
        return ViperConnectorServerProtocol()


class ViperConnectorServer():
    inst = None
    def __init__(self):
        pass
    
    @staticmethod
    def getInstance():
        if not ViperConnectorServer.inst:
            inst = ViperConnectorServer()
        return inst
    
    def getReactor(self):
        return reactor
        
    def start(self):
        logger = ViperLogger.getLogger()
        logger.info('Viper Connector Server selector type:' + str(type(reactor)))
        reactor.listenTCP(SERVER_PORT, ViperConnectorServerFactory())
        reactor.callWhenRunning(onViperConnectorServerRunning)
#        reactor.callWhenRunning(group.checkConnectorServerStatus)
        reactor.run()
    
