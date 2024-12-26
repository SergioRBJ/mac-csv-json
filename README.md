# MAC - Microscopia A Chinesa: CSV-JSON Converter

This project provides tools to convert data between CSV and JSON formats, specifically designed for the Microscopia A Chinesa (MAC) project.

## Description

The project consists of two main scripts:

1. `csv_to_json.py`: Converts data from CSV to JSON.
2. `json_to_csv.py`: Converts data from JSON to CSV.

These scripts are useful for manipulating and transforming data between CSV and JSON formats, maintaining the specific structure required for the MAC project.

## Requirements

- Python 3.6+
- pandas
- Other dependencies listed in `requirements.txt`

## Installation

1. Create and activate a virtual environment:

`python -m venv venv` <br>
`source venv/bin/activate`

On Windows use `venv\Scripts\activate`

3. Install the dependencies:

`pip install -r requirements.txt`

## Usage

1. Place your input file (either CSV or JSON) in the `input` folder with the name `input.csv` or `input.json`.
2. Run the main script:

`python main.py`

3. The script will automatically detect the input file type and perform the appropriate conversion.
4. The resulting file (JSON or CSV) will be generated in the `output` folder with a name in the format `result_[timestamp].[json/csv]`.

## Notes

- Ensure that the input files are in the correct format and contain all necessary fields.
- The scripts will automatically create the `input` and `output` folders if they don't exist.
- Output files are named with a timestamp to avoid overwriting existing files.
