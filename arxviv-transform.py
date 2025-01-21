from maltego_trx.entities import Phrase
from maltego_trx.transform import DiscoverableTransform
import requests

class ArxivSearchTransform(DiscoverableTransform):
    def __init__(self):
        super().__init__()

    @classmethod
    def create_entities(cls, request, response):
        # Retrieve search parameters
        search_query = request.Value or "pakistanterrorism"
        start = request.TransformSettings.get("start", 10)
        max_results = request.TransformSettings.get("max_results", 1)

        # Query the arXiv API
        url = f"https://export.arxiv.org/api/query?search_query=all:{search_query}&start={start}&max_results={max_results}"
        response_data = requests.get(url)

        if response_data.status_code == 200:
            # Parse response data
            feed = response_data.text
            entries = feed.split("<entry>")
            for entry in entries[1:]:
                title_start = entry.find("<title>") + 7
                title_end = entry.find("</title>")
                title = entry[title_start:title_end].strip()

                summary_start = entry.find("<summary>") + 9
                summary_end = entry.find("</summary>")
                summary = entry[summary_start:summary_end].strip()

                # Add Phrase entity for each result
                phrase = Phrase(title)
                phrase.addProperty("summary", "Summary", "strict", summary)
                response.addEntity(phrase)
        else:
            response.addUIMessage(f"Failed to fetch data. Status code: {response_data.status_code}")
