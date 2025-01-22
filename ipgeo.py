from maltego_trx.entities import IPAddress, Location
from maltego_trx.transform import DiscoverableTransform
import requests

class IPGeolocationTransform(DiscoverableTransform):
    def __init__(self):
        super().__init__()

    @classmethod
    def create_entities(cls, request, response):
        ip_address = request.Value
        api_key = "your_api_key_here"
        url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}"
        
        res = requests.get(url).json()
        if "country_name" in res:
            location = response.addEntity(Location, f"{res['city']}, {res['country_name']}")
            location.addProperty("latitude", "Latitude", "strict", res.get("latitude"))
            location.addProperty("longitude", "Longitude", "strict", res.get("longitude"))
        else:
            response.addUIMessage("Geolocation data not found")
