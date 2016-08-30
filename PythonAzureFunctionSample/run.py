import settings
import json
import data

config = settings.Config()
data = data.Database(config.connectionString)

configVals = json.dumps(config.__dict__)
print(configVals)
data.save(configVals)
