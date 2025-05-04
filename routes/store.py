from fastapi import APIRouter
from services.chroma import ChromaService
from models.schemas import StoreVectorsRequest


router = APIRouter()

@router.post("/store")
async def store_vectors(request: StoreVectorsRequest):
   
    collection_name = "safi"
    db_location = "./raze"

    chroma = ChromaService(collection_name,db_location)
    chroma.store(request.texts)


    return {"status": "success"}
