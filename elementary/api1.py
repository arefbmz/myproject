import requests
import json

r = requests.get("https://api.sunrise-sunset.org/json?lat=34.03&lng=118.15")
print(json.dumps(r.json(), indent=4))
