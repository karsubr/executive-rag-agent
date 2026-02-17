from pypdf import PdfReader

class DocumentLoader:

    @staticmethod
    def load_pdf(path: str) -> str:
        reader = PdfReader(path)
        text = ""

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

        return text
