from fastapi import APIRouter
from services.chroma import ChromaService
from services.llm import LLMService
from models.schemas import QueryRequest


chroma = ChromaService(collection_name="pdf", embedding_type="query")


llm = LLMService()

router = APIRouter()

@router.post("/query")
async def query(request: QueryRequest):
  
    results = chroma.query(request.query,k=10)
    # context = []
    # print('results',results)
    # for document in results:
    #   if request.type == 'text':
    #       context.append(document.page_content)

    # context_text = "\n".join(context)
    # answer = llm.query(request.query,context_text)
    
    return {"answer": results}
