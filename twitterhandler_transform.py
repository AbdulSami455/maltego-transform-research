from maltego_trx.entities import SocialMedia, Phrase
from maltego_trx.transform import DiscoverableTransform
import requests

class TwitterHandleTransform(DiscoverableTransform):
    def __init__(self):
        super().__init__()

    @classmethod
    def create_entities(cls, request, response):
        twitter_handle = request.Value
        bearer_token = "your_bearer_token_here"
        url = f"https://api.twitter.com/2/users/by/username/{twitter_handle}"
        headers = {"Authorization": f"Bearer {bearer_token}"}
        
        res = requests.get(url, headers=headers).json()
        if "data" in res:
            entity = response.addEntity(SocialMedia, f"@{twitter_handle}")
            entity.addProperty("Name", "Name", "strict", res["data"]["name"])
            entity.addProperty("ID", "ID", "strict", res["data"]["id"])
        else:
            response.addUIMessage("Twitter handle not found")
