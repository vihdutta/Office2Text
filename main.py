#!/usr/bin/env python3

import sys
import os
from pdf_extractor import extract_text_from_pdf
from pptx_extractor import extract_text_from_pptx
from docx_extractor import extract_text_from_docx
from xlsx_extractor import extract_data_from_excel
from util import extractor

EXTRACTORS = {
    '.pdf': extract_text_from_pdf,
    '.pptx': extract_text_from_pptx,
    '.docx': extract_text_from_docx,
    '.xlsx': extract_data_from_excel
}

FILE_TYPES = {
    '.pdf': 'file',
    '.pptx': 'presentation',
    '.docx': 'document',
    '.xlsx': 'file'
}

def main():
    if len(sys.argv) != 2:
        print("Usage: ./main.py <input_file_name_and_extension>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file + ".json"

    file_extension = os.path.splitext(input_file)[1].lower()

    if file_extension not in EXTRACTORS:
        print(f"Error: Unsupported file type '{file_extension}'")
        sys.exit(1)

    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist")
        sys.exit(1)

    extract_function = EXTRACTORS[file_extension]
    file_type = FILE_TYPES[file_extension]

    try:
        extractor(input_file, output_file, extract_function, file_type)
    except Exception as e:
        print(f"Error: An exception occurred while processing the file: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()