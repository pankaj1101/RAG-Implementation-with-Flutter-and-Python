from fastapi import FastAPI

from pydantic_models.chat_body import Chatbody
from services.search_service import SearchService
from services.sort_search_service import SortSearchService
app=FastAPI()

search_service=SearchService()
sort_service=SortSearchService()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat")
def chat_endpoint(body:Chatbody):
    serch_result = search_service.web_search(query=body.query)
    sort_resut=sort_service.sort_service(body.query,serch_result)

