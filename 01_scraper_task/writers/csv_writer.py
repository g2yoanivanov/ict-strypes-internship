"""
CSV Writer implementation.
"""

import csv
import os

from exceptions.file_write_exception import FileWriteException

from .data_writer import Writer


class CSVWriter(Writer):
    """
    Writer class for CSV format.
    """
    def save_data(self, header, data, location, first_call):
        """
        Write data to a CSV  file.
    
        Args:
            header: Column names written as first row
            data: Scraped records to be written
            location: Path to the output CSV file
        """
        try:
            super().save_data(header, data, location, first_call)

            file_exists = os.path.exists(location)

            with open(location, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                if not file_exists:
                    writer.writerow(header)

                writer.writerows(data)
        except OSError as e:
            raise FileWriteException(f'Failed to write to location. {e}')
