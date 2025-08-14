from services.pdf_service import extract_pdf_text_with_ocr

# Test with a scanned file
pages, ocr_pages = extract_pdf_text_with_ocr("data/scanned_sample.pdf")
print(f"Total pages: {len(pages)}")
print(f"OCR used on: {ocr_pages}")

# Test with a digital file
pages, ocr_pages = extract_pdf_text_with_ocr("data/nike_report.pdf")
print(f"Total pages: {len(pages)}")
print(f"OCR used on: {ocr_pages}")
