from services.embedding import EmbeddingService
embedding_service = EmbeddingService(type="image")
embedding = embedding_service.embed("https://hips.hearstapps.com/autoweek/assets/s3fs-public/0j5a6937-edit.jpg?resize=980:*")
print(embedding)