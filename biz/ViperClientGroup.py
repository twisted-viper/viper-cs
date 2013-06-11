# coding:utf-8
'''
Created on 2013-6-11

@author: wolf_m
'''

class ViperClientGroup():
    inst = None
    def __init__(self):
        self.clientMap = {}
    
    def addClient(self, client):
        if client.id in self.clientMap:
            return None
        else:
            self.clientMap[client.id] = client
            return client
        
    def broadcast(self,message):
        pass
        
    def removeClientById(self, clientId):
        del self.clientMap[clientId]
        
    def removeClient(self, client):
        del self.clientMap[client.id]
        
    def getClientSize(self):
        return len(self.clientMap.keys())
    
    @staticmethod
    def getInstance():
        if ViperClientGroup.inst == None:
            ViperClientGroup.inst = ViperClientGroup()
        return ViperClientGroup.inst
        
