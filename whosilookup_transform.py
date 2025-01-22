from maltego_trx.entities import Domain, Phrase
from maltego_trx.transform import DiscoverableTransform
import whois

class WhoisLookupTransform(DiscoverableTransform):
    def __init__(self):
        super().__init__()

    @classmethod
    def create_entities(cls, request, response):
        domain_name = request.Value
        try:
            whois_data = whois.whois(domain_name)
            registrar = whois_data.registrar or "Unknown"
            creation_date = str(whois_data.creation_date) or "Unknown"

            response.addEntity(Phrase, f"Registrar: {registrar}")
            response.addEntity(Phrase, f"Created: {creation_date}")
        except Exception as e:
            response.addUIMessage(f"WHOIS lookup failed: {str(e)}")
