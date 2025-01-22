from maltego_trx.entities import Domain, Phrase
from maltego_trx.transform import DiscoverableTransform
import requests

class VirusTotalDomainTransform(DiscoverableTransform):
    def __init__(self):
        super().__init__()

    @classmethod
    def create_entities(cls, request, response):
        domain = request.Value
        api_key = "your_api_key_here"
        url = f"https://www.virustotal.com/api/v3/domains/{domain}"
        headers = {"x-apikey": api_key}
        
        res = requests.get(url, headers=headers).json()
        if res.get("data"):
            reputation = res["data"]["attributes"]["reputation"]
            entity = response.addEntity(Phrase, f"Reputation: {reputation}")
            entity.addProperty("Category", "Category", "strict", str(res["data"]["attributes"]["categories"]))
        else:
            response.addUIMessage("No data found for domain")
