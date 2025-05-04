from langchain_ollama import OllamaEmbeddings

class EmbeddingService:
    def __init__(self, model: str = "nomic-embed-text"):
        self.embeddings =   OllamaEmbeddings(model=model)

  