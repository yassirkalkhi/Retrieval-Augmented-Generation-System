from fastapi import APIRouter
from services.chroma import ChromaService
from services.splitter import SemanticSplitterService
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from models.schemas import Document, PDFStoreRequest
import uuid

router = APIRouter()

db = ChromaService(collection_name="pdf",embedding_type='text')

async def store_pdf(pdf):
        path = pdf.path
        loader = PyPDFLoader(path)
        pages = []
        async for page in loader.alazy_load():
           pages.append(page)

        splitter = RecursiveCharacterTextSplitter(
          chunk_size=1000,
          chunk_overlap=20,
          length_function=len,
          is_separator_regex=False,
          separators=[
              "\n\n", "\n", ".", ",",
              "\u200b", "\uff0c", "\u3001", "\uff0e", "\u3002", ""
          ]
          )
        chunks = []

        for i, page in enumerate(pages, start=1):
         metadata = {"page": i, "source": path}
         split_docs = splitter.create_documents(
                [page.page_content],
         )
         splitter_service = SemanticSplitterService(max_chunk_size=1000, num_clusters=5)
         splits = splitter_service.split(page.page_content)
         for j,chunk in enumerate(split_docs,start=1):
            document = Document(
                content=chunk.page_content,
                metadata={
                    **metadata,
                    "id": str(uuid.uuid4()),
                    "chunk": str(j)
                },
            )
            chunks.append(document)
        
      
        chunks = [doc for doc in chunks if doc.content.strip()]

        db.store(chunks)
        print(chunks[-1])

@router.post("/pdf/store")
async def store(request : PDFStoreRequest):
    for pdf in request.pdfs :
     await  store_pdf(pdf)
        
    return {"answer": 'success'}
