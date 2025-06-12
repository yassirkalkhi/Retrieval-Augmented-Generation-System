import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from fastapi import FastAPI
from routes.file import router as file_router

app = FastAPI()

app.include_router(file_router)

