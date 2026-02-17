from openai import OpenAI
from app.config.settings import Settings

client = OpenAI(api_key=Settings.OPENAI_API_KEY)


class Embedder:

    def embed(self, texts: list[str]):
        response = client.embeddings.create(
            model=Settings.EMBEDDING_MODEL,
            input=texts
        )

        return [item.embedding for item in response.data]