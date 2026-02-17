from app.ingestion.pipeline import IngestionPipeline
from app.config.settings import Settings
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=Settings.OPENAI_API_KEY)

if __name__ == "__main__":
    pipeline = IngestionPipeline()

    # --- Ingest all PDFs ---
    pdf_folder = Settings.PDF_DIR
    pdf_files = [
        os.path.join(pdf_folder, f)
        for f in os.listdir(pdf_folder)
        if f.lower().endswith(".pdf")
    ]

    if pdf_files:
        for pdf_path in pdf_files:
            print(f"Ingesting: {pdf_path}")
            pipeline.ingest_pdf(pdf_path)
    else:
        print(f"No PDFs found in {pdf_folder}")

    print("PDF ingestion completed!")

    # --- Query loop with GPT generation ---
    print("\nYou can now query your documents. Type 'exit' to quit.")
    while True:
        query = input("\nEnter your question: ")
        if query.lower() in ["exit", "quit"]:
            print("Exiting query session.")
            break

        # 1️⃣ Get top chunks from Chroma
        query_embedding = pipeline.embedder.embed([query])[0]
        results = pipeline.store.query(query_embedding, k=10)

        top_docs = results.get("documents", [[]])[0]

        if not top_docs:
            print("No relevant documents found.")
            continue

        # 2️⃣ Use GPT to summarize / answer
        prompt = f"Use the following document excerpts to answer the question:\n\n"
        for i, doc in enumerate(top_docs, 1):
            prompt += f"Chunk {i}:\n{doc}\n\n"
        prompt += f"Question: {query}\nAnswer:"

        response = client.chat.completions.create(
            model=Settings.GENERATION_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        answer = response.choices[0].message.content
        print("\nAnswer:\n", answer)
