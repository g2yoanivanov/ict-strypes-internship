from zipfile import ZipFile
import os
import re

def extract_instructions():
    zip_path = os.path.join('.', 'unzip_me_for_instructions.zip')

    extract_dir = os.path.join('.', 'extracted')

    with ZipFile(zip_path, 'r') as z:
        z.extractall(extract_dir)

def read_instructiopns():
    instructions = os.path.join(
        '.',
        'extracted',
        'extracted_content',
        'Instructions.txt'
    )
    with open(instructions, 'r') as f:
        print(f.read())

def find_phone_number():
    search_dir = os.path.join(
        '.',
        'extracted',
        'extracted_content'
    )

    for root, _, files in os.walk(search_dir):
        for file in files:
            path = os.path.join(root, file)

            with open(path, 'r') as searchable:
                match = re.search(
                    r'\d{3}-\d{3}-\d{4}',
                    searchable.read()
                )

                if match:
                    print(match.group() + f' in {path}')
                    break

read_instructiopns()
find_phone_number()