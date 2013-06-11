'''
Created on 2013-6-10

@author: wolf_m
'''

from biz.ViperClientGroup import ViperClientGroup
from settings import SERVER_NAME

def getConnectorInfo():
    returnObj = {}
    returnObj['name'] = SERVER_NAME
    returnObj['clientCount'] = ViperClientGroup.getInstance().getClientSize()
    return returnObj