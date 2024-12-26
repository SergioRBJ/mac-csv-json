import pandas as pd
import json
import os
from datetime import datetime

INPUT_DIR = "input"
OUTPUT_DIR = "output"

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

INPUT_FILE = os.path.join(INPUT_DIR, "input.csv")
timestamp = int(datetime.now().timestamp())
OUTPUT_FILE = os.path.join(OUTPUT_DIR, f"result_{timestamp}.json")

def process_csv_to_json(input_csv):
    try:
        df = pd.read_csv(input_csv)
        df.columns = [col.lower() for col in df.columns]

        perguntas_dict = {}

        for _, row in df.iterrows():
            pergunta = row['pergunta']
            tipo = row['tipo']
            genero = row['genero']
            grupo = row['grupo']
            peso = row['peso']

            if pergunta in perguntas_dict:
                perguntas_dict[pergunta]['grupos'].append({"grupo": grupo, "peso": peso})
            else:
                perguntas_dict[pergunta] = {
                    "pergunta": pergunta,
                    "tipo": tipo,
                    "genero": genero,
                    "grupos": [{"grupo": grupo, "peso": peso}]
                }

        resultado = list(perguntas_dict.values())

        with open(OUTPUT_FILE, "w", encoding="utf-8") as json_file:
            json.dump(resultado, json_file, ensure_ascii=False, indent=4)

        print(f"JSON successfully generated at: {OUTPUT_FILE}")

    except Exception as e:
        print(f"Error processing the CSV: {e}")