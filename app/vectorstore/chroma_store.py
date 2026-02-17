# import chromadb
# from app.config.settings import Settings


# class ChromaStore:

#     def __init__(self):
#         self.client = chromadb.PersistentClient(path=Settings.CHROMA_PATH)
#         self.collection = self.client.get_or_create_collection(
#             name=Settings.COLLECTION_NAME
#         )

#     def add(self, ids, documents, embeddings):
#         self.collection.add(
#             ids=ids,
#             documents=documents,
#             embeddings=embeddings
#         )

#     def query(self, query_embedding, k=5):
#         return self.collection.query(
#             query_embeddings=[query_embedding],
#             n_results=k
#         )








import chromadb
from app.config.settings import Settings

class ChromaStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(path=Settings.CHROMA_PATH)
        self.collection = self.client.get_or_create_collection(
            name=Settings.COLLECTION_NAME
        )

    def add(self, ids, documents, embeddings):
        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings
        )

    def query(self, query_embedding, k=5):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )
    
    def count(self):
        """Return the total number of documents in this collection."""
        return self.collection.count()
