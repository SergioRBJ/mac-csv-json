import os
from csv_to_json import process_csv_to_json
from json_to_csv import process_json_to_csv

INPUT_DIR = "input"
INPUT_FILE = os.path.join(INPUT_DIR, "input")

def get_input_file():
    for ext in ['.csv', '.json']:
        if os.path.exists(INPUT_FILE + ext):
            return INPUT_FILE + ext
    return None

if __name__ == "__main__":
    input_file = get_input_file()
    
    if not input_file:
        print(f"Error: No input file with .csv or .json extension was found in the '{INPUT_DIR}' directory.")
    else:
        file_extension = os.path.splitext(input_file)[1].lower()
        
        if file_extension == '.csv':
            process_csv_to_json(input_file)
        elif file_extension == '.json':
            process_json_to_csv(input_file)
        else:
            print(f"Error: Unsupported file extension '{file_extension}'. Only .csv and .json are supported.")
