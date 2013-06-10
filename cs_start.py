#coding:utf-8
'''
Created on May 24, 2013

@author: HP
'''
from core.net.viper_server import ViperConnectorServer



if __name__ =='__main__' :
    viperConnectorServer = ViperConnectorServer.getInstance()
    viperConnectorServer.start()