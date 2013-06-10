'''
Created on 2013-6-10

@author: wolf_m
'''
from biz.BalanceServer import BanlanceServer
from log.viper_log import ViperLogger
from twisted.internet import reactor
import json


logger = ViperLogger.getLogger()

SEND_PING_INTERVAL = 60 * 2

def sendIntervalPing2BanlanceServer():
    logger.info('Send Ping to Banlance Server')
    banlanceServer = BanlanceServer.getInstance()
    message = {}
    message['name'] = 'connector-ping'
    banlanceServer.sendMessage(json.dumps(message))
    reactor.callLater(SEND_PING_INTERVAL, sendIntervalPing2BanlanceServer)
    