from fastapi import APIRouter
from services.chroma import ChromaService
from models.schemas import Document, ImageStoreRequest
from uuid import uuid4
from PIL import Image
import os
import requests

router = APIRouter()

db = ChromaService(collection_name="images", embedding_type="image")

async def store_image(image):
    path = image.path
    # Check if path is a URL
    if path.startswith(('http://', 'https://')):
        try:
            response = requests.head(path)
            if response.status_code != 200:
                raise FileNotFoundError(f"Image not found at URL {path}")
        except requests.exceptions.RequestException:
            raise FileNotFoundError(f"Failed to access URL {path}")
    else:
        # Check local file path
        if not os.path.exists(path):
            raise FileNotFoundError(f"Image not found at local path {path}")

    metadata = {
        "source": path,
        "id": str(uuid4())
    }

    document = Document(
        content=path, 
        metadata=metadata
    )

    db.store([document])
    print(document)

@router.post("/image/store")
async def store(request: ImageStoreRequest):
    for image in request.images:
        await store_image(image)

    return {"answer": "success"}
