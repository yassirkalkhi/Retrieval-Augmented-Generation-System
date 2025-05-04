from fastapi import APIRouter
from services.chroma import ChromaService
from services.llm import LLMService
from models.schemas import QueryLLMRequest


router = APIRouter()

@router.post("/query")
async def query_llm(request: QueryLLMRequest):
    collection_name = "safi"
    db_location = "./raze"
    chroma = ChromaService(collection_name,db_location)
    results = chroma.query(request.query)
    context = []
    print('results',results)
    for document in results:
          context.append(document.page_content)

    
    prompt = f"context:\n\n{context}\n\prompt: {request.query}"
    
    llm = LLMService()
    answer = llm.query_llm(prompt)
    
    return {"answer": answer}
