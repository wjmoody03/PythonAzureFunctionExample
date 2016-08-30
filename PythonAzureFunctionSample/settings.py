#this will leverage environment variables if found. if not, return settings from static 
#settings.json file that is excluded from source control

import json
import os

class config:

    def __init__(self):
        try:
            self.LendingClubUserName = os.environ["LendingClubUserName"]
            self.env = "azure"
            self.text = "i am running there"
        except KeyError:
            self.env = "local"
            self.text = "i am running here"

