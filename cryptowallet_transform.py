from maltego_trx.entities import CryptocurrencyWallet, Phrase
from maltego_trx.transform import DiscoverableTransform
import requests

class CryptoWalletTransform(DiscoverableTransform):
    def __init__(self):
        super().__init__()

    @classmethod
    def create_entities(cls, request, response):
        wallet_address = request.Value
        url = f"https://api.blockchain.info/rawaddr/{wallet_address}"
        
        res = requests.get(url).json()
        if "txs" in res:
            for tx in res["txs"][:5]:
                entity = response.addEntity(Phrase, f"Transaction: {tx['hash']}")
                entity.addProperty("Amount", "Amount (BTC)", "strict", str(tx["result"]))
        else:
            response.addUIMessage("No transactions found")
