from pydantic import BaseModel
from typing import List, Optional

class StoreVectorsRequest(BaseModel):
    user_id: str
    texts: List[str]
    metadatas: Optional[List[dict]] = None

class QueryLLMRequest(BaseModel):
    user_id: str
    query: str
