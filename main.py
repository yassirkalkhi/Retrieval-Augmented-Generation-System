from fastapi import FastAPI
from routes.store import router as store_vectors_router
from routes.query import router as query_llm_router

app = FastAPI()

app.include_router(store_vectors_router)
app.include_router(query_llm_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
