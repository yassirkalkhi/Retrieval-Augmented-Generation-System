import chromadb
import asyncio
from services.embedding import EmbeddingService



class ChromaService:
    def __init__(self, collection_name,db_location='C:\\Users\\yasser\\Desktop\\chroma-database',use_http=False, host='localhost', port=5000,embedding_type = 'text'):
        self.embedding_service = EmbeddingService(type=embedding_type)
        if use_http:
            client = AsyncHttpClient(host=host, port=port)
        else:
            client = chromadb.PersistentClient(path=db_location)
        self.chroma = client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_service

          ) 

    def store(self, documents):
        """
        Store vectors in the ChromaDB.
        """
        Documents = [doc.content for doc in documents]
        Metadatas = [doc.metadata for doc in documents]
        ids = [doc.metadata['id'] for doc in documents]

        self.chroma.add(
            documents=Documents,
            metadatas=Metadatas,
            ids=ids
        )
       
       
        

    def query(self, query,k=3):
        """
        Query the vector database for the most similar texts.
        """
        results = self.chroma.query(query_texts=query, n_results=k)
        return results
