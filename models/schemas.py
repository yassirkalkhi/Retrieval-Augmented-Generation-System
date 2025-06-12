from pydantic import BaseModel, Field
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

class Message(BaseModel):
    role: str
    content: str


class QueryRequest(BaseModel):
    uid: str
    query: str
