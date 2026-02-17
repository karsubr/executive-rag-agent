# Executive RAG Agent
This project ingests PDFs, splits them into chunks, and embeds the text using OpenAI embeddings for efficient retrieval with ChromaDB. Users can interactively query the documents to get summaries or answers based on the content. It’s built with Python, LangChain, and ChromaDB, and is designed for fast, vector-based document search and analysis.

## Features
- Automatically load and process all PDFs in the `data/pdfs` folder.
- Chunking and embedding of PDF text for efficient similarity search.
- Persistent storage using ChromaDB.
- Interactive command-line querying with natural language questions.
- Configurable chunk size, overlap, and OpenAI models via `settings.py`.

## Requirements
- Python 3.11+
- `langchain`, `chromadb`, `openai`, and other dependencies (see `requirements.txt`).

## Usage
1. Place PDFs into `data/pdfs/`.
2. Activate your virtual environment:
   ```bash
   .\venv\Scripts\activate
````

## License
MIT License

Source Code
Vibe Coded Project