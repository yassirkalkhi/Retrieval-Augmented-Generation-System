from langchain_core.documents import Document
from langchain_chroma import Chroma
from services.embedding import EmbeddingService
import uuid



class ChromaService:
    def __init__(self, collection_name,db_location):
        self.chroma = Chroma(
         collection_name=collection_name,
         embedding_function= EmbeddingService('nomic-embed-text').embeddings,
         persist_directory=db_location,
           )

    def store(self, texts, metadatas=None):
        """
        Store vectors in the ChromaDB.
        """
       
        documents = []
        ids = []
        for i in range(len(texts)):
               ids.append(str(uuid.uuid4()))

        for i in range(len(texts)):
            documents.append(Document(
                page_content=texts[i],
                metadata=metadatas[i] if metadatas else {},
                id=ids[i]
            ))


        self.chroma.add_documents(
           documents = documents
        )
            


    def query(self, query):
        """
        Query the vector database for the most similar texts.
        """
        retreiver  =  self.chroma.as_retriever(
        search_kwargs={"k": 1}
             )
        return retreiver.invoke(query)
