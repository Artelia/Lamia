#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json, os, logging
from collections import namedtuple

class Configuration():       

    configurationpath = os.path.join(os.path.dirname(__file__), 'configuration.json')
    __instance = None

    # Init file implementing the singleton pattern    
    def __init__(self):
        self.data = None
        if self.__instance is not None:
            raise Exception("This class is a Singleton !")
        Configuration.__instance = self
        self.data = self.loadjsonfile(self.configurationpath)

    def __call__(self):
        """ Callable returning directly the data from the readed configuration file make things tidier and more handy    

            Return:
                dict: The dictionnary representation of the Json object, except this dict can be access through attributes
            
            Example:
                ``myConfigurationInstance().myAttribute``
        """
        return self.data

    @staticmethod        
    def getinstance():
        """ Static Getter which ensure that there is only access point to the Configuration class (because it's a Singleton)

            Return:
                Configuration: An object able to read and write on a configuration files, should be the only one use through the system
            
            Example:
                `myConfigurationInstance = Configuration.getconfigurationinstance()`
        """
        if Configuration.__instance is None:
            Configuration()
        return Configuration.__instance        
    
    # Supposed to write the config files, didn't test it
    def setconfiguration(self):
        json.dumps(self.data)

    # Load the configuration file and parse and interface it as a Python object (neet isn't ?)
    def loadjsonfile(self, path):
        with open(self.configurationpath) as config_file:       
            return json.load(config_file, object_hook = lambda dict: DictWithAttributeAccess(dict))

# Allow to read a Json file, parse/interface it into as an object and get/set this object, only problem, cannot set non already genrerated nested value
class DictWithAttributeAccess(dict):
    def __getattr__(self, key):
        return self[key]
 
    def __setattr__(self, key, value):
        self[key] = value