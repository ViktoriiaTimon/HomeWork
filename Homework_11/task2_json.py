from constants import BASE_PATH

import os
import json
import logging

logging.basicConfig(filename='json_error_file.log',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

main_folder = os.path.join(BASE_PATH, 'work_with_json')

for path_, folder, files in os.walk(main_folder):

    for file in files:
        file_path = os.path.join(path_, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                json_content = json.load(f)
            if not isinstance(json_content, dict):
                raise ValueError("File does not match expected JSON structure (must be a JSON object).")
        except json.JSONDecodeError as e:
             logging.error(f"Invalid JSON in file {file_path}: {e}")
        except ValueError as e:
            logging.error(f"Structural issue in file {file_path}: {e}")
        except Exception as e:
            logging.error(f"Error processing file {file_path}: {e}")



