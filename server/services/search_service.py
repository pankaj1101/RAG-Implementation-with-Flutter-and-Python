from config import Settings
from tavily import TavilyClient
from trafilatura import fetch_url, extract

setting = Settings()

tavily_client = TavilyClient(api_key=setting.tavily_api_key)

class SearchService:
    def web_search(self, query:str):
        results=[]
        response = tavily_client.search(query,max_results=10)
        search_results = response.get('results',[])

        for result in search_results:
            raw_data=trafilatura.fetch_url(result.get('url'))
            content=trafilatura.extract(raw_data,include_comments=False)
            results.append(
                {
                    "title":result.get('title'),
                    "url":result.get('url'),
                    "content":content,
                }
            )

        return results