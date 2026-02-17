import tiktoken
from app.config.settings import Settings


class TokenChunker:

    def __init__(self):
        self.encoding = tiktoken.get_encoding("cl100k_base")

    def chunk(self, text: str):
        tokens = self.encoding.encode(text)
        chunks = []

        start = 0

        while start < len(tokens):
            end = start + Settings.CHUNK_SIZE
            chunk_tokens = tokens[start:end]
            chunk_text = self.encoding.decode(chunk_tokens)

            chunks.append(chunk_text)

            start += Settings.CHUNK_SIZE - Settings.CHUNK_OVERLAP

        return chunks
