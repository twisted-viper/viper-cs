'''
Created on 2013-5-26

@author: wolf_m
'''


from biz.MessageFactory import MESSAGE_ACTION
from biz.ViperClient import ViperClient
from biz.ViperClientGroup import ViperClientGroup
from biz.connector_client import buildConnectonToBalanceServer
from log.viper_log import ViperLogger
import json



logger = ViperLogger.getLogger()
  
    
def onViperConnectorServerRunning():
    logger.debug('Viper Connector Server Started')
    buildConnectonToBalanceServer()
    
def onConectorConnectionMade(protocol): 
    logger.debug('Client connection made')
    ViperClientGroup.getInstance().addClient(ViperClient(protocol));

def onConectorConnectionLost(protocol, reason):
    connectorId = str(protocol.transport.getPeer())
    logger.debug('Conector connection lost ' + connectorId)
    
def onLineReceived(protocol, line):
    logger.debug('Message Received ' + line)
    message = json.loads(line)
    connectorId = str(protocol.transport.getPeer())
    messageParse = MESSAGE_ACTION.get(message['name'])
    if messageParse == None:
        logger.error('Unrecognized message received ' + message['name'])
        protocol.transport.loseConnection()
    else:
        messageParse(connectorId, message)
    
