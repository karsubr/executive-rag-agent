import os
import uuid
import json
from app.ingestion.loader import DocumentLoader
from app.ingestion.chunker import TokenChunker
from app.embeddings.embedder import Embedder
from app.vectorstore.chroma_store import ChromaStore
from app.config.settings import Settings

class IngestionPipeline:

    def __init__(self):
        self.loader = DocumentLoader()
        self.chunker = TokenChunker()
        self.embedder = Embedder()
        self.store = ChromaStore()

    def ingest_pdf(self, filename: str):

        path = os.path.join(Settings.PDF_DIR, filename)

        print("Loading PDF...")
        text = self.loader.load_pdf(path)

        print("Chunking...")
        chunks = self.chunker.chunk(text)
        print(f"Created {len(chunks)} chunks")

        # Save chunks for inspection
        os.makedirs(Settings.CHUNKS_DIR, exist_ok=True)
        with open(os.path.join(Settings.CHUNKS_DIR, "chunks.json"), "w", encoding="utf-8") as f:
            json.dump(chunks, f, indent=2)

        print("Embedding...")
        embeddings = self.embedder.embed(chunks)

        ids = [str(uuid.uuid4()) for _ in chunks]

        print("Storing in Chroma...")
        self.store.add(ids, chunks, embeddings)

        print(f"Total documents in DB: {self.store.count()}")
        print("Ingestion complete.")
