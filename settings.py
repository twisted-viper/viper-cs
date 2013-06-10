#coding:utf-8
'''
Created on May 24, 2013

@author: HP
'''
import logging
import os

BANLANCE_SERVER_HOST = '127.0.0.1'
BANLANCE_SERVER_PORT = 55024

SERVER_PORT = 50610
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

LOG = {
       'path':os.path.join(SITE_ROOT, 'log'),
       'level':logging.NOTSET
}


