# will load mastodon public API data

import requests
import json

response = requests.get("https://aus.social/api/v1/timelines/tag/cats?limit=2")
statuses = json.loads(response.text) # this converts the json to a python list of dictionary
assert statuses[0]["visibility"] == "public" # we are reading a public timeline
print(statuses[0]["content"]) # this prints the status text

