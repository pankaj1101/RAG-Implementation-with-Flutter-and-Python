from fastapi import FastAPI

from pydantic_models.chat_body import Chatbody
from services.search_service import SearchService

app=FastAPI()

search_service=SearchService()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat")
def chat_endpoint(body:Chatbody):
    serch_result = search_service.web_search(query=body.query)
    print(serch_result)

