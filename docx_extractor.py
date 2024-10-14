import docx
from util import extractor

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    full_text = []
    
    for para in doc.paragraphs:
        full_text.append(para.text)
    
    return full_text

if __name__ == "__main__":
    input_docx = 'test_documents/test.docx'
    output_json = 'output_docx.json'
    extractor(input_docx, output_json, extract_text_from_docx, "document")