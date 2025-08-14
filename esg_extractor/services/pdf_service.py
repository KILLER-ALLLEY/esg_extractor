import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path

def extract_pdf_text_with_ocr(pdf_path, min_length=20, ocr_lang="eng"):
    doc = fitz.open(pdf_path)
    pages_data = []
    ocr_pages = []

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text").strip()

        if len(text) < min_length:
            images = convert_from_path(pdf_path, first_page=page_num, last_page=page_num)
            if images:
                ocr_text = pytesseract.image_to_string(images[0], lang=ocr_lang).strip()
                if ocr_text:
                    text = ocr_text
                    ocr_pages.append(page_num)

        pages_data.append({
            "page_num": page_num,
            "text": text
        })

    return pages_data, ocr_pages
