from fastapi import FastAPI
from routes.query import router as query_router
from routes.pdf import router as pdf_router
from routes.image import router as image_router

app = FastAPI()

app.include_router(query_router)
app.include_router(pdf_router)
app.include_router(image_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
