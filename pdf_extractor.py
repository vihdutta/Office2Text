from pypdf import PdfReader
from util import extractor

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    pdf_data = []
    
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        pdf_data.append({
            "page_number": page_number,
            "content": text
        })
    
    return pdf_data

if __name__ == "__main__":
    input_pdf = 'test_documents/test.pdf'
    output_json = 'output_pdf.json'
    extractor(input_pdf, output_json, extract_text_from_pdf, "file")