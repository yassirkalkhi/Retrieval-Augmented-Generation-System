from ast import Str
from numpy import number
from pydantic import BaseModel
from typing import List, Optional,Any




class Document(BaseModel):
    content: str
    metadata: Optional[Any]

class Documents(BaseModel):
    documents: List[Document]

class StoreVectorsRequest(BaseModel):
    user_id: str
    texts: List[str]
    metadatas: Optional[List[dict]] = None

class QueryRequest(BaseModel):
    query: str
    
class PDFDocument(BaseModel):
    path: str

class PDFStoreRequest(BaseModel):
    uid: str
    pdfs: List[PDFDocument]


class ImageDocument(BaseModel):
    path: str

class ImageStoreRequest(BaseModel):
    uid: str
    images: List[ImageDocument]