import os
import requests

tile_url = "https://tiles0.planet.com/data/v1/layers"
data = {
    "ids": [
        "PSScene4Band:20180326_190231_0d05, PSScene4Band:20180326_190231_1_0d05, PSScene4Band:20180326_190230_0d05, PSScene4Band:20180326_154223_1053, PSScene4Band:20180326_154222_1053"
    ]
}
api_key = "PLAKf9ed24ca36b8460f923682adbdb376f5"  # os.getenv('PL_API_KEY')

res = requests.post(tile_url, auth=(api_key, ""), data=data)
print(res)
name = res.json()["name"]
url = "{}/wmts/{}?api_key={}".format(tile_url, name, api_key)
print(url)
