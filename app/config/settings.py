# CHROMA_PATH = "db/chroma"

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Models
    EMBEDDING_MODEL = "text-embedding-3-small"
    GENERATION_MODEL = "gpt-4o-mini"

    # Chunking
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 100

    # Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    PDF_DIR = os.path.join(DATA_DIR, "pdfs")
    CHUNKS_DIR = os.path.join(DATA_DIR, "chunks")
    DB_DIR = os.path.join(BASE_DIR, "db")
    CHROMA_PATH = os.path.join(DB_DIR, "chroma")
    LOG_DIR = os.path.join(BASE_DIR, "logs")

    COLLECTION_NAME = os.getenv("CHROMA_COLLECTION", "default_collection")


