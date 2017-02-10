# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 12:43:35 2017

@author: paulb
"""

import yaml

btdiges={}

with open ("config.yml",'r') as ymlfile:
    cfg=yaml.load(ymlfile)

    for bridgeid in cfg:
        print bridgeid
        # check for a bridgetype and ip address, if it exists then we can store the 
        bridges.append(bridgeid,bridge['bridgip'])
        
        