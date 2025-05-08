from langchain_ollama import OllamaEmbeddings
from transformers import CLIPProcessor, CLIPModel
import torch
from PIL import Image
import numpy as np
import requests
from chromadb import EmbeddingFunction, Embeddings
from models.schemas import  Documents

class EmbeddingService(EmbeddingFunction):
    def __init__(self, type: str = "text"):
        self.type = type
        if type == "text" or type == "query":
            self.embeddings = OllamaEmbeddings(model="nomic-embed-text")
        elif type == "image":
            self.clip_model = CLIPModel.from_pretrained("openai/clip-vit-large-patch14")
            self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")
        else:
            raise ValueError(f"Unsupported embedding type: {type}")

    def __call__(self, input: Documents) -> Embeddings:
        """
        This is the method required by the EmbeddingFunction interface.
        It will be called by Chroma to generate embeddings for the documents.
        :param input: A Documents object, which is a list of documents that need to be embedded.
        :return: The embeddings (numpy arrays).
        """
        embeddings = []
        for doc in input:
            if self.type == "query":
                text_embedding = self.embeddings.embed_query(doc)
                embeddings.append(np.array(text_embedding))
            elif self.type == "text":
                text_embedding = self.embeddings.embed_query(doc)
                embeddings.append(np.array(text_embedding))
            elif self.type == "image":
                if content.startswith(('http://', 'https://')):
                    image = Image.open(requests.get(content, stream=True).raw).convert("RGB")
                else:
                    image = Image.open(doc).convert("RGB")
                
                inputs = self.processor(images=image, return_tensors="pt")
                with torch.no_grad():
                    image_embedding = self.clip_model.get_image_features(**inputs)
                embeddings.append(image_embedding[0].cpu().numpy())
            else:
                raise ValueError(f"Unsupported embedding type: {self.type}")

        return embeddings
