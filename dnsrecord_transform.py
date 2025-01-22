from maltego_trx.entities import Domain, Phrase
from maltego_trx.transform import DiscoverableTransform
import dns.resolver

class DNSLookupTransform(DiscoverableTransform):
    def __init__(self):
        super().__init__()

    @classmethod
    def create_entities(cls, request, response):
        domain = request.Value
        try:
            for record_type in ["A", "MX", "TXT"]:
                answers = dns.resolver.resolve(domain, record_type, raise_on_no_answer=False)
                for answer in answers:
                    response.addEntity(Phrase, f"{record_type} Record: {str(answer)}")
        except Exception as e:
            response.addUIMessage(f"DNS lookup failed: {str(e)}")
