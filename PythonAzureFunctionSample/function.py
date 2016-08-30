import settings
import json

config = settings.config()


print(json.dumps(config.__dict__))