# esg_extractor/services/pdf_service.py

import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
import os

def extract_pdf_text_with_ocr(pdf_path, min_length=20, ocr_lang="eng", poppler_path=None):
    """
    Extract text from a PDF using PyMuPDF, with OCR fallback via pdf2image + pytesseract.

    Args:
        pdf_path (str): Path to the PDF file
        min_length (int): Minimum length of text before OCR is triggered
        ocr_lang (str): Language for pytesseract OCR
        poppler_path (str, optional): Path to Poppler 'bin' folder (Windows only)

    Returns:
        pages_data (list of dict): List of pages with text
        ocr_pages (list of int): Pages where OCR was used
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    doc = fitz.open(pdf_path)
    pages_data = []
    ocr_pages = []

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text").strip()

        if len(text) < min_length:
            try:
                images = convert_from_path(
                    pdf_path,
                    first_page=page_num,
                    last_page=page_num,
                    poppler_path=poppler_path  # Works on Windows
                )
            except Exception as e:
                print(f"[Warning] Could not convert page {page_num} to image: {e}")
                images = []

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
