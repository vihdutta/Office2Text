import json

def save_as_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def extractor(input_file, output_file, extract_function, file_type):
    extracted_data = extract_function(input_file)
    
    data = {
        f"{file_type}_name": input_file,
        "content": extracted_data
    }
    
    save_as_json(data, output_file)
    print(f"Data extracted from '{input_file}' and saved to '{output_file}'")