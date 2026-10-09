"""
JSON Writer implementation.
"""

import json
import os

from exceptions.file_write_exception import FileWriteException

from .data_writer import Writer


class JSONWriter(Writer):
    """
    Writer class for JSON format.
    """
    @staticmethod
    def convert_to_json(header, record):
        """
        Convert list objects to dictionary.
        """
        if len(header) != len(record):
            raise ValueError(
                'Invalid data passed for conversion'
            )

        result = dict(zip(header, record))
        return result

    def save_data(self, header, data, location, first_call):
        """
        Write data to a JSON file.

        Args:
            header: Key names for the entries
            data: Values for the entires
            location: Path to the output JSON file
        """
        try:
            super().save_data(header, data, location, first_call)

            new_records = [
                    self.convert_to_json(header, record)
                    for record in data
                ]

            if os.path.exists(location):
                with open(location, 'r', encoding='utf-8') as file:
                    records = json.load(file)

            else:
                records = []

            records.extend(new_records)

            with open(location, 'w', encoding='utf-8') as file:
                json.dump(records, file, ensure_ascii=False, indent=4)

        except OSError as e:
            raise FileWriteException(f'Failed to write to location. {e}')