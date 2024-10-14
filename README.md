# Document Data Extractor

This project provides a terminal Python script to extract data from various document formats (PDF, PPTX, DOCX, XLSX) and save the extracted text information in JSON files.

## Modules

### util.py

This module contains common utility functions used across all extractor scripts:

- `save_as_json(data, output_file)`: Saves the extracted data as a JSON file.
- `extractor(input_file, output_file, extract_function, file_type)`: A generic function that handles the extraction process for all document types.

### Extractor Scripts

1. **pdf_extractor.py**: Extracts text from PDF files.
2. **pptx_extractor.py**: Extracts text from PowerPoint presentations.
3. **docx_extractor.py**: Extracts text from Word documents.
4. **xlsx_extractor.py**: Extracts data from Excel spreadsheets.

Each extractor script contains a specific function to extract data from its respective file type and uses the common `extractor` function from `util.py` to process the data and save it as JSON.

## Dependencies
- pypdf: For PDF extraction
- python-pptx: For PowerPoint extraction
- python-docx: For Word document extraction
- openpyxl: For Excel spreadsheet extraction

## Usage

`python3 main.py <input_file_name> <output_file_name>.json`

Working example with test documents:
- `python3 main.py test_documents/test.docx test.json`

Note that you will always specify <output_name>**.json** for the output file since everything is a json. It is manually entered for consistency with the `<input_file_name>`.