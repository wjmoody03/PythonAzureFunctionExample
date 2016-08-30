#this will leverage environment variables if found. if not, return settings from static 
#settings.json file that is excluded from source control

import json
import os

class Config:

    def __init__(self):
        try:
            #in Azure the app settings will be exposed as environment variables. This is essentially
            #a messy way of determining whether we are running in azure or locally. 
            self.LendingClubUserName = os.environ["LendingClubUserName"]
            dict = os.environ
        except KeyError:
            #NOTE: If running locally, you must create a file in this directory called settings.json
            #which contains an object with all required settings/variables referenced below
            with open('settings.json') as data_file:    
                data = json.load(data_file)
                dict = data

        #now we know where we need to get our settings from. Let's expose them on this object 
        self.lendingClubUserName = dict["LendingClubUserName"]
        self.lendingClubPassword = dict["LendingClubPassword"]
        self.connectionString = dict["ConnectionString"]
        