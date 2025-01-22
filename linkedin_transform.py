from maltego_trx.entities import Person, Phrase
from maltego_trx.transform import DiscoverableTransform
import requests

class LinkedInSearchTransform(DiscoverableTransform):
    def __init__(self):
        super().__init__()

    @classmethod
    def create_entities(cls, request, response):
        person_name = request.Value
        linkedin_url = f"https://api.example.com/linkedin?name={person_name}"  # Replace with actual API
        
        res = requests.get(linkedin_url).json()
        if res.get("profiles"):
            for profile in res["profiles"]:
                entity = response.addEntity(Phrase, profile["name"])
                entity.addProperty("LinkedIn URL", "LinkedIn URL", "strict", profile["url"])
        else:
            response.addUIMessage("No LinkedIn profiles found")
