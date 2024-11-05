import fitz

class PDFHelper:
    @staticmethod
    def extract_text_from_page(file_path: str, page_number: int) -> str:
        """Извлекает текст с указанной страницы PDF файла."""
        with fitz.open(file_path) as pdf:
            page = pdf.load_page(page_number - 1)
            return page.get_text()