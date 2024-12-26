import json
import pandas as pd
import os
from datetime import datetime

INPUT_DIR = "input"
OUTPUT_DIR = "output"

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_json_to_csv(input_json):
    try:
        with open(input_json, 'r', encoding='utf-8') as file:
            data = json.load(file)

        csv_rows = []

        for item in data:
            pergunta = item['pergunta']
            tipo = item['tipo']
            genero = item['genero']

            for grupo in item['grupos']:
                csv_rows.append({
                    'PERGUNTA': pergunta,
                    'TIPO': tipo,
                    'GENERO': genero,
                    'GRUPO': grupo['grupo'],
                    'PESO': grupo['peso']
                })

        df = pd.DataFrame(csv_rows)

        timestamp = int(datetime.now().timestamp())
        output_file = os.path.join(OUTPUT_DIR, f"result_{timestamp}.csv")

        df.to_csv(output_file, index=False, encoding='utf-8')

        print(f"CSV successfully generated at: {output_file}")

    except Exception as e:
        print(f"Error processing the JSON: {e}")

if __name__ == "__main__":
    input_file = os.path.join(INPUT_DIR, "input.json")
    if os.path.exists(input_file):
        process_json_to_csv(input_file)
    else:
        print(f"Error: The input file '{input_file}' was not found.")