# esg_extractor/tests/test_pdf_extraction.py

import sys
import os
import pytesseract

# Allow importing from 'services'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services.pdf_service import extract_pdf_text_with_ocr

# -------------------- CONFIG --------------------

# Poppler bin path for Windows (adjust to your installation)
poppler_path = r"C:\poppler-24.08.0\Library\bin"

# Tesseract executable path for Windows (adjust if installed elsewhere)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Output folder for extracted text
output_dir = r"C:\ELM's Challenge\esg_extractor\data\extracted_text"
os.makedirs(output_dir, exist_ok=True)

# -------------------- HELPER FUNCTION --------------------

def write_pdf_text_to_file(pages, ocr_pages, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for page in pages:
            f.write(f"--- Page {page['page_num']} ---\n")
            f.write(page['text'] + "\n\n")
        f.write("=== OCR was used on pages: ===\n")
        f.write(", ".join(str(p) for p in ocr_pages) + "\n")

# -------------------- PROCESS PDFs --------------------

pdf_files = {
    "scanned_pdf": r"C:\ELM's Challenge\esg_extractor\data\FY23_Nike_Impact_Report (2).pdf",
    "digital_pdf": r"C:\ELM's Challenge\esg_extractor\data\scanned_sample.pdf"
}

for name, path in pdf_files.items():
    print(f"Processing {name}...")
    pages, ocr_pages = extract_pdf_text_with_ocr(path, poppler_path=poppler_path)
    print(f"{name} - Total pages: {len(pages)}")
    print(f"{name} - OCR used on: {ocr_pages}")

    output_file = os.path.join(output_dir, f"{name}_text.txt")
    write_pdf_text_to_file(pages, ocr_pages, output_file)
    print(f"Text written to: {output_file}\n")
